"""Gera figuras estáticas (matplotlib) no estilo dos widgets do site,
para uso nos slides. Salva em assets/slides/."""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats
from pathlib import Path

BASE = Path(__file__).parent.parent
OUT = BASE / "assets" / "slides"
OUT.mkdir(parents=True, exist_ok=True)

# paleta do site
INK = "#1a1a1a"
PAPER = "#fffdf8"
BG = "#f3ecdf"
BLUE = "#3266ad"
RED = "#c0392b"
GREEN = "#1a7a4a"
MUTED = "#6b6457"

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 13,
    "axes.edgecolor": "#b9ad95",
    "axes.linewidth": 0.9,
    "axes.titlesize": 14,
    "figure.facecolor": PAPER,
    "axes.facecolor": PAPER,
    "savefig.facecolor": PAPER,
    "axes.grid": True,
    "grid.color": "#e2d9c4",
    "grid.linewidth": 0.7,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "axes.labelcolor": INK,
    "text.color": INK,
})

rng = np.random.default_rng(7)


def save(fig, name):
    fig.tight_layout()
    p = OUT / name
    fig.savefig(p, dpi=150, bbox_inches="tight", facecolor=PAPER)
    plt.close(fig)
    print("OK", p.relative_to(BASE))


# 1 — Curva normal com 68-95-99,7
def fig_normal():
    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    x = np.linspace(-4, 4, 500)
    y = stats.norm.pdf(x)
    for k, a in [(3, 0.10), (2, 0.18), (1, 0.30)]:
        m = (x >= -k) & (x <= k)
        ax.fill_between(x[m], y[m], color=BLUE, alpha=a)
    ax.plot(x, y, color=BLUE, lw=2.4)
    ax.axvline(0, color=INK, ls="--", lw=1.3)
    for k, lbl in [(1, "68,3%"), (2, "95,4%"), (3, "99,7%")]:
        ax.annotate(f"±{k}σ → {lbl}", xy=(0, stats.norm.pdf(k)),
                    xytext=(k+0.15, 0.30 - 0.07*k), color=BLUE, fontsize=11)
    ax.set_yticks([])
    ax.set_xlabel("desvios padrão a partir da média")
    ax.set_title("Distribuição normal e a regra 68–95–99,7")
    save(fig, "normal.png")


# 2 — Histograma + curva teórica
def fig_histograma():
    data = rng.normal(0, 1, 800)
    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    ax.hist(data, bins=22, density=True, color=BLUE, alpha=0.55, edgecolor=PAPER)
    x = np.linspace(-4, 4, 300)
    ax.plot(x, stats.norm.pdf(x), color=RED, lw=2.2, label="curva teórica")
    ax.axvline(data.mean(), color=INK, ls="--", lw=1.3, label="média amostral")
    ax.set_yticks([])
    ax.legend(frameon=False)
    ax.set_title("Histograma de uma amostra com a curva normal sobreposta")
    save(fig, "histograma.png")


