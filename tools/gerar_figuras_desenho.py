"""Figuras estáticas específicas para o deck de Desenho Experimental.
Salva em assets/slides/desenho/."""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from scipy import stats
from pathlib import Path

BASE = Path(__file__).parent.parent
OUT = BASE / "assets" / "slides" / "desenho"
OUT.mkdir(parents=True, exist_ok=True)

INK = "#1a1a1a"; PAPER = "#fffdf8"
BLUE = "#3266ad"; RED = "#c0392b"; GREEN = "#1a7a4a"; MUTED = "#6b6457"
BLUEF = "#dce7f4"; REDF = "#f6dedb"; GREENF = "#dcefe4"; GREYF = "#ece4d3"

plt.rcParams.update({
    "font.family": "serif", "font.size": 13,
    "axes.edgecolor": "#b9ad95", "axes.linewidth": 0.9,
    "axes.titlesize": 14, "figure.facecolor": PAPER, "axes.facecolor": PAPER,
    "savefig.facecolor": PAPER, "axes.grid": True,
    "grid.color": "#e2d9c4", "grid.linewidth": 0.7,
    "xtick.color": MUTED, "ytick.color": MUTED,
    "axes.labelcolor": INK, "text.color": INK,
})


def save(fig, name):
    fig.tight_layout()
    fig.savefig(OUT / name, dpi=150, bbox_inches="tight", facecolor=PAPER)
    plt.close(fig)
    print("OK", (OUT / name).relative_to(BASE))


# 1 — Curvas de poder × n para diferentes efeitos
def fig_poder_curvas():
    fig, ax = plt.subplots(figsize=(7.4, 4.4))
    ns = np.arange(2, 200, 2)
    cores = [(0.2, BLUE), (0.5, GREEN), (0.8, RED)]
    for d, cor in cores:
        zc = stats.norm.ppf(0.975)
        ncp = d * np.sqrt(ns / 2)
        power = stats.norm.cdf(ncp - zc) + stats.norm.cdf(-ncp - zc)
        ax.plot(ns, power, color=cor, lw=2.4, label=f"d = {d}")
    ax.axhline(0.8, color=MUTED, ls="--", lw=1.2)
    ax.text(195, 0.81, "poder 80%", color=MUTED, ha="right", fontsize=10)
    ax.set_xlabel("n por grupo")
    ax.set_ylabel("poder (1 − β)")
    ax.set_ylim(0, 1.02)
    ax.legend(frameon=False, loc="lower right", title="tamanho de efeito")
    ax.set_title("Poder × tamanho da amostra (teste t bilateral, α = 0,05)")
    save(fig, "poder_curvas.png")


# 2 — Quatro quadrantes (efeito × variabilidade)
def fig_quadrantes():
    fig, ax = plt.subplots(figsize=(7.6, 5.2))
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")

    def quad(cx, cy, w, h, top, body, fc, ec):
        ax.add_patch(FancyBboxPatch((cx - w/2, cy - h/2), w, h,
                     boxstyle="round,pad=0.2,rounding_size=0.25",
                     facecolor=fc, edgecolor=ec, lw=1.4))
        ax.text(cx, cy + h/2 - 0.5, top, ha="center", va="top",
                fontsize=11, weight="bold", color=ec)
        ax.text(cx, cy - 0.2, body, ha="center", va="center",
                fontsize=10, color=INK, wrap=True)

    quad(3, 7, 4, 3, "Quadrante fácil", "efeito grande,\nbaixa variabilidade\n→ amostra modesta", GREENF, GREEN)
    quad(7, 7, 4, 3, "Anômalo", "efeito grande,\nalta variabilidade\n→ algo estranho", GREYF, MUTED)
    quad(3, 2.8, 4, 3, "Difícil", "efeito pequeno,\nbaixa variabilidade\n→ exige n grande", BLUEF, BLUE)
    quad(7, 2.8, 4, 3, "Luta quotidiana", "efeito pequeno,\nalta variabilidade\n→ raramente conclusivo", REDF, RED)

    ax.text(0.2, 5, "← efeito grande     |     efeito pequeno →", rotation=90,
            ha="center", va="center", fontsize=10, color=MUTED)
    ax.text(5, 0.1, "← baixa variabilidade     |     alta variabilidade →",
            ha="center", va="center", fontsize=10, color=MUTED)
    save(fig, "quadrantes.png")


