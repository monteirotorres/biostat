"""Gera os notebooks das novas seções (distribuições amostrais, design,
amostragem, exercícios)."""

import json
from pathlib import Path

BASE = Path(__file__).parent.parent


def md(t): return {"cell_type": "markdown", "metadata": {}, "source": t.splitlines(keepends=True)}
def code(t): return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": t.splitlines(keepends=True)}
def nb(cells): return {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python", "version": "3.11"}}, "nbformat": 4, "nbformat_minor": 5}
def save(p, cells):
    p = BASE / p
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(nb(cells), ensure_ascii=False, indent=1), encoding="utf-8")
    print("OK", p.relative_to(BASE))


SETUP = """import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

sns.set_theme(style="whitegrid")
"""

# ---------- 05_distribuicoes_amostrais ----------
save("05_distribuicoes_amostrais/01_de_onde_vem.ipynb", [
    md("# De onde vêm t, F e χ²\n\nVamos ver, por simulação, que essas distribuições nascem da amostragem de variáveis normais."),
    code(SETUP),
    md("## A média amostral é normal (TLC)"),
    code("medias = [stats.norm.rvs(size=30, random_state=i).mean() for i in range(2000)]\n"
         "sns.histplot(medias, stat='density', bins=40)\n"
         "x = np.linspace(-1, 1, 200)\n"
         "plt.plot(x, stats.norm.pdf(x, 0, 1/np.sqrt(30)), 'r')\n"
         "plt.title('Distribuição da média amostral');"),
    md("Nos próximos notebooks construímos cada distribuição (χ², t, F) a partir de normais."),
])

save("05_distribuicoes_amostrais/02_qui_quadrado.ipynb", [
    md("# Construindo a distribuição qui-quadrado\n\n"
       "χ² com k graus de liberdade = soma de k normais padrão ao quadrado."),
    code(SETUP),
    code("rng = np.random.default_rng(0)\n"
         "k = 4\n"
         "amostras = (rng.normal(size=(20000, k))**2).sum(axis=1)\n"
         "sns.histplot(amostras, stat='density', bins=60)\n"
         "x = np.linspace(0, 25, 300)\n"
         "plt.plot(x, stats.chi2.pdf(x, df=k), 'r', label=f'chi2 teórica (df={k})')\n"
         "plt.legend();"),
    md("O histograma das somas de quadrados coincide com `stats.chi2`. Média ≈ k, variância ≈ 2k."),
    code("print('média simulada:', amostras.mean(), ' teórica:', k)\n"
         "print('variância simulada:', amostras.var(), ' teórica:', 2*k)"),
    md("## Efeito dos graus de liberdade"),
    code("x = np.linspace(0, 30, 300)\n"
         "for k in [1, 3, 6, 10]:\n"
         "    plt.plot(x, stats.chi2.pdf(x, df=k), label=f'df={k}')\n"
         "plt.legend(); plt.title('Distribuição qui-quadrado');"),
])

save("05_distribuicoes_amostrais/03_t_student.ipynb", [
    md("# Construindo a distribuição t de Student\n\n"
       "t surge quando padronizamos a média usando o desvio padrão **estimado** (s), não o populacional (σ)."),
    code(SETUP),
    code("rng = np.random.default_rng(0)\n"
         "n = 5\n"
         "ts = []\n"
         "for _ in range(20000):\n"
         "    x = rng.normal(0, 1, n)\n"
         "    ts.append(x.mean() / (x.std(ddof=1) / np.sqrt(n)))\n"
         "ts = np.array(ts)"),
    code("sns.histplot(ts, stat='density', bins=120)\n"
         "x = np.linspace(-6, 6, 400)\n"
         "plt.plot(x, stats.t.pdf(x, df=n-1), 'r', label=f't (df={n-1})')\n"
         "plt.plot(x, stats.norm.pdf(x), 'g--', label='normal')\n"
         "plt.xlim(-6, 6); plt.legend();"),
    md("Repare nas **caudas mais pesadas** que a normal (verde). Com n grande, t → normal."),
    code("x = np.linspace(-4, 4, 400)\n"
         "for df in [1, 3, 10, 30]:\n"
         "    plt.plot(x, stats.t.pdf(x, df=df), label=f'df={df}')\n"
         "plt.plot(x, stats.norm.pdf(x), 'k--', label='normal')\n"
         "plt.legend();"),
])

save("05_distribuicoes_amostrais/04_f_distribuicao.ipynb", [
    md("# Construindo a distribuição F\n\n"
       "F = razão entre duas variâncias (duas qui-quadrado, cada uma sobre seus gl)."),
    code(SETUP),
    code("rng = np.random.default_rng(0)\n"
         "d1, d2 = 5, 10\n"
         "fs = []\n"
         "for _ in range(20000):\n"
         "    a = rng.normal(size=d1+1)\n"
         "    b = rng.normal(size=d2+1)\n"
         "    fs.append(a.var(ddof=1) / b.var(ddof=1))\n"
         "fs = np.array(fs)"),
    code("sns.histplot(fs, stat='density', bins=80)\n"
         "x = np.linspace(0, 6, 300)\n"
         "plt.plot(x, stats.f.pdf(x, d1, d2), 'r', label=f'F({d1},{d2})')\n"
         "plt.xlim(0, 6); plt.legend();"),
    md("## Relação t² = F(1, k)"),
    code("k = 10\n"
         "t = stats.t.rvs(df=k, size=20000, random_state=0)\n"
         "print('quantil 95% de t²:', np.quantile(t**2, 0.95))\n"
         "print('quantil 95% de F(1,k):', stats.f.ppf(0.95, 1, k))"),
])