# 3 — TLC: convergência para a normal
def fig_tlc():
    fig, axes = plt.subplots(1, 4, figsize=(11.5, 3.0))
    pop = rng.exponential(1.0, 200000)
    for ax, n in zip(axes, [1, 2, 5, 30]):
        means = pop[: (len(pop)//n)*n].reshape(-1, n).mean(axis=1)
        ax.hist(means, bins=40, density=True, color=BLUE, alpha=0.6, edgecolor=PAPER)
        ax.set_title(f"n = {n}", fontsize=12)
        ax.set_yticks([])
        ax.set_xticks([])
    axes[0].set_ylabel("densidade")
    fig.suptitle("Teorema do limite central: a média de amostras tende à normal", y=1.02)
    save(fig, "tlc.png")


# 4 — Boxplot + histograma
def fig_boxplot():
    data = rng.exponential(1.0, 300) * 4 + 6
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(7.2, 4.0), height_ratios=[3, 1], sharex=True)
    a1.hist(data, bins=30, color=BLUE, alpha=0.55, edgecolor=PAPER)
    a1.set_yticks([]); a1.grid(False)
    a1.set_title("Histograma e boxplot dos mesmos dados (assimétricos)")
    bp = a2.boxplot(data, vert=False, widths=0.6, patch_artist=True,
                    medianprops=dict(color=RED, lw=2.4),
                    flierprops=dict(marker="o", markerfacecolor=RED, markersize=4, markeredgecolor=RED))
    bp["boxes"][0].set(facecolor=BLUE, alpha=0.35, edgecolor=INK)
    for w in bp["whiskers"] + bp["caps"]:
        w.set(color=INK)
    a2.set_yticks([]); a2.grid(False)
    a2.set_xlabel("valor")
    save(fig, "boxplot.png")


# 5 — Tendência central com outlier
def fig_tendencia():
    base = np.array([3, 4, 4, 5, 5, 5, 6, 6, 7, 22])
    fig, ax = plt.subplots(figsize=(7.2, 3.4))
    # dotplot
    from collections import Counter
    c = Counter(base)
    for val, cnt in c.items():
        for i in range(cnt):
            ax.plot(val, i, "o", color=BLUE, ms=10)
    ax.axvline(base.mean(), color=RED, ls="--", lw=2, label=f"média = {base.mean():.1f}")
    ax.axvline(np.median(base), color=GREEN, ls="--", lw=2, label=f"mediana = {np.median(base):.1f}")
    ax.set_ylim(-0.5, 4)
    ax.set_yticks([]); ax.grid(False)
    ax.set_xlabel("valor")
    ax.legend(frameon=False, loc="upper center")
    ax.set_title("Um valor extremo puxa a média, mas não a mediana")
    save(fig, "tendencia.png")


# 6 — Precisão x acurácia (4 alvos)
def fig_precisao():
    fig, axes = plt.subplots(1, 4, figsize=(11.5, 3.2))
    cenarios = [
        ("Acurado e preciso", 0.0, 0.12),
        ("Preciso, não acurado", 0.55, 0.12),
        ("Acurado, não preciso", 0.0, 0.40),
        ("Nem um, nem outro", 0.55, 0.40),
    ]
    for ax, (titulo, vies, ruido) in zip(axes, cenarios):
        for r in [1.0, 0.66, 0.33]:
            ax.add_patch(plt.Circle((0, 0), r, color="#efe6d4", ec="#cbbfa5", zorder=0))
        ax.plot(0, 0, "+", color=RED, ms=10, mew=2)
        ang = rng.uniform(0, 2*np.pi)
        pts = rng.normal(0, ruido, (18, 2)) + np.array([vies*np.cos(ang), vies*np.sin(ang)])
        ax.plot(pts[:, 0], pts[:, 1], "o", color=BLUE, ms=5, alpha=0.8)
        ax.set_xlim(-1.2, 1.2); ax.set_ylim(-1.2, 1.2)
        ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(titulo, fontsize=10.5)
    fig.suptitle("Acurácia (perto do centro) × Precisão (tiros agrupados)", y=1.04)
    save(fig, "precisao.png")


# 7 — Distribuição binomial
def fig_binomial():
    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    n, p = 20, 0.5
    k = np.arange(0, n+1)
    ax.bar(k, stats.binom.pmf(k, n, p), color=BLUE, alpha=0.7, edgecolor=PAPER)
    ax.set_xlabel("número de sucessos")
    ax.set_ylabel("probabilidade")
    ax.set_title(f"Distribuição binomial (n = {n}, p = {p})")
    ax.grid(axis="x")
    save(fig, "binomial.png")


# 8 — Sensibilidade e especificidade (duas distribuições + corte)
def fig_sens_esp():
    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    x = np.linspace(-4, 8, 500)
    saud = stats.norm.pdf(x, 0, 1)
    doe = stats.norm.pdf(x, 3, 1)
    corte = 1.5
    ax.fill_between(x, saud, where=(x >= corte), color=RED, alpha=0.3, label="falso positivo")
    ax.fill_between(x, doe, where=(x < corte), color=BLUE, alpha=0.3, label="falso negativo")
    ax.plot(x, saud, color=BLUE, lw=2.2)
    ax.plot(x, doe, color=RED, lw=2.2)
    ax.axvline(corte, color=INK, ls="--", lw=1.5)
    ax.text(0, 0.42, "saudáveis", color=BLUE, ha="center", fontsize=11)
    ax.text(3, 0.42, "doentes", color=RED, ha="center", fontsize=11)
    ax.text(corte, 0.45, "corte", color=INK, ha="center", fontsize=10)
    ax.set_yticks([]); ax.legend(frameon=False, loc="upper right")
    ax.set_title("Sensibilidade, especificidade e o ponto de corte")
    save(fig, "sens_esp.png")


# 9 — Curva ROC
def fig_roc():
    fig, ax = plt.subplots(figsize=(6.4, 4.4))
    t = np.linspace(-6, 8, 400)
    for sep, lbl, cor in [(3.0, "excelente (AUC≈0,98)", BLUE),
                          (1.5, "bom (AUC≈0,86)", "#5a8fd0"),
                          (0.7, "fraco (AUC≈0,69)", RED)]:
        ax.plot(1-stats.norm.cdf(t), 1-stats.norm.cdf(t-sep), color=cor, lw=2.3, label=lbl)
    ax.plot([0, 1], [0, 1], "--", color="#999", lw=1.4, label="inútil (0,5)")
    ax.set_xlabel("1 − especificidade"); ax.set_ylabel("sensibilidade")
    ax.legend(frameon=False, fontsize=9, loc="lower right")
    ax.set_title("Curva ROC")
    save(fig, "roc.png")


# 10 — Intervalo de confiança
def fig_ic():
    fig, ax = plt.subplots(figsize=(6.0, 5.0))
    mu, sd, n = 100, 15, 30
    for i in range(30):
        s = rng.normal(mu, sd, n)
        m = s.mean(); sem = s.std(ddof=1)/np.sqrt(n)
        lo, hi = m - 1.96*sem, m + 1.96*sem
        cobre = lo <= mu <= hi
        ax.plot([lo, hi], [i, i], color=BLUE if cobre else RED, lw=2)
        ax.plot(m, i, "o", color=BLUE if cobre else RED, ms=3)
    ax.axvline(mu, color=INK, ls="--", lw=1.5)
    ax.set_yticks([]); ax.set_xlabel("média estimada")
    ax.set_title("Intervalos de confiança 95%\n(vermelho = não contém μ)")
    save(fig, "ic.png")


# 11 — Valor-p
def fig_valorp():
    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    x = np.linspace(-4, 4, 500); y = stats.norm.pdf(x)
    z = 1.96
    ax.fill_between(x, y, where=(x >= z), color=RED, alpha=0.4)
    ax.fill_between(x, y, where=(x <= -z), color=RED, alpha=0.4)
    ax.plot(x, y, color=BLUE, lw=2.2)
    ax.axvline(z, color=INK, ls="--", lw=1.3)
    ax.axvline(-z, color=INK, ls="--", lw=1.3)
    ax.set_yticks([])
    ax.set_title("Valor-p: área nas caudas além da estatística observada")
    save(fig, "valorp.png")


# 12 — Erros tipo I e II
def fig_erros():
    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    x = np.linspace(-4, 7, 500)
    h0 = stats.norm.pdf(x, 0, 1); h1 = stats.norm.pdf(x, 3, 1)
    zc = stats.norm.ppf(0.95)
    ax.fill_between(x, h0, where=(x >= zc), color=RED, alpha=0.35, label="α (erro tipo I)")
    ax.fill_between(x, h1, where=(x < zc), color=BLUE, alpha=0.35, label="β (erro tipo II)")
    ax.plot(x, h0, color=BLUE, lw=2.2); ax.plot(x, h1, color=RED, lw=2.2)
    ax.axvline(zc, color=INK, ls="--", lw=1.3)
    ax.text(0, 0.42, "H₀", color=BLUE, ha="center"); ax.text(3, 0.42, "H₁", color=RED, ha="center")
    ax.set_yticks([]); ax.legend(frameon=False, loc="upper left", fontsize=10)
    ax.set_title("Erros tipo I (α) e tipo II (β)")
    save(fig, "erros.png")


# 13 — Correlação com resíduos
def fig_correlacao():
    fig, ax = plt.subplots(figsize=(6.6, 4.4))
    x = rng.normal(0, 1, 40)
    y = 0.7*x + np.sqrt(1-0.49)*rng.normal(0, 1, 40)
    b1 = np.cov(x, y)[0, 1]/np.var(x, ddof=1)
    b0 = y.mean() - b1*x.mean()
    xs = np.array([x.min(), x.max()])
    for xi, yi in zip(x, y):
        ax.plot([xi, xi], [yi, b0+b1*xi], color=RED, alpha=0.4, lw=1)
    ax.plot(x, y, "o", color=BLUE, alpha=0.75, ms=5)
    ax.plot(xs, b0+b1*xs, color=RED, lw=2)
    ax.set_xlabel("X"); ax.set_ylabel("Y")
    ax.set_title("Correlação e resíduos (r ≈ 0,7)")
    save(fig, "correlacao.png")


# 14 — Distribuições t, chi2, F
def fig_dist_amostral():
    fig, axes = plt.subplots(1, 3, figsize=(11.5, 3.2))
    x = np.linspace(-4, 4, 300)
    axes[0].plot(x, stats.norm.pdf(x), "--", color=GREEN, lw=1.6, label="normal")
    for df in [1, 3, 30]:
        axes[0].plot(x, stats.t.pdf(x, df), lw=1.8, label=f"t (df={df})")
    axes[0].set_title("t de Student"); axes[0].legend(frameon=False, fontsize=8); axes[0].set_yticks([])
    xc = np.linspace(0, 20, 300)
    for df in [2, 4, 8]:
        axes[1].plot(xc, stats.chi2.pdf(xc, df), lw=1.8, label=f"df={df}")
    axes[1].set_title("χ² (qui-quadrado)"); axes[1].legend(frameon=False, fontsize=8); axes[1].set_yticks([])
    xf = np.linspace(0, 5, 300)
    for d1, d2 in [(2, 10), (5, 10), (10, 20)]:
        axes[2].plot(xf, stats.f.pdf(xf, d1, d2), lw=1.8, label=f"F({d1},{d2})")
    axes[2].set_title("F"); axes[2].legend(frameon=False, fontsize=8); axes[2].set_yticks([])
    fig.suptitle("Distribuições derivadas da amostragem de normais", y=1.03)
    save(fig, "dist_amostral.png")


# 15 — Regressão linear
def fig_regressao():
    fig, ax = plt.subplots(figsize=(6.6, 4.4))
    altura = np.array([152,157,163,168,173,178,183,188,193])
    peso = np.array([38,43,64,70,54,79,66,89,68])
    reg = stats.linregress(altura, peso)
    xs = np.array([altura.min(), altura.max()])
    ax.plot(altura, peso, "o", color=BLUE, ms=7)
    ax.plot(xs, reg.intercept + reg.slope*xs, color=RED, lw=2)
    ax.set_xlabel("altura (cm)"); ax.set_ylabel("peso (kg)")
    ax.set_title(f"Regressão linear: y = {reg.slope:.2f}x − {abs(reg.intercept):.0f}  (R² = {reg.rvalue**2:.2f})")
    save(fig, "regressao.png")


# 16 — ANOVA (3 grupos)
def fig_anova():
    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    centros = [10, 11.5, 13]
    cols = [BLUE, RED, GREEN]
    for gi, (c, col) in enumerate(zip(centros, cols)):
        vals = rng.normal(c, 1.2, 12)
        jx = gi + rng.uniform(-0.12, 0.12, 12)
        ax.plot(jx, vals, "o", color=col, alpha=0.7, ms=6)
        ax.plot([gi-0.25, gi+0.25], [vals.mean()]*2, color=col, lw=3)
    ax.set_xticks([0, 1, 2]); ax.set_xticklabels(["Grupo A", "Grupo B", "Grupo C"])
    ax.set_ylabel("valor")
    ax.set_title("ANOVA: variação entre grupos × dentro dos grupos")
    save(fig, "anova.png")


if __name__ == "__main__":
    for fn in [fig_normal, fig_histograma, fig_tlc, fig_boxplot, fig_tendencia,
               fig_precisao, fig_binomial, fig_sens_esp, fig_roc, fig_ic,
               fig_valorp, fig_erros, fig_correlacao, fig_dist_amostral,
               fig_regressao, fig_anova]:
        fn()
    print("\nFiguras geradas em assets/slides/")