# 3 — Pareamento vs aleatório (variabilidade entre indivíduos vs do efeito)
def fig_pareamento():
    rng = np.random.default_rng(1)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))
    # painel A: não pareado — variação entre indivíduos domina
    n = 12
    ind_var = rng.normal(0, 3, n)
    antes = ind_var + rng.normal(0, 0.5, n)
    depois = ind_var + 1.0 + rng.normal(0, 0.5, n)  # efeito de +1
    axA = axes[0]
    axA.boxplot([antes, depois], labels=["antes", "depois"], widths=0.5,
                patch_artist=True,
                boxprops=dict(facecolor=BLUEF, edgecolor=BLUE),
                medianprops=dict(color=BLUE))
    axA.set_title("Tratando os dados como independentes")
    axA.set_ylabel("medida")
    axA.text(1.5, max(depois.max(), antes.max()) + 1,
             "a variabilidade entre indivíduos\nesconde o efeito",
             ha="center", fontsize=10, color=MUTED, style="italic")
    # painel B: pareado — olha as diferenças individuais
    axB = axes[1]
    for i in range(n):
        axB.plot([0, 1], [antes[i], depois[i]], "o-", color=BLUE, alpha=0.7)
    axB.set_xticks([0, 1]); axB.set_xticklabels(["antes", "depois"])
    axB.set_title("Pareando: cada indivíduo é seu próprio controle")
    axB.set_ylabel("medida")
    axB.text(0.5, axB.get_ylim()[1] * 0.9,
             "as diferenças individuais\nrevelam o efeito",
             ha="center", fontsize=10, color=GREEN, style="italic")
    save(fig, "pareamento.png")


# 4 — Os quatro pilares (quadro estilizado)
def fig_pilares():
    fig, ax = plt.subplots(figsize=(11, 3.6))
    ax.set_xlim(0, 12); ax.set_ylim(0, 4); ax.axis("off")
    pilares = [
        ("Controle", "manter constantes as\nvariáveis não estudadas", BLUE),
        ("Aleatorização", "sortear quem recebe\ncada tratamento", RED),
        ("Repetição", "medir vários indivíduos\npara reduzir o acaso", GREEN),
        ("Pareamento", "agrupar unidades\nsemelhantes em blocos", MUTED),
    ]
    for i, (titulo, corpo, cor) in enumerate(pilares):
        cx = 1.5 + i * 3.0
        ax.add_patch(FancyBboxPatch((cx - 1.3, 0.4), 2.6, 3.0,
                     boxstyle="round,pad=0.2,rounding_size=0.3",
                     facecolor=PAPER, edgecolor=cor, lw=1.6))
        ax.text(cx, 2.9, titulo, ha="center", va="center", fontsize=13,
                weight="bold", color=cor)
        ax.text(cx, 1.6, corpo, ha="center", va="center", fontsize=10.5,
                color=INK)
    save(fig, "pilares.png")


# 5 — Calculadora de potência (preview estático)
def fig_calc_preview():
    fig, ax = plt.subplots(figsize=(7.4, 4.4))
    ns = np.arange(2, 200, 2)
    d, alpha = 0.5, 0.05
    zc = stats.norm.ppf(1 - alpha/2)
    ncp = d * np.sqrt(ns / 2)
    power = stats.norm.cdf(ncp - zc) + stats.norm.cdf(-ncp - zc)
    ax.plot(ns, power, color=BLUE, lw=2.4)
    ax.axhline(0.8, color=GREEN, ls="--", lw=1.4)
    # encontra n para 80%
    i80 = int(np.argmax(power >= 0.8))
    ax.plot(ns[i80], power[i80], "o", color=RED, ms=10)
    ax.annotate(f"n ≈ {ns[i80]} para poder = 80%", xy=(ns[i80], power[i80]),
                xytext=(ns[i80] + 25, 0.55), fontsize=11, color=RED,
                arrowprops=dict(arrowstyle="->", color=RED))
    ax.set_xlabel("n por grupo"); ax.set_ylabel("poder")
    ax.set_ylim(0, 1.02)
    ax.set_title("Calculadora de potência (teste t, d = 0,5)")
    save(fig, "calc_preview.png")


if __name__ == "__main__":
    fig_poder_curvas()
    fig_quadrantes()
    fig_pareamento()
    fig_pilares()
    fig_calc_preview()
