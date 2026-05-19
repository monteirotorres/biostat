"""Gerador de notebooks Jupyter para o curso de Bioestatística.

Este script gera os arquivos .ipynb a partir de uma lista de células
estruturada. Não faz parte do conteúdo didático, é apenas uma utilidade.
"""

import json
from pathlib import Path

BASE = Path(__file__).parent.parent


def md(text: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": text.splitlines(keepends=True),
    }


def code(text: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": text.splitlines(keepends=True),
    }


def notebook(cells: list) -> dict:
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
                "version": "3.11",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def save(path: Path, nb: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)


# Setup comum reutilizado em vários notebooks
SETUP = """import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

sns.set_theme(style="whitegrid")
"""


# =====================================================================
# Parte 1 — Introdução
# =====================================================================

NOTEBOOKS = {}

NOTEBOOKS["01_introducao/01_amostra_populacao.ipynb"] = [
    md("# Amostra e população\n\n"
       "Vamos simular uma população e tirar amostras dela para ver como cada amostra "
       "estima o parâmetro verdadeiro."),
    code(SETUP),
    md("## Criando uma 'população' simulada\n\n"
       "Vamos imaginar a altura (em cm) de **100.000 adultos**. "
       "Como é uma simulação, nós conhecemos os parâmetros verdadeiros."),
    code("populacao = pd.Series(stats.norm.rvs(loc=170, scale=8, size=100_000, random_state=0))\n"
         "populacao.describe()"),
    md("A média **verdadeira** da população é 170 cm e o desvio padrão é 8 cm."),
    md("## Tirando uma amostra\n\n"
       "Vamos sortear apenas 30 pessoas dessa população."),
    code("amostra = populacao.sample(n=30, random_state=1)\n"
         "amostra.describe()"),
    md("Repare que a média da amostra (`mean`) é **próxima**, mas não igual a 170. "
       "Isso é normal — chamamos esse fenômeno de **erro amostral**."),
    md("## E se tirarmos várias amostras?"),
    code("medias = [populacao.sample(n=30, random_state=i).mean() for i in range(500)]\n"
         "medias = pd.Series(medias)\n"
         "sns.histplot(medias, bins=30)\n"
         "plt.axvline(170, color='red', label='média da população')\n"
         "plt.xlabel('média da amostra')\n"
         "plt.legend();"),
    md("Cada amostra dá uma média um pouco diferente, mas todas se concentram em torno do valor verdadeiro. "
       "Essa é a ideia central da inferência estatística."),
]

NOTEBOOKS["01_introducao/02_descricao_inferencia.ipynb"] = [
    md("# Descrição vs. inferência\n\n"
       "A **descrição** resume os dados que temos em mãos. A **inferência** generaliza esses dados "
       "para uma população maior."),
    code(SETUP),
    md("## Carregando um conjunto de dados real\n\n"
       "Vamos usar o famoso dataset de pinguins do `seaborn`."),
    code("df = sns.load_dataset('penguins').dropna()\n"
         "df.head()"),
    md("## Descrição: o que esses 333 pinguins têm?"),
    code("df['body_mass_g'].describe()"),
    md("Esse é um resumo **descritivo** — fala apenas dos pinguins que estão no dataset."),
    md("## Inferência: o que isso diz sobre TODOS os pinguins?"),
    code("stats.t.interval(0.95,\n"
         "                df=len(df) - 1,\n"
         "                loc=df['body_mass_g'].mean(),\n"
         "                scale=stats.sem(df['body_mass_g']))"),
    md("Esse intervalo é uma **inferência**: estimamos que a massa média dos pinguins (em geral) "
       "está dentro desse intervalo, com 95% de confiança."),
]

NOTEBOOKS["01_introducao/03_precisao_acuracia.ipynb"] = [
    md("# Precisão e acurácia\n\n"
       "Vamos simular quatro situações para visualizar a diferença."),
    code(SETUP),
    code("# Valor verdadeiro\n"
         "verdadeiro = 100\n\n"
         "cenarios = {\n"
         "    'Acurado e preciso':       stats.norm.rvs(loc=100, scale=1,  size=50, random_state=0),\n"
         "    'Preciso, não acurado':    stats.norm.rvs(loc=110, scale=1,  size=50, random_state=1),\n"
         "    'Acurado, não preciso':    stats.norm.rvs(loc=100, scale=8,  size=50, random_state=2),\n"
         "    'Nem acurado, nem preciso':stats.norm.rvs(loc=110, scale=8,  size=50, random_state=3),\n"
         "}\n"
         "df = pd.DataFrame(cenarios)\n"
         "df.head()"),
    code("sns.boxplot(data=df)\n"
         "plt.axhline(verdadeiro, color='red', linestyle='--', label='valor verdadeiro')\n"
         "plt.xticks(rotation=30, ha='right')\n"
         "plt.legend();"),
    md("- **Acurácia** = quão perto da linha vermelha (valor verdadeiro).\n"
       "- **Precisão** = quão pequena é a caixa (pouca dispersão)."),
]

NOTEBOOKS["01_introducao/04_algarismos_significativos.ipynb"] = [
    md("# Algarismos significativos\n\n"
       "Vamos ver como o Python lida com arredondamento."),
    code(SETUP),
    code("valor = 3.14159265\n"
         "round(valor, 2), round(valor, 4)"),
    md("## Em DataFrames"),
    code("df = pd.DataFrame({'altura': [1.6234, 1.7567, 1.8123],\n"
         "                   'peso':   [62.34,  75.671, 81.123]})\n"
         "df.round({'altura': 2, 'peso': 1})"),
    md("## Formatando para exibição"),
    code("for v in [12345.678, 0.000045678, 3.14]:\n"
         "    print(f'{v:.3g}')"),
]

