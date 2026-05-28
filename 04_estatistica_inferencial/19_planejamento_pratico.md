# Planejamento prático: pós-testes e ANOVA fatorial

Este notebook aplica os conceitos de planejamento experimental de forma prática, com código Python comentado e gráficos gerados com matplotlib e seaborn.

## O que o notebook cobre

| Seção | Conteúdo |
| --- | --- |
| Cálculo amostral | Fórmula para teste t; curva poder × n |
| Poder por simulação Monte Carlo | Verificação empírica do poder teórico |
| ANOVA one-way + pós-testes | Tukey HSD, Dunnett, Bonferroni |
| Kruskal-Wallis + Dunn | Alternativa não-paramétrica com correção de Bonferroni |
| ANOVA fatorial 2 × 2 | Efeitos principais, interação, visualização |

## Pré-requisitos

```python
pip install scipy statsmodels scikit-posthocs seaborn
```

## Como usar

Abra o notebook no Google Colab (botão acima) ou execute localmente com Jupyter. Todas as células podem ser rodadas na ordem — cada seção é independente.

> Os dados são simulados com `numpy.random` para reprodutibilidade; altere a semente (`rng = np.random.default_rng(42)`) para gerar novos cenários.
