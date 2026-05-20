"""Notebooks por tema dos exercícios (apenas temas com computação)."""
import json
from pathlib import Path
BASE = Path(__file__).parent.parent

def md(t): return {"cell_type": "markdown", "metadata": {}, "source": t.splitlines(keepends=True)}
def code(t): return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": t.splitlines(keepends=True)}
def save(p, cells):
    nb = {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python", "version": "3.11"}}, "nbformat": 4, "nbformat_minor": 5}
    (BASE / p).write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
    print("OK", p)

S = "import numpy as np\nimport pandas as pd\nfrom scipy import stats\n"

save("07_exercicios/01_precisao_acuracia.ipynb", [
    md("# Exercícios — Precisão e acurácia"), code(S),
    md("## Exercício 1 — Pipeta"),
    code("p200 = pd.Series([198.75, 198.83, 198.78, 198.87])\n"
         "p1000 = pd.Series([996.41, 996.34, 996.48, 996.44])\n"
         "print('exatidão 200 (viés):', round(p200.mean()-200, 3))\n"
         "print('exatidão 1000 (viés):', round(p1000.mean()-1000, 3))\n"
         "print('precisão 200 (DP):', round(p200.std(), 4))\n"
         "print('precisão 1000 (DP):', round(p1000.std(), 4))\n"
         "print('CV 200 (%):', round(stats.variation(p200)*100, 4))\n"
         "print('CV 1000 (%):', round(stats.variation(p1000)*100, 4))"),
    md("## Exercício 5 — Béqueres"),
    code("b = pd.Series([33.45,35.21,35.77,35.20,34.72,33.81,33.91,34.54,34.63,34.12])\n"
         "print('média:', round(b.mean(),3), '| viés vs 35:', round(b.mean()-35,3))\n"
         "print('DP (precisão):', round(b.std(),3))"),
])

save("07_exercicios/03_probabilidade.ipynb", [
    md("# Exercícios — Probabilidade"), code(S),
    md("## Exercício 1 — Chevalier de Méré"),
    code("print('ao menos um 6 em 4 jogadas:', round(1-(5/6)**4, 4))\n"
         "print('ao menos um duplo-6 em 24:', round(1-(35/36)**24, 4))"),
    md("## Exercício 2 — Megasena"),
    code("from math import comb\nprint('P =', 1/comb(60,6))"),
    md("## Exercício 3 — Falso positivo na publicação"),
    code("print('independente:', 0.05*0.05)\nprint('dependente:', 0.05*0.30)"),
])

save("07_exercicios/04_probabilidade_condicional.ipynb", [
    md("# Exercícios — Probabilidade condicional"), code(S),
    md("Teorema de Bayes: P(D|+) = sens·prev / [sens·prev + (1−esp)·(1−prev)]"),
    md("## Exercício 1 — Rastreio (prev 0,01%)"),
    code("prev, sens, esp = 0.0001, 0.99, 0.95\n"
         "print('P(doente|+) =', round(sens*prev/(sens*prev+(1-esp)*(1-prev)), 5))"),
    md("## Exercício 2 — Previsão do tempo"),
    code("prev, sens, esp = 0.1, 0.8, 0.9\n"
         "print('P(chuva|previsão+) =', round(sens*prev/(sens*prev+(1-esp)*(1-prev)), 4))"),
    md("## Exercício 3 — AVC e pressão alta"),
    code("prev, sens, esp = 0.10, 0.40, 0.80\n"
         "print('P(AVC|PA alta) =', round(sens*prev/(sens*prev+(1-esp)*(1-prev)), 4))"),
])

save("07_exercicios/05_descritiva.ipynb", [
    md("# Exercícios — Estatística descritiva"), code(S),
    md("## Exercício 2 — Salários"),
    code("sal = pd.Series([2]*1000 + [3]*3000 + [4]*6000)\n"
         "print('média:', sal.mean(), '| mediana:', sal.median())"),
    md("## Exercício 3 — Faixas de renda (mediana acumulada)"),
    code("faixas = pd.DataFrame({'faixa':['<1','1-1.5','1.5-3','3-5','5-10','10+'],\n"
         "                       'pct':[24.1,20.6,28.5,11.7,8.5,6.6]})\n"
         "faixas['acum'] = faixas['pct'].cumsum()\nfaixas"),
])

save("07_exercicios/06_binomial.ipynb", [
    md("# Exercícios — Distribuição binomial"), code(S),
    md("## Exercício 1 — Falsos positivos acumulados"),
    code("for k in [3,10,50]:\n    print(f'{k} testes: P(>=1 FP) =', round(1-0.95**k, 4))"),
    md("## Exercício 2 — Pôquer (>=3 vitórias em 10, p=1/4)"),
    code("print(round(1 - stats.binom.cdf(2, 10, 0.25), 4))"),
    md("## Exercício 3 — Mudas"),
    code("print('P(nenhuma contaminação):', round(0.94**50, 4))\n"
         "print('P(<10 contaminadas):', round(stats.binom.cdf(9, 50, 0.06), 4))"),
    md("## Exercício 4 — Prova de múltipla escolha"),
    code("print('10 questões:', round(1-stats.binom.cdf(4,10,0.2), 4))\n"
         "print('20 questões:', round(1-stats.binom.cdf(9,20,0.25), 4))"),
    md("## Exercício 5 — Controle de qualidade"),
    code("print(round(1 - stats.binom.cdf(1, 10, 0.005), 4))"),
    md("## Exercício 6 — Genética 3:1"),
    code("print('P(>=80 amarelas):', round(1-stats.binom.cdf(79,100,0.75), 3))"),
])

save("07_exercicios/07_normal.ipynb", [
    md("# Exercícios — Distribuição normal"), code(S),
    md("## Exercício 1 — Regra 68-95-99,7"),
    code("for k in [1,2,3]:\n    print(f'±{k}σ:', round(stats.norm.cdf(k)-stats.norm.cdf(-k), 4))"),
    md("## Exercício 3 — Elevador (soma de pesos)"),
    code("for n in [7,6]:\n"
         "    mu, sd = 70*n, 10*np.sqrt(n)\n"
         "    print(f'{n} passageiros: P(soma>500) =', round(1-stats.norm.cdf(500, mu, sd), 4))"),
    md("## Exercício 4 — Pressão arterial N(100,10)"),
    code("print('% entre 80 e 120:', round(stats.norm.cdf(120,100,10)-stats.norm.cdf(80,100,10), 4))\n"
         "print('faixa 95%:', np.round(stats.norm.interval(0.95,100,10), 1))\n"
         "print('1% acima de:', round(stats.norm.ppf(0.99,100,10), 1))"),
    md("## Exercício 5 — Média de 4 pessoas"),
    code("print('faixa 95% das médias (σ conhecido):', np.round(stats.norm.interval(0.95,100,10/2),1))\n"
         "print('com s=7,8 (usa t, 3 gl):', round(stats.t.ppf(0.975,3)*7.8/2, 2))"),
    md("## Exercício 6 — Garantia"),
    code("print('% falha antes de 1 ano:', round(stats.norm.cdf(1, 1.5, 0.3), 4))"),
    md("## Exercício 7 — Temperatura"),
    code("print('frac entre 36,8 e 37,0:', round(stats.norm.cdf(37.0,36.8,0.15)-0.5, 3))\n"
         "print('faixa central 50%:', np.round(stats.norm.interval(0.5,36.8,0.15), 2))"),
])

save("07_exercicios/08_amostragem.ipynb", [
    md("# Exercícios — Distribuição amostral"), code(S),
    md("## Exercício 1 — Caixa de produtos"),
    code("mu = 500 + 50*10\nvar = 25**2 + 50*2**2\nsd = np.sqrt(var)\n"
         "print('média:', mu, '| DP:', round(sd,1))\n"
         "print('P(>1050):', round(1-stats.norm.cdf(1050, mu, sd), 4))"),
])

save("07_exercicios/09_inferencia_ic.ipynb", [
    md("# Exercícios — Inferência e intervalo de confiança"), code(S),
    md("## Exercício 3 — IC 95%"),
    code("a = pd.Series([5,3,4,2,3,4,2,3,4,5])\n"
         "print('média:', a.mean(), '| s:', round(a.std(),3))\n"
         "print('IC95%:', np.round(stats.t.interval(0.95, len(a)-1, a.mean(), stats.sem(a)), 2))"),
    md("## Exercício 4 — Moeda viciada (binomial, 20 lançamentos)"),
    code("p_caudas = stats.binom.cdf(5,20,0.5) + (1-stats.binom.cdf(14,20,0.5))\n"
         "print('P(<=5 ou >=15):', round(p_caudas, 4), '→ < 5% logo rejeita honesta')"),
])

save("07_exercicios/10_testes_dois_grupos.ipynb", [
    md("# Exercícios — Testes de dois grupos"), code(S),
    md("## Exercício 2 — Besouros (Mann-Whitney)"),
    code("a1 = pd.Series([8,12,15,21,25,44,44,60])\n"
         "a2 = pd.Series([2,4,5,9,12,17,19])\n"
         "stats.mannwhitneyu(a1, a2, alternative='two-sided')"),
    md("## Exercício 3 — Halotano x Morfina (t a partir de resumos)"),
    code("res = stats.ttest_ind_from_stats(66.9,12.2,61, 73.2,14.4,61)\nres"),
    md("## Exercício 4 — Pressão de homens e mulheres"),
    code("homens   = pd.Series([72,124,138,84,123,139,128,128,115,107,105,141])\n"
         "mulheres = pd.Series([57,143,112,133,140,156,132,121,140,175,98,142])\n"
         "stats.ttest_ind(homens, mulheres)"),
    md("## Exercício 5 — t não pareado"),
    code("a1 = pd.Series(range(0,10), dtype=float)\n"
         "a2 = pd.Series(range(3,13), dtype=float)\n"
         "stats.ttest_ind(a1, a2)"),
])

save("07_exercicios/11_anova.ipynb", [
    md("# Exercícios — ANOVA"), code(S),
    md("## Exercício 1 — Drogas A, B e placebo"),
    code("P = [5.4,4.0,7.0,5.8,3.5,7.6,5.5]\n"
         "A = [6.0,4.8,6.9,6.4,5.5,9.0,6.8]\n"
         "B = [5.1,3.9,6.5,5.6,3.9,7.0,5.4]\n"
         "stats.f_oneway(P, A, B)"),
    md("## Exercício 2 — Concurso (5 avaliadores × 6 candidatos)"),
    code("notas = pd.DataFrame({\n"
         "    'c1': [9.43,9.20,8.95,8.90,9.10],\n"
         "    'c2': [9.00,8.88,9.13,8.75,9.15],\n"
         "    'c3': [8.63,8.65,8.70,8.38,8.95],\n"
         "    'c4': [8.35,8.18,8.60,7.85,8.35],\n"
         "    'c5': [7.80,8.33,8.18,7.75,7.68],\n"
         "    'c6': [7.95,7.55,8.03,8.08,8.08],\n"
         "})\n"
         "print('médias dos candidatos:')\n"
         "print(notas.mean().round(3))\n"
         "stats.f_oneway(*[notas[c] for c in notas])"),
])

save("07_exercicios/12_correlacao_regressao.ipynb", [
    md("# Exercícios — Correlação e regressão"), code(S),
    md("## Exercício 1 — Peso x altura"),
    code("altura = pd.Series([152,157,163,168,173,178,183,188,193])\n"
         "peso = pd.Series([38,43,64,70,54,79,66,89,68])\n"
         "r, p = stats.pearsonr(altura, peso)\n"
         "reg = stats.linregress(altura, peso)\n"
         "print('r =', round(r,4), '| R² =', round(r**2,4))\n"
         "print(f'reta: y = {reg.slope:.2f}x + {reg.intercept:.1f}')"),
])

save("07_exercicios/13_potencia.ipynb", [
    md("# Exercícios — Potência"), code(S),
    md("## Exercício 1 — Erro padrão cai com a raiz de n"),
    code("for n in [2,3,4,6,10,20]:\n    print(f'n={n}: SEM ∝ 1/√n =', round(1/np.sqrt(n),3))"),
    md("## Exercício 2 — Escolha do sexo (4 meninos)"),
    code("print('P sob H0 =', (1/2)**4, '→ > 5%, teste inconclusivo')"),
    md("## Poder por simulação (t não pareado)"),
    code("def poder(n, delta, sigma=1, reps=2000, seed=0):\n"
         "    rng = np.random.default_rng(seed); r = 0\n"
         "    for _ in range(reps):\n"
         "        a = rng.normal(0, sigma, n); b = rng.normal(delta, sigma, n)\n"
         "        if stats.ttest_ind(a, b).pvalue < 0.05: r += 1\n"
         "    return r/reps\n"
         "print('n=17, delta=1:', poder(17, 1))"),
])

save("07_exercicios/14_qui_quadrado.ipynb", [
    md("# Exercícios — Qui-quadrado"), code(S),
    md("## Exercício 1 — Dado honesto"),
    code("obs = [8,11,7,12,15,7]\n"
         "print('60 lançamentos:', stats.chisquare(obs, [10]*6))\n"
         "print('600 lançamentos:', stats.chisquare([o*10 for o in obs], [100]*6))"),
    md("## Exercício 2 — Mendel 9:3:3:1"),
    code("obs = [315,108,101,32]; total = sum(obs)\n"
         "esp = [total*p for p in [9/16,3/16,3/16,1/16]]\n"
         "print('Mendel:', stats.chisquare(obs, esp))"),
])

save("07_exercicios/15_tabelas_contingencia.ipynb", [
    md("# Exercícios — Tabelas de contingência"), code(S),
    md("## Exercício 1 — Mortalidade Halotano x Morfina"),
    code("tab = np.array([[8, 10], [53, 51]])  # mortos / vivos\n"
         "chi2, p, dof, esp = stats.chi2_contingency(tab)\n"
         "print('chi2 =', round(chi2,3), '| p =', round(p,4))\n"
         "print('Fisher:', stats.fisher_exact(tab))"),
])

print("\nConcluído.")