NOTEBOOKS["01_introducao/05_notacao_cientifica.ipynb"] = [
    md("# Notação científica\n\n"
       "Python escreve automaticamente em notação científica para números muito grandes ou pequenos."),
    code(SETUP),
    code("# Número de Avogadro\n"
         "n_avogadro = 6.022e23\n"
         "print(n_avogadro)"),
    code("# Massa de um próton (kg)\n"
         "m_proton = 1.6726e-27\n"
         "print(m_proton)"),
    md("## Convertendo automaticamente"),
    code("df = pd.DataFrame({'concentracao_M': [1e-3, 5e-6, 2.3e-9, 4.5e-12]})\n"
         "df"),
    code("# Forçando notação científica na exibição\n"
         "pd.set_option('display.float_format', '{:.2e}'.format)\n"
         "df"),
    code("pd.reset_option('display.float_format')"),
]

NOTEBOOKS["01_introducao/06_tipos_variaveis.ipynb"] = [
    md("# Tipos de variáveis\n\n"
       "Vamos explorar diferentes tipos de variáveis no dataset `tips` do seaborn."),
    code(SETUP),
    code("df = sns.load_dataset('tips')\n"
         "df.head()"),
    code("df.dtypes"),
    md("## Variáveis qualitativas (categóricas)"),
    code("df['day'].value_counts()"),
    code("sns.countplot(data=df, x='day');"),
    md("## Variáveis quantitativas"),
    code("df['total_bill'].describe()"),
    code("sns.histplot(data=df, x='total_bill', bins=20);"),
    md("## Convertendo tipos"),
    code("df['sex'] = df['sex'].astype('category')\n"
         "df['sex'].cat.codes.head()"),
]

NOTEBOOKS["01_introducao/07_histogramas.ipynb"] = [
    md("# Histogramas\n\n"
       "O histograma mostra a **forma** da distribuição dos dados."),
    code(SETUP),
    code("df = sns.load_dataset('penguins').dropna()"),
    md("## Histograma simples"),
    code("sns.histplot(data=df, x='flipper_length_mm', bins=20);"),
    md("## Mudando o número de barras"),
    code("fig, axes = plt.subplots(1, 3, figsize=(12, 3))\n"
         "for ax, b in zip(axes, [5, 15, 50]):\n"
         "    sns.histplot(data=df, x='flipper_length_mm', bins=b, ax=ax)\n"
         "    ax.set_title(f'{b} barras')"),
    md("Poucas barras = perdemos detalhes. Muitas barras = ruído. O ideal fica no meio do caminho."),
    md("## Separando por grupo"),
    code("sns.histplot(data=df, x='flipper_length_mm', hue='species', bins=20);"),
    md("## Densidade (forma suavizada)"),
    code("sns.kdeplot(data=df, x='flipper_length_mm', hue='species', fill=True);"),
]

NOTEBOOKS["01_introducao/08_curva_normal.ipynb"] = [
    md("# Curva normal\n\n"
       "A distribuição normal é totalmente definida por dois parâmetros: **média** ($\\mu$) e **desvio padrão** ($\\sigma$)."),
    code(SETUP),
    md("## Como muda com $\\mu$ e $\\sigma$?"),
    code("import numpy as np\n"
         "x = np.linspace(-15, 15, 500)\n"
         "for mu, sigma, label in [(0, 1, 'μ=0, σ=1'),\n"
         "                         (0, 3, 'μ=0, σ=3'),\n"
         "                         (5, 1, 'μ=5, σ=1')]:\n"
         "    plt.plot(x, stats.norm.pdf(x, mu, sigma), label=label)\n"
         "plt.legend();"),
    md("## A regra 68-95-99,7\n\n"
       "Vamos verificar empiricamente em uma amostra de 100.000 valores."),
    code("amostra = pd.Series(stats.norm.rvs(loc=0, scale=1, size=100_000, random_state=0))\n"
         "for k in [1, 2, 3]:\n"
         "    pct = ((amostra > -k) & (amostra < k)).mean() * 100\n"
         "    print(f'Entre -{k}σ e +{k}σ: {pct:.1f}%')"),
    md("Bem próximo de 68%, 95% e 99,7%, como prevê a teoria."),
    md("## Calculando probabilidades"),
    code("# P(X < 1.5) em uma normal padrão\n"
         "stats.norm.cdf(1.5, loc=0, scale=1)"),
    code("# P(-1 < X < 1)\n"
         "stats.norm.cdf(1) - stats.norm.cdf(-1)"),
]


# =====================================================================
# Parte 2 — Estatística Descritiva
# =====================================================================

NOTEBOOKS["02_estatistica_descritiva/01_tendencia_central.ipynb"] = [
    md("# Medidas de tendência central\n\n"
       "As três principais são **moda**, **média** e **mediana**. "
       "Cada uma resume os dados de um jeito diferente."),
    code(SETUP),
    code("idades = pd.Series([21, 22, 22, 23, 23, 23, 24, 25, 26, 80])"),
    code("idades.mean(), idades.median(), idades.mode()[0]"),
    md("Repare como o valor `80` puxa a **média** para cima, mas a **mediana** mal se mexe. "
       "Essa é a principal lição: cada medida é sensível a coisas diferentes."),
]

NOTEBOOKS["02_estatistica_descritiva/02_moda.ipynb"] = [
    md("# Moda\n\nA **moda** é o valor que aparece mais vezes."),
    code(SETUP),
    code("dados = pd.Series([1, 2, 2, 3, 4, 4, 4, 5])\n"
         "dados.mode()"),
    md("## Mais de uma moda"),
    code("dados = pd.Series([1, 2, 2, 3, 3])\n"
         "dados.mode()  # bimodal"),
    md("## Moda em variáveis categóricas\n\nÉ a única medida de tendência central que funciona em texto."),
    code("df = sns.load_dataset('tips')\n"
         "df['day'].mode()"),
    code("sns.countplot(data=df, x='day');"),
]

