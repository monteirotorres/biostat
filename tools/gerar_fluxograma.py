"""Gera o fluxograma de escolha de testes estatísticos (estilo do site).
Salva assets/fluxograma_testes.png."""

from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

BASE = Path(__file__).parent.parent
OUT = BASE / "assets" / "fluxograma_testes.png"

INK = "#1a1a1a"; PAPER = "#fffdf8"; BG = "#f3ecdf"
BLUE = "#3266ad"; RED = "#c0392b"; GREEN = "#1a7a4a"; MUTED = "#6b6457"
BLUEF = "#dce7f4"; REDF = "#f6dedb"; GREENF = "#dcefe4"; GREYF = "#ece4d3"

plt.rcParams["font.family"] = "serif"

fig, ax = plt.subplots(figsize=(14, 8.6))
fig.patch.set_facecolor(PAPER)
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")


def box(cx, cy, w, h, text, fc, ec=INK, tc=INK, fs=10.5, bold=False):
    ax.add_patch(FancyBboxPatch((cx - w/2, cy - h/2), w, h,
                 boxstyle="round,pad=0.4,rounding_size=1.2",
                 linewidth=1.1, edgecolor=ec, facecolor=fc, mutation_scale=1))
    ax.text(cx, cy, text, ha="center", va="center", fontsize=fs,
            color=tc, weight=("bold" if bold else "normal"), wrap=True)


def arrow(x1, y1, x2, y2, color=MUTED):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                 mutation_scale=12, lw=1.2, color=color, shrinkA=2, shrinkB=2))


def label(x, y, t, color=MUTED, fs=9, style="italic"):
    ax.text(x, y, t, ha="center", va="center", fontsize=fs, color=color, style=style)


# topo
box(50, 95, 30, 6, "Pergunta de pesquisa", GREYF, fs=12, bold=True)

# três famílias
box(19, 84, 30, 7, "Comparar grupos / médias\n(variável quantitativa)", BLUEF, ec=BLUE, fs=10.5, bold=True)
box(66, 84, 24, 7, "Associação entre duas\nvariáveis quantitativas", GREENF, ec=GREEN, fs=10.5, bold=True)
box(89, 84, 20, 7, "Variáveis categóricas\n(contagens / proporções)", REDF, ec=RED, fs=9.8, bold=True)
arrow(43, 93, 23, 87.5); arrow(52, 92.5, 66, 87.5); arrow(56, 93, 87, 87.5)

# ---- Família 1: grade paramétrico x não-paramétrico ----
label(19, 78.5, "A variável é aproximadamente normal (ou n grande)?", MUTED, 9)
# cabeçalhos de coluna
box(23, 74, 16, 4.2, "Paramétrico", BLUEF, ec=BLUE, tc=BLUE, fs=10, bold=True)
box(40, 74, 16, 4.2, "Não-paramétrico", REDF, ec=RED, tc=RED, fs=10, bold=True)
arrow(13, 80.5, 21, 76.2); arrow(24, 80.5, 40, 76.2)

linhas = [
    ("1 grupo vs. valor",   "Teste t de 1 amostra", "Wilcoxon do sinal"),
    ("2 grupos independentes", "Teste t (Welch)",     "Mann–Whitney"),
    ("2 grupos pareados",   "Teste t pareado",       "Wilcoxon pareado"),
    ("3+ grupos independentes", "ANOVA one-way",     "Kruskal–Wallis"),
    ("3+ grupos pareados",  "ANOVA medidas repet.",  "Friedman"),
]
y = 67.5
for est, par, npar in linhas:
    y -= 8.2
    box(7, y, 15, 5.2, est, GREYF, ec=MUTED, fs=9)
    box(23, y, 16, 5.2, par, PAPER, ec=BLUE, tc=BLUE, fs=9)
    box(40, y, 16, 5.2, npar, PAPER, ec=RED, tc=RED, fs=9)

# ---- Família 2: associação ----
arrow(66, 80.5, 66, 70)
box(66, 66, 22, 5, "Relação linear e\ndados ~normais?", PAPER, ec=GREEN, fs=9.5)
box(66, 56.5, 22, 5.2, "Sim → Pearson (r)\n+ regressão linear", GREENF, ec=GREEN, tc=GREEN, fs=9.5)
box(66, 47.5, 22, 5.2, "Não / ordinal →\nSpearman (postos)", PAPER, ec=GREEN, tc=GREEN, fs=9.5)
arrow(66, 63.5, 66, 59.2); arrow(66, 53.9, 66, 50.2)

# ---- Família 3: categóricas ----
arrow(89, 80.5, 89, 70)
box(89, 66, 20, 5, "Tabela de\ncontingência", PAPER, ec=RED, fs=9.5)
box(89, 57, 20, 5, "Qui-quadrado\n(esperados ≥ 5)", REDF, ec=RED, tc=RED, fs=9.5)
box(89, 48.5, 20, 5, "Fisher exato\n(amostra pequena)", PAPER, ec=RED, tc=RED, fs=9.5)
box(89, 40, 20, 5, "McNemar\n(dados pareados)", PAPER, ec=RED, tc=RED, fs=9.5)
arrow(89, 63.5, 89, 59.7); arrow(89, 54.4, 89, 51.1); arrow(89, 46, 89, 42.6)

# ---- faixa de post-tests (após ANOVA) ----
box(50, 10.5, 96, 9, "", "#f7f1e3", ec=MUTED)
ax.text(50, 14.5, "Pós-testes após ANOVA significativa", ha="center", va="center",
        fontsize=11, weight="bold", color=INK)
post = ("Todos × todos: Tukey HSD     ·     Cada grupo × controle: Dunnett     ·     "
        "Poucas comparações planejadas: Bonferroni / Šidák     ·     Combinações de médias: Scheffé")
ax.text(50, 8.5, post, ha="center", va="center", fontsize=9.5, color=MUTED)

fig.tight_layout()
fig.savefig(OUT, dpi=150, facecolor=PAPER, bbox_inches="tight")
print("OK", OUT.relative_to(BASE))