# ---------- 01_introducao/09 ----------
save("01_introducao/09_tecnicas_amostragem.ipynb", [
    md("# Técnicas de amostragem\n\nComo o método de amostragem afeta a representatividade."),
    code(SETUP),
    md("## Uma população com dois estratos"),
    code("rng = np.random.default_rng(0)\n"
         "pop = pd.DataFrame({\n"
         "    'grupo': ['A']*8000 + ['B']*2000,\n"
         "    'valor': np.concatenate([rng.normal(50, 5, 8000), rng.normal(80, 5, 2000)])\n"
         "})\n"
         "pop.groupby('grupo')['valor'].mean()"),
    md("## Amostra aleatória simples"),
    code("simples = pop.sample(100, random_state=1)\n"
         "simples['grupo'].value_counts()"),
    md("## Amostra estratificada (proporcional)"),
    code("estrat = pop.groupby('grupo', group_keys=False).apply(lambda g: g.sample(frac=0.01, random_state=1))\n"
         "estrat['grupo'].value_counts()"),
    code("print('média pop:       ', pop['valor'].mean())\n"
         "print('média simples:   ', simples['valor'].mean())\n"
         "print('média estratif.: ', estrat['valor'].mean())"),
    md("A estratificada garante a proporção certa de cada grupo e costuma estimar melhor a média."),
])

# ---------- 04_estatistica_inferencial/17 ----------
save("04_estatistica_inferencial/17_design_experimental.ipynb", [
    md("# Design experimental e potência\n\nSimulando o poder estatístico de um teste t."),
    code(SETUP),
    md("## Poder por simulação\n\nFração de experimentos em que rejeitamos H₀ quando há efeito real."),
    code("def poder_simulado(n, delta, sigma=1, alpha=0.05, reps=2000, seed=0):\n"
         "    rng = np.random.default_rng(seed)\n"
         "    rejeicoes = 0\n"
         "    for _ in range(reps):\n"
         "        a = rng.normal(0, sigma, n)\n"
         "        b = rng.normal(delta, sigma, n)\n"
         "        if stats.ttest_ind(a, b).pvalue < alpha:\n"
         "            rejeicoes += 1\n"
         "    return rejeicoes / reps\n\n"
         "poder_simulado(n=17, delta=1)"),
    md("## Curva de poder vs. tamanho da amostra"),
    code("ns = [5, 10, 17, 25, 40, 60, 100]\n"
         "poderes = [poder_simulado(n, delta=1) for n in ns]\n"
         "plt.plot(ns, poderes, 'o-')\n"
         "plt.axhline(0.8, color='red', linestyle='--', label='80%')\n"
         "plt.xlabel('n por grupo'); plt.ylabel('poder'); plt.legend();"),
    md("## Efeito do tamanho do efeito (δ)"),
    code("deltas = [0.2, 0.5, 0.8, 1.0, 1.5, 2.0]\n"
         "poderes = [poder_simulado(n=20, delta=d) for d in deltas]\n"
         "plt.plot(deltas, poderes, 'o-')\n"
         "plt.axhline(0.8, color='red', linestyle='--')\n"
         "plt.xlabel('tamanho do efeito (δ/σ)'); plt.ylabel('poder');"),
])

# ---------- 06_tabelas ----------
save("06_tabelas/01_tabelas.ipynb", [
    md("# Tabelas estatísticas com scipy\n\nComo obter qualquer valor crítico ou área sem consultar tabelas impressas."),
    code(SETUP),
    md("## Normal padrão (tabela Z)"),
    code("print('P(Z < 1.96) =', stats.norm.cdf(1.96))\n"
         "print('z para 95% bilateral =', stats.norm.ppf(0.975))"),
    md("## Valores críticos t"),
    code("for df in [5, 10, 30, 100]:\n"
         "    print(f'gl={df}: t* 95% = {stats.t.ppf(0.975, df):.3f}')"),
    md("## Valores críticos qui-quadrado"),
    code("for df in [1, 5, 10]:\n"
         "    print(f'gl={df}: chi2* (5%) = {stats.chi2.ppf(0.95, df):.3f}')"),
    md("## Valores críticos F (ANOVA)"),
    code("print('F* (5%, 2, 27) =', stats.f.ppf(0.95, 2, 27))"),
    md("## Construindo uma tabela Z em DataFrame"),
    code("z = np.round(np.arange(0, 3.5, 0.1), 1)\n"
         "cols = np.round(np.arange(0, 0.1, 0.01), 2)\n"
         "tab = pd.DataFrame({c: stats.norm.cdf(z + c) for c in cols}, index=z).round(4)\n"
         "tab.head(10)"),
])