NOTEBOOKS["02_estatistica_descritiva/03_media_aritmetica.ipynb"] = [
    md("# Média aritmética\n\n"
       "Soma todos os valores e divide pelo número deles."),
    code(SETUP),
    code("notas = pd.Series([6.0, 7.5, 8.0, 5.5, 9.0])\n"
         "notas.mean()"),
    md("## Em todo o DataFrame"),
    code("df = sns.load_dataset('penguins').dropna()\n"
         "df.select_dtypes('number').mean()"),
    md("## Por grupo"),
    code("df.groupby('species')['body_mass_g'].mean()"),
]

NOTEBOOKS["02_estatistica_descritiva/04_media_cortada.ipynb"] = [
    md("# Média cortada (truncada)\n\n"
       "Removemos uma porcentagem dos valores extremos antes de calcular a média. "
       "Isso reduz a influência de outliers."),
    code(SETUP),
    code("dados = pd.Series([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 200])"),
    code("dados.mean()"),
    code("# Cortando 10% de cada lado\n"
         "stats.trim_mean(dados, proportiontocut=0.1)"),
    md("Repare como a média cortada (~15) descreve melhor a maioria dos dados que a média "
       "comum (~31), distorcida pelo valor 200."),
]

NOTEBOOKS["02_estatistica_descritiva/05_media_ponderada.ipynb"] = [
    md("# Média ponderada\n\n"
       "Cada valor entra com um **peso** diferente. "
       "Útil quando alguns valores 'valem mais' que outros."),
    code(SETUP),
    md("## Exemplo clássico: nota final de uma disciplina"),
    code("notas = pd.DataFrame({\n"
         "    'avaliacao': ['P1', 'P2', 'Trabalho', 'Final'],\n"
         "    'nota':  [7.0, 6.0, 9.0, 8.0],\n"
         "    'peso':  [2,   3,   1,   4],\n"
         "})\n"
         "notas"),
    code("(notas['nota'] * notas['peso']).sum() / notas['peso'].sum()"),
]

NOTEBOOKS["02_estatistica_descritiva/06_media_geometrica.ipynb"] = [
    md("# Média geométrica\n\n"
       "Apropriada para taxas de crescimento, diluições em série, títulos de anticorpos — "
       "em geral, dados **multiplicativos**."),
    code(SETUP),
    code("# Crescimento bacteriano (vezes por hora)\n"
         "taxas = pd.Series([1.5, 2.0, 1.8, 2.2, 1.9])\n"
         "stats.gmean(taxas)"),
    md("## Diluições em série\n\nTítulos de anticorpos costumam ser reportados como média geométrica."),
    code("titulos = pd.Series([1/40, 1/80, 1/160, 1/320, 1/640])\n"
         "print('Média aritmética:', titulos.mean())\n"
         "print('Média geométrica:', stats.gmean(titulos))"),
]

NOTEBOOKS["02_estatistica_descritiva/07_mediana.ipynb"] = [
    md("# Mediana\n\nValor do meio quando os dados estão ordenados."),
    code(SETUP),
    code("dados = pd.Series([3, 1, 4, 1, 5, 9, 2, 6])\n"
         "dados.median()"),
    md("## Robustez a outliers"),
    code("d1 = pd.Series([1, 2, 3, 4, 5])\n"
         "d2 = pd.Series([1, 2, 3, 4, 500])\n"
         "print('média:    ', d1.mean(), d2.mean())\n"
         "print('mediana:  ', d1.median(), d2.median())"),
    md("A média muda muito; a mediana mal se mexe."),
]

NOTEBOOKS["02_estatistica_descritiva/08_media_vs_mediana.ipynb"] = [
    md("# Média x mediana\n\nQuando usar qual?"),
    code(SETUP),
    md("## Distribuição simétrica → tanto faz"),
    code("simetrica = pd.Series(stats.norm.rvs(loc=50, scale=10, size=1000, random_state=0))\n"
         "print('média:  ', simetrica.mean())\n"
         "print('mediana:', simetrica.median())\n"
         "sns.histplot(simetrica);"),
    md("## Distribuição assimétrica → mediana é mais representativa"),
    code("assimetrica = pd.Series(stats.expon.rvs(scale=50, size=1000, random_state=0))\n"
         "print('média:  ', assimetrica.mean())\n"
         "print('mediana:', assimetrica.median())\n"
         "sns.histplot(assimetrica);"),
    md("Em distribuições assimétricas (como renda, tempo de sobrevida, contagens), "
       "a **mediana** descreve melhor o 'indivíduo típico'."),
]

NOTEBOOKS["02_estatistica_descritiva/09_teorema_limite_central.ipynb"] = [
    md("# Teorema do limite central (TLC)\n\n"
       "Mesmo que a população tenha uma distribuição estranha, as **médias das amostras** "
       "tendem a uma distribuição normal — desde que a amostra seja grande o bastante."),
    code(SETUP),
    md("## População nada normal: uma exponencial"),
    code("import numpy as np\n"
         "populacao = pd.Series(stats.expon.rvs(scale=10, size=100_000, random_state=0))\n"
         "sns.histplot(populacao, bins=50);"),
    md("## Tirando 1000 amostras de tamanho n e calculando a média de cada uma"),
    code("def medias_de_amostras(n, k=1000):\n"
         "    return pd.Series([populacao.sample(n, random_state=i).mean() for i in range(k)])\n\n"
         "fig, axes = plt.subplots(1, 4, figsize=(15, 3))\n"
         "for ax, n in zip(axes, [2, 5, 30, 100]):\n"
         "    sns.histplot(medias_de_amostras(n), ax=ax, bins=30)\n"
         "    ax.set_title(f'n = {n}')"),
    md("Repare: quando a amostra cresce, a distribuição das médias fica cada vez mais parecida com "
       "uma curva normal — independentemente da forma original da população. Esse é o TLC."),
]

NOTEBOOKS["02_estatistica_descritiva/10_amplitude.ipynb"] = [
    md("# Amplitude\n\nMaior valor menos o menor valor."),
    code(SETUP),
    code("dados = pd.Series([12, 15, 18, 22, 25, 30])\n"
         "dados.max() - dados.min()"),
    md("## Limitação\n\n"
       "Depende apenas de dois valores e é muito sensível a outliers."),
    code("d1 = pd.Series([10, 12, 14, 16, 18])\n"
         "d2 = pd.Series([10, 12, 14, 16, 500])\n"
         "print(d1.max() - d1.min())\n"
         "print(d2.max() - d2.min())"),
]

NOTEBOOKS["02_estatistica_descritiva/11_desvio_medio.ipynb"] = [
    md("# Desvio médio\n\nMédia das distâncias até a média, em valor absoluto."),
    code(SETUP),
    code("dados = pd.Series([2, 4, 4, 4, 5, 5, 7, 9])\n"
         "(dados - dados.mean()).abs().mean()"),
    md("Atalho usando `mad` do pandas (em versões mais novas, usar a expressão acima)."),
]

NOTEBOOKS["02_estatistica_descritiva/12_variancia.ipynb"] = [
    md("# Variância\n\n"
       "Média dos quadrados das distâncias até a média. "
       "Por elevar ao quadrado, fica numa unidade diferente (kg² em vez de kg)."),
    code(SETUP),
    code("dados = pd.Series([2, 4, 4, 4, 5, 5, 7, 9])\n"
         "dados.var()  # divide por n-1 (variância amostral)"),
    code("dados.var(ddof=0)  # divide por n (variância populacional)"),
    md("`ddof=1` (padrão do pandas) é o caso amostral. `ddof=0` é o populacional."),
]

NOTEBOOKS["02_estatistica_descritiva/13_desvio_padrao.ipynb"] = [
    md("# Desvio padrão\n\nRaiz quadrada da variância. Volta para a mesma unidade dos dados."),
    code(SETUP),
    code("df = sns.load_dataset('penguins').dropna()\n"
         "df.groupby('species')['body_mass_g'].agg(['mean', 'std'])"),
    code("sns.boxplot(data=df, x='species', y='body_mass_g');"),
    md("## Populacional vs. amostral"),
    code("dados = pd.Series([10, 12, 14, 16, 18])\n"
         "print('amostral:    ', dados.std())             # ddof=1 (padrão)\n"
         "print('populacional:', dados.std(ddof=0))"),
]

NOTEBOOKS["02_estatistica_descritiva/14_desvio_interquartil.ipynb"] = [
    md("# Desvio interquartil (IQR)\n\n"
       "Diferença entre o terceiro e o primeiro quartil. "
       "Descreve a dispersão dos **50% centrais** dos dados — robusto a outliers."),
    code(SETUP),
    code("df = sns.load_dataset('penguins').dropna()\n"
         "q1 = df['body_mass_g'].quantile(0.25)\n"
         "q3 = df['body_mass_g'].quantile(0.75)\n"
         "iqr = q3 - q1\n"
         "print(f'Q1 = {q1}, Q3 = {q3}, IQR = {iqr}')"),
    md("Função pronta:"),
    code("stats.iqr(df['body_mass_g'])"),
    md("## Boxplot mostra o IQR visualmente"),
    code("sns.boxplot(data=df, y='body_mass_g');"),
]

NOTEBOOKS["02_estatistica_descritiva/15_coeficiente_variacao.ipynb"] = [
    md("# Coeficiente de variação (CV)\n\n"
       "Desvio padrão dividido pela média, em porcentagem. "
       "É a dispersão **relativa**."),
    code(SETUP),
    code("df = sns.load_dataset('penguins').dropna()\n"
         "stats.variation(df['body_mass_g']) * 100"),
    md("## Comparando variabilidade entre grupos com escalas diferentes"),
    code("df.groupby('species')['body_mass_g'].agg(\n"
         "    media='mean', desvio='std',\n"
         "    cv=lambda x: stats.variation(x) * 100\n"
         ")"),
]


# =====================================================================
# Parte 3 — Probabilidade
# =====================================================================

NOTEBOOKS["03_probabilidade/01_evento.ipynb"] = [
    md("# Evento — definição\n\n"
       "Um **evento** é um resultado (ou conjunto de resultados) possível de um experimento aleatório."),
    code(SETUP),
    md("## Simulando 10.000 lançamentos de moeda"),
    code("import numpy as np\n"
         "lancamentos = pd.Series(np.random.default_rng(0).choice(['cara', 'coroa'], size=10_000))\n"
         "lancamentos.value_counts(normalize=True)"),
    md("## Simulando lançamentos de dado"),
    code("dado = pd.Series(np.random.default_rng(0).integers(1, 7, size=10_000))\n"
         "(dado == 6).mean()  # P(sair 6)"),
    code("(dado % 2 == 0).mean()  # P(número par)"),
]