# ---------- 07_exercicios ----------
save("07_exercicios/01_exercicios.ipynb", [
    md("# Exercícios resolvidos em Python\n\n"
       "Soluções de exercícios selecionados de cada tema, usando pandas e scipy.stats."),
    code(SETUP),
    md("## 1.1 — Calibração de pipeta"),
    code("p200 = pd.Series([198.75, 198.83, 198.78, 198.87])\n"
         "p1000 = pd.Series([996.41, 996.34, 996.48, 996.44])\n"
         "print('Exatidão 200 (viés):', p200.mean() - 200)\n"
         "print('Exatidão 1000 (viés):', p1000.mean() - 1000)\n"
         "print('Precisão 200 (DP):', p200.std())\n"
         "print('Precisão 1000 (DP):', p1000.std())\n"
         "print('CV 200 (%):', stats.variation(p200)*100)\n"
         "print('CV 1000 (%):', stats.variation(p1000)*100)"),
    md("## 3.1 — Chevalier de Méré"),
    code("p1 = 1 - (5/6)**4\n"
         "p2 = 1 - (35/36)**24\n"
         "print('ao menos um 6 em 4 jogadas:', p1)\n"
         "print('ao menos um duplo-6 em 24:', p2)"),
    md("## 3.2 — Megasena"),
    code("from math import comb\n"
         "print('P =', 1/comb(60, 6))"),
    md("## 4.1 — Rastreio (Bayes)"),
    code("prev, sens, esp = 0.0001, 0.99, 0.95\n"
         "vpp = sens*prev / (sens*prev + (1-esp)*(1-prev))\n"
         "print('P(doente | +) =', vpp)"),
    md("## 6.4 — Prova de múltipla escolha"),
    code("print('10 questões, P(passar):', 1 - stats.binom.cdf(4, 10, 0.2))\n"
         "print('20 questões, P(passar):', 1 - stats.binom.cdf(9, 20, 0.25))"),
    md("## 6.6 — Genética 3:1"),
    code("print('P(>=80 amarelas em 100):', 1 - stats.binom.cdf(79, 100, 0.75))"),
    md("## 7.4 — Pressão arterial N(100,10)"),
    code("print('% entre 80 e 120:', stats.norm.cdf(120,100,10) - stats.norm.cdf(80,100,10))\n"
         "print('faixa 95%:', stats.norm.interval(0.95, 100, 10))\n"
         "print('1% acima de:', stats.norm.ppf(0.99, 100, 10))"),
    md("## 9.3 — Intervalo de confiança"),
    code("amostra = pd.Series([5,3,4,2,3,4,2,3,4,5])\n"
         "ic = stats.t.interval(0.95, len(amostra)-1, amostra.mean(), stats.sem(amostra))\n"
         "print('média:', amostra.mean(), ' IC95%:', ic)"),
    md("## 10.2 — Besouros (Mann–Whitney)"),
    code("a1 = pd.Series([8,12,15,21,25,44,44,60])\n"
         "a2 = pd.Series([2,4,5,9,12,17,19])\n"
         "stats.mannwhitneyu(a1, a2)"),
    md("## 10.5 — Teste t não pareado"),
    code("a1 = pd.Series([0,1,2,3,4,5,6,7,8,9]) + 0.0\n"
         "a2 = pd.Series([3,4,5,6,7,8,9,10,11,12]) + 0.0\n"
         "stats.ttest_ind(a1, a2)"),
    md("## 11.1 — ANOVA drogas A, B, placebo"),
    code("P = [5.4,4.0,7.0,5.8,3.5,7.6,5.5]\n"
         "A = [6.0,4.8,6.9,6.4,5.5,9.0,6.8]\n"
         "B = [5.1,3.9,6.5,5.6,3.9,7.0,5.4]\n"
         "stats.f_oneway(P, A, B)"),
    md("## 12.1 — Peso × altura"),
    code("altura = pd.Series([152,157,163,168,173,178,183,188,193])\n"
         "peso = pd.Series([38,43,64,70,54,79,66,89,68])\n"
         "r, p = stats.pearsonr(altura, peso)\n"
         "reg = stats.linregress(altura, peso)\n"
         "print('r =', r, ' R² =', r**2)\n"
         "print(f'reta: y = {reg.slope:.2f}x + {reg.intercept:.1f}')"),
    md("## 14.1 — Dado honesto (qui-quadrado)"),
    code("obs = [8,11,7,12,15,7]\n"
         "esp = [10]*6\n"
         "print('60 lançamentos:', stats.chisquare(obs, esp))\n"
         "print('600 lançamentos:', stats.chisquare([o*10 for o in obs], [100]*6))"),
    md("## 14.2 — Mendel 9:3:3:1"),
    code("obs = [315,108,101,32]\n"
         "total = sum(obs)\n"
         "esp = [total*p for p in [9/16,3/16,3/16,1/16]]\n"
         "stats.chisquare(obs, esp)"),
])

print("\nConcluído.")