NOTEBOOKS["03_probabilidade/02_eventos_compostos.ipynb"] = [
    md("# Eventos compostos\n\n"
       "União ($A \\cup B$) e interseção ($A \\cap B$)."),
    code(SETUP),
    code("import numpy as np\n"
         "rng = np.random.default_rng(0)\n"
         "dado = pd.Series(rng.integers(1, 7, size=10_000))"),
    md("## P(par OU maior que 4)"),
    code("par = dado % 2 == 0\n"
         "maior4 = dado > 4\n"
         "(par | maior4).mean()"),
    md("## P(par E maior que 4)"),
    code("(par & maior4).mean()"),
    md("## Regra da adição"),
    code("p_par = par.mean()\n"
         "p_maior4 = maior4.mean()\n"
         "p_par_e_maior4 = (par & maior4).mean()\n"
         "p_par + p_maior4 - p_par_e_maior4  # confere com a união"),
]

NOTEBOOKS["03_probabilidade/03_probabilidade_condicional.ipynb"] = [
    md("# Probabilidade condicional\n\n"
       "$P(A \\mid B)$ = probabilidade de A, **sabendo que** B aconteceu."),
    code(SETUP),
    code("df = sns.load_dataset('titanic')\n"
         "df[['sex', 'survived']].head()"),
    md("## P(sobreviver)"),
    code("df['survived'].mean()"),
    md("## P(sobreviver | sexo = feminino)"),
    code("df.groupby('sex')['survived'].mean()"),
    md("Repare como a probabilidade muda muito quando condicionamos no sexo. "
       "Os dois eventos não são independentes."),
]

NOTEBOOKS["03_probabilidade/04_analise_combinatoria.ipynb"] = [
    md("# Análise combinatória\n\n"
       "Quantas formas existem de organizar ou escolher elementos?"),
    code(SETUP),
    md("## Fatorial"),
    code("from math import factorial\n"
         "factorial(5)  # 5! = 120"),
    md("## Combinações: escolher k entre n (a ordem não importa)"),
    code("from math import comb\n"
         "comb(60, 6)  # mega-sena"),
    md("## Permutações: ordenar k entre n (a ordem importa)"),
    code("from math import perm\n"
         "perm(10, 3)  # quantos pódios em uma corrida de 10 atletas?"),
    md("## Probabilidade de ganhar na mega-sena"),
    code("1 / comb(60, 6)"),
]

NOTEBOOKS["03_probabilidade/05_testes_binarios.ipynb"] = [
    md("# Testes binários\n\n"
       "Um teste binário retorna apenas dois resultados: **positivo** ou **negativo**. "
       "Quase todo teste diagnóstico cai aqui."),
    code(SETUP),
    md("Vamos simular 1000 pacientes em que 10% têm a doença e o teste acerta 95% das vezes."),
    code("import numpy as np\n"
         "rng = np.random.default_rng(0)\n"
         "n = 1000\n"
         "doente = rng.random(n) < 0.10\n"
         "# Sensibilidade = 95%, Especificidade = 95%\n"
         "teste_pos = np.where(doente,\n"
         "                     rng.random(n) < 0.95,\n"
         "                     rng.random(n) < 0.05)\n"
         "df = pd.DataFrame({'doente': doente, 'teste_positivo': teste_pos})\n"
         "df.head()"),
    code("pd.crosstab(df['doente'], df['teste_positivo'], margins=True)"),
]

NOTEBOOKS["03_probabilidade/06_sensibilidade_especificidade.ipynb"] = [
    md("# Sensibilidade e especificidade\n\n"
       "São propriedades **do teste**, calculadas em pessoas cujo diagnóstico verdadeiro é conhecido."),
    code(SETUP),
    code("df = pd.DataFrame({\n"
         "    'doente':         [True]*90  + [False]*910,\n"
         "    'teste_positivo': [True]*85  + [False]*5   + [True]*45 + [False]*865,\n"
         "})\n"
         "tab = pd.crosstab(df['doente'], df['teste_positivo'])\n"
         "tab"),
    code("VP, FN = tab.loc[True, True], tab.loc[True, False]\n"
         "FP, VN = tab.loc[False, True], tab.loc[False, False]\n"
         "print('Sensibilidade:', VP / (VP + FN))\n"
         "print('Especificidade:', VN / (VN + FP))"),
]

NOTEBOOKS["03_probabilidade/07_matriz_confusao.ipynb"] = [
    md("# Matriz de confusão\n\n"
       "Tabela 2×2 que mostra acertos e erros do teste."),
    code(SETUP),
    code("import numpy as np\n"
         "rng = np.random.default_rng(0)\n"
         "doente = rng.random(1000) < 0.20\n"
         "teste_pos = np.where(doente, rng.random(1000) < 0.90, rng.random(1000) < 0.10)"),
    code("matriz = pd.crosstab(pd.Series(doente, name='verdadeiro'),\n"
         "                     pd.Series(teste_pos, name='teste'))\n"
         "matriz"),
    code("sns.heatmap(matriz, annot=True, fmt='d', cmap='Blues');"),
]

NOTEBOOKS["03_probabilidade/08_valor_preditivo.ipynb"] = [
    md("# Valor preditivo positivo e negativo\n\n"
       "Respondem à pergunta do paciente: 'meu teste deu positivo, qual a chance de eu ter mesmo a doença?'"),
    code(SETUP),
    code("df = pd.DataFrame({\n"
         "    'doente':         [True]*90  + [False]*910,\n"
         "    'teste_positivo': [True]*85  + [False]*5   + [True]*45 + [False]*865,\n"
         "})\n"
         "tab = pd.crosstab(df['teste_positivo'], df['doente'])\n"
         "tab"),
    code("VP = tab.loc[True, True]\n"
         "FP = tab.loc[True, False]\n"
         "VN = tab.loc[False, False]\n"
         "FN = tab.loc[False, True]\n\n"
         "print('VPP:', VP / (VP + FP))\n"
         "print('VPN:', VN / (VN + FN))"),
    md("VPP e VPN **dependem da prevalência**, ao contrário de sensibilidade e especificidade."),
]

NOTEBOOKS["03_probabilidade/09_curva_roc.ipynb"] = [
    md("# Curva ROC\n\n"
       "Mostra como o teste se comporta para **diferentes valores de corte**."),
    code(SETUP),
    code("import numpy as np\n"
         "rng = np.random.default_rng(0)\n"
         "n = 500\n"
         "doentes = stats.norm.rvs(loc=60, scale=10, size=n, random_state=0)\n"
         "saudaveis = stats.norm.rvs(loc=40, scale=10, size=n, random_state=1)\n"
         "df = pd.concat([\n"
         "    pd.DataFrame({'valor': doentes,   'doente': True}),\n"
         "    pd.DataFrame({'valor': saudaveis, 'doente': False}),\n"
         "])"),
    code("sns.histplot(data=df, x='valor', hue='doente', bins=30);"),
    code("# Calcula sens. e (1-esp.) para cada corte\n"
         "cortes = pd.Series(range(20, 80))\n"
         "tpr = cortes.apply(lambda c: ((df['valor'] >= c) & df['doente']).sum() / df['doente'].sum())\n"
         "fpr = cortes.apply(lambda c: ((df['valor'] >= c) & ~df['doente']).sum() / (~df['doente']).sum())\n"
         "plt.plot(fpr, tpr)\n"
         "plt.plot([0,1], [0,1], '--', color='gray')\n"
         "plt.xlabel('1 - especificidade (FPR)')\n"
         "plt.ylabel('sensibilidade (TPR)');"),
]

NOTEBOOKS["03_probabilidade/10_distribuicao_binomial.ipynb"] = [
    md("# Distribuição binomial\n\n"
       "Conta o número de sucessos em $n$ tentativas independentes, cada uma com a mesma probabilidade $p$ de sucesso."),
    code(SETUP),
    md("## Lançar 10 moedas — quantas caras?"),
    code("import numpy as np\n"
         "n, p = 10, 0.5\n"
         "k = np.arange(0, n+1)\n"
         "probs = stats.binom.pmf(k, n, p)\n"
         "pd.Series(probs, index=k).plot.bar()\n"
         "plt.xlabel('caras')\n"
         "plt.ylabel('probabilidade');"),
    md("## Pelo menos 7 caras em 10 jogadas"),
    code("1 - stats.binom.cdf(6, n=10, p=0.5)"),
    md("## Simulando 5000 experimentos"),
    code("amostras = pd.Series(stats.binom.rvs(n=10, p=0.5, size=5000, random_state=0))\n"
         "amostras.value_counts().sort_index()"),
]


# =====================================================================
# Parte 4 — Estatística Inferencial
# =====================================================================

NOTEBOOKS["04_estatistica_inferencial/01_logica_inferencia.ipynb"] = [
    md("# Lógica da inferência\n\n"
       "A inferência estatística assume que **a hipótese nula é verdadeira** e calcula a probabilidade dos dados terem ocorrido."),
    code(SETUP),
    md("## Exemplo: a moeda é honesta?\n\n"
       "Joguei uma moeda 100 vezes e deu 65 caras. Isso é coincidência ou a moeda é viciada?"),
    code("# Sob H0 (moeda honesta), qual a chance de obter 65 ou mais caras?\n"
         "1 - stats.binom.cdf(64, n=100, p=0.5)"),
    md("Probabilidade pequena = os dados são **incompatíveis** com a hipótese de moeda honesta."),
]

NOTEBOOKS["04_estatistica_inferencial/02_estimacao.ipynb"] = [
    md("# Estimação\n\n"
       "Usar dados da amostra para estimar parâmetros da população. "
       "Pode ser **pontual** (um número) ou **intervalar** (um intervalo)."),
    code(SETUP),
    code("df = sns.load_dataset('penguins').dropna()\n"
         "x = df['body_mass_g']"),
    md("## Estimativa pontual"),
    code("x.mean()"),
    md("## Estimativa intervalar (intervalo de confiança 95%)"),
    code("stats.t.interval(0.95, df=len(x)-1, loc=x.mean(), scale=stats.sem(x))"),
]

NOTEBOOKS["04_estatistica_inferencial/03_intervalo_confianca.ipynb"] = [
    md("# Intervalos de confiança\n\n"
       "Um intervalo de 95% significa que, se repetíssemos o experimento muitas vezes, "
       "95% dos intervalos calculados conteriam o parâmetro verdadeiro."),
    code(SETUP),
    md("## Construindo IC para a média"),
    code("df = sns.load_dataset('penguins').dropna()\n"
         "amostra = df['body_mass_g'].sample(50, random_state=0)\n"
         "ic = stats.t.interval(0.95, df=len(amostra)-1, loc=amostra.mean(), scale=stats.sem(amostra))\n"
         "ic"),
    md("## Visualizando 50 ICs"),
    code("import numpy as np\n"
         "verdadeiro = df['body_mass_g'].mean()\n"
         "fig, ax = plt.subplots(figsize=(6, 8))\n"
         "for i in range(50):\n"
         "    s = df['body_mass_g'].sample(30, random_state=i)\n"
         "    lo, hi = stats.t.interval(0.95, df=len(s)-1, loc=s.mean(), scale=stats.sem(s))\n"
         "    cor = 'tab:blue' if lo <= verdadeiro <= hi else 'tab:red'\n"
         "    ax.plot([lo, hi], [i, i], color=cor)\n"
         "ax.axvline(verdadeiro, color='black', linestyle='--');"),
    md("Os intervalos em vermelho **não** contêm o valor verdadeiro — esperamos que ~5% dos 95%-ICs falhem."),
]

NOTEBOOKS["04_estatistica_inferencial/04_hipoteses.ipynb"] = [
    md("# Hipótese nula (H₀) e alternativa (H₁)\n\n"
       "- **H₀**: 'não há diferença' / 'nada está acontecendo'\n"
       "- **H₁**: 'há diferença' / 'o efeito existe'"),
    code(SETUP),
    md("## Exemplo: novo remédio reduz pressão arterial?\n\n"
       "- H₀: a pressão média **não** muda com o remédio.\n"
       "- H₁: a pressão média muda com o remédio."),
    code("antes  = pd.Series([142, 138, 145, 150, 139, 144, 141, 147])\n"
         "depois = pd.Series([135, 130, 140, 142, 132, 138, 134, 139])\n"
         "stats.ttest_rel(antes, depois)"),
    md("`pvalue` muito pequeno → temos evidência para **rejeitar H₀** em favor de H₁."),
]

NOTEBOOKS["04_estatistica_inferencial/05_significancia.ipynb"] = [
    md("# Nível de significância (α)\n\n"
       "É o limiar que escolhemos para considerar um resultado 'estatisticamente significativo'."),
    code(SETUP),
    code("alpha = 0.05\n"
         "p = 0.03\n"
         "p < alpha  # significativo?"),
    md("## Distribuição da diferença sob H0"),
    code("import numpy as np\n"
         "x = np.linspace(-4, 4, 500)\n"
         "y = stats.norm.pdf(x)\n"
         "plt.plot(x, y)\n"
         "z_crit = stats.norm.ppf(1 - 0.025)\n"
         "plt.axvline( z_crit, color='red')\n"
         "plt.axvline(-z_crit, color='red')\n"
         "plt.fill_between(x, y, where=(x > z_crit) | (x < -z_crit), color='red', alpha=0.3);"),
]

NOTEBOOKS["04_estatistica_inferencial/06_valor_p.ipynb"] = [
    md("# Valor-p\n\n"
       "Probabilidade de obter dados **tão ou mais extremos** que os observados, supondo que H₀ seja verdadeira."),
    code(SETUP),
    md("## Exemplo: moeda joga 100 vezes, dá 60 caras"),
    code("# Teste bilateral\n"
         "stats.binomtest(60, n=100, p=0.5)"),
    md("Como o p-valor é maior que 0,05, **não rejeitamos** H₀ no nível de 5%."),
    md("## Teste t para uma amostra"),
    code("import numpy as np\n"
         "rng = np.random.default_rng(0)\n"
         "amostra = pd.Series(rng.normal(102, 15, size=30))\n"
         "stats.ttest_1samp(amostra, popmean=100)"),
]

NOTEBOOKS["04_estatistica_inferencial/07_erros_tipo_i_ii.ipynb"] = [
    md("# Erros tipo I e tipo II\n\n"
       "- **Tipo I** ($\\alpha$): rejeitar H₀ quando ela era verdadeira (falso positivo).\n"
       "- **Tipo II** ($\\beta$): não rejeitar H₀ quando ela era falsa (falso negativo)."),
    code(SETUP),
    md("## Simulando o erro tipo I\n\n"
       "Quando H₀ é verdadeira, esperamos rejeitar H₀ em ~5% dos testes (α=0.05)."),
    code("import numpy as np\n"
         "rng = np.random.default_rng(0)\n"
         "rejeicoes = 0\n"
         "for _ in range(1000):\n"
         "    a = rng.normal(100, 15, 30)\n"
         "    b = rng.normal(100, 15, 30)  # mesma média!\n"
         "    if stats.ttest_ind(a, b).pvalue < 0.05:\n"
         "        rejeicoes += 1\n"
         "rejeicoes / 1000"),
    md("## Poder estatístico (1 − β)"),
    code("from scipy.stats import norm\n"
         "n, mu0, mu1, sigma, alpha = 30, 100, 105, 15, 0.05\n"
         "se = sigma / n**0.5\n"
         "z_crit = norm.ppf(1 - alpha/2)\n"
         "poder = 1 - norm.cdf(mu0 + z_crit*se, mu1, se) + norm.cdf(mu0 - z_crit*se, mu1, se)\n"
         "poder"),
]

NOTEBOOKS["04_estatistica_inferencial/08_teste_z.ipynb"] = [
    md("# Teste z para uma amostra\n\n"
       "Quando conhecemos o desvio padrão da população."),
    code(SETUP),
    code("import numpy as np\n"
         "# Glicemia média populacional conhecida: μ=90 mg/dL, σ=12\n"
         "amostra = pd.Series(stats.norm.rvs(loc=95, scale=12, size=40, random_state=0))\n"
         "mu_0 = 90\n"
         "sigma = 12\n"
         "z = (amostra.mean() - mu_0) / (sigma / np.sqrt(len(amostra)))\n"
         "p = 2 * (1 - stats.norm.cdf(abs(z)))\n"
         "z, p"),
]

NOTEBOOKS["04_estatistica_inferencial/09_teste_t_uma_amostra.ipynb"] = [
    md("# Teste t para uma amostra\n\n"
       "Compara a média de uma amostra com um valor de referência. Usa-se quando $\\sigma$ é desconhecido."),
    code(SETUP),
    code("import numpy as np\n"
         "amostra = pd.Series(stats.norm.rvs(loc=102, scale=14, size=25, random_state=0))\n"
         "stats.ttest_1samp(amostra, popmean=100)"),
    md("## E se o p-valor for unilateral?"),
    code("stats.ttest_1samp(amostra, popmean=100, alternative='greater')"),
]

NOTEBOOKS["04_estatistica_inferencial/10_teste_t_independente.ipynb"] = [
    md("# Teste t para duas amostras independentes\n\n"
       "Compara as médias de **dois grupos diferentes**."),
    code(SETUP),
    code("df = sns.load_dataset('penguins').dropna()\n"
         "adelie  = df[df['species']=='Adelie']['body_mass_g']\n"
         "gentoo  = df[df['species']=='Gentoo']['body_mass_g']\n"
         "stats.ttest_ind(adelie, gentoo, equal_var=False)  # Welch"),
    code("sns.boxplot(data=df[df['species'].isin(['Adelie','Gentoo'])],\n"
         "            x='species', y='body_mass_g');"),
]

NOTEBOOKS["04_estatistica_inferencial/11_teste_t_pareado.ipynb"] = [
    md("# Teste t pareado\n\n"
       "Cada indivíduo é medido **duas vezes** (antes e depois, por exemplo)."),
    code(SETUP),
    code("antes  = pd.Series([142, 138, 145, 150, 139, 144, 141, 147, 152, 137])\n"
         "depois = pd.Series([135, 130, 140, 142, 132, 138, 134, 139, 144, 130])\n"
         "stats.ttest_rel(antes, depois)"),
    code("df = pd.DataFrame({'antes': antes, 'depois': depois}).melt(var_name='momento', value_name='PA')\n"
         "sns.boxplot(data=df, x='momento', y='PA');"),
]

NOTEBOOKS["04_estatistica_inferencial/12_anova.ipynb"] = [
    md("# ANOVA — análise de variância\n\n"
       "Compara as médias de **três ou mais grupos**."),
    code(SETUP),
    code("df = sns.load_dataset('penguins').dropna()\n"
         "grupos = [g['body_mass_g'].values for _, g in df.groupby('species')]\n"
         "stats.f_oneway(*grupos)"),
    code("sns.boxplot(data=df, x='species', y='body_mass_g');"),
    md("Se p < 0.05, **alguma** das médias é diferente. Para saber qual, fazemos comparações pareadas."),
]

NOTEBOOKS["04_estatistica_inferencial/13_qui_quadrado.ipynb"] = [
    md("# Teste do qui-quadrado ($\\chi^2$)\n\n"
       "Testa associação entre **variáveis categóricas**."),
    code(SETUP),
    code("df = sns.load_dataset('titanic')\n"
         "tabela = pd.crosstab(df['sex'], df['survived'])\n"
         "tabela"),
    code("chi2, p, dof, esperado = stats.chi2_contingency(tabela)\n"
         "print(f'chi² = {chi2:.2f}')\n"
         "print(f'p-valor = {p}')\n"
         "print(f'graus de liberdade = {dof}')"),
    md("## Visualizando"),
    code("sns.heatmap(tabela, annot=True, fmt='d', cmap='Blues');"),
]

NOTEBOOKS["04_estatistica_inferencial/14_correlacao.ipynb"] = [
    md("# Correlação\n\n"
       "Mede a força e direção da associação linear entre **duas variáveis numéricas**."),
    code(SETUP),
    code("df = sns.load_dataset('penguins').dropna()\n"
         "stats.pearsonr(df['flipper_length_mm'], df['body_mass_g'])"),
    code("sns.scatterplot(data=df, x='flipper_length_mm', y='body_mass_g', hue='species');"),
    md("## Matriz de correlação"),
    code("df.select_dtypes('number').corr()"),
    code("sns.heatmap(df.select_dtypes('number').corr(), annot=True, cmap='coolwarm', center=0);"),
    md("## Spearman — correlação não paramétrica"),
    code("stats.spearmanr(df['flipper_length_mm'], df['body_mass_g'])"),
]

NOTEBOOKS["04_estatistica_inferencial/15_regressao_linear.ipynb"] = [
    md("# Regressão linear simples\n\n"
       "Ajusta uma reta que prevê $y$ a partir de $x$."),
    code(SETUP),
    code("df = sns.load_dataset('penguins').dropna()\n"
         "x = df['flipper_length_mm']\n"
         "y = df['body_mass_g']\n"
         "result = stats.linregress(x, y)\n"
         "result"),
    code("print(f'reta: y = {result.intercept:.1f} + {result.slope:.1f} * x')\n"
         "print(f'R² = {result.rvalue**2:.3f}')"),
    code("sns.regplot(data=df, x='flipper_length_mm', y='body_mass_g');"),
]

NOTEBOOKS["04_estatistica_inferencial/16_testes_nao_parametricos.ipynb"] = [
    md("# Testes não paramétricos\n\n"
       "Quando os dados não são normais ou são ordinais."),
    code(SETUP),
    md("## Mann–Whitney U (substitui o t independente)"),
    code("df = sns.load_dataset('penguins').dropna()\n"
         "a = df[df['species']=='Adelie']['body_mass_g']\n"
         "g = df[df['species']=='Gentoo']['body_mass_g']\n"
         "stats.mannwhitneyu(a, g)"),
    md("## Wilcoxon (substitui o t pareado)"),
    code("antes  = pd.Series([142, 138, 145, 150, 139, 144, 141, 147])\n"
         "depois = pd.Series([135, 130, 140, 142, 132, 138, 134, 139])\n"
         "stats.wilcoxon(antes, depois)"),
    md("## Kruskal–Wallis (substitui a ANOVA)"),
    code("grupos = [g['body_mass_g'].values for _, g in df.groupby('species')]\n"
         "stats.kruskal(*grupos)"),
]


def main():
    for rel_path, cells in NOTEBOOKS.items():
        save(BASE / rel_path, notebook(cells))
        print(f"OK  {rel_path}")


if __name__ == "__main__":
    main()
