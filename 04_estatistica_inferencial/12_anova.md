# ANOVA — análise de variância

A ANOVA compara as médias de **três ou mais grupos** simultaneamente.

## Por que não fazer vários testes t?

Imagine comparar 4 grupos dois a dois: são 6 comparações. Se cada uma tem $\alpha = 0{,}05$, a chance de **pelo menos um falso positivo** vira:

$$
1 - (1 - 0{,}05)^{6} \approx 26\%
$$

Quase 1 em cada 4 análises geraria uma "diferença" espúria. A ANOVA resolve isso fazendo **um único teste global**.

## A ideia central

A ANOVA decompõe a variabilidade total em duas partes:

- **Variabilidade entre grupos**: as médias dos grupos diferem?
- **Variabilidade dentro de grupos**: quanto cada grupo varia internamente?

Se a variabilidade **entre** grupos for muito maior que a variabilidade **dentro**, é evidência de que as médias são diferentes.

## A estatística F

$$
F = \frac{\text{variância entre grupos}}{\text{variância dentro dos grupos}} = \frac{\text{MS}_{\text{entre}}}{\text{MS}_{\text{dentro}}}
$$

Sob H₀ (todas as médias iguais), $F$ segue a **distribuição F** com graus de liberdade $(k-1, n-k)$, onde $k$ é o número de grupos e $n$ o total de observações.

## Hipóteses

$$
H_0: \mu_1 = \mu_2 = \cdots = \mu_k
$$

$$
H_1: \text{pelo menos uma média é diferente}
$$

Atenção: H₁ não diz **qual** é a diferente — só que existe alguma. Isso requer testes posteriores.

## Suposições

| Suposição | Verificação |
| --- | --- |
| Independência das observações | Desenho do estudo |
| Normalidade dentro de cada grupo | Histograma, Q-Q plot, Shapiro–Wilk |
| Variâncias iguais (homocedasticidade) | Teste de Levene, Bartlett |

> ANOVA é razoavelmente robusta a desvios moderados da normalidade, especialmente com grupos balanceados.

## Exemplo

Comparando 3 dietas em ratos quanto ao ganho de peso (g/semana):

| Dieta | $n$ | $\bar{x}$ | $s$ |
| --- | --- | --- | --- |
| A | 10 | 15 | 2,1 |
| B | 10 | 18 | 2,3 |
| C | 10 | 22 | 2,0 |

ANOVA retornaria $F \approx 25$, $p < 0{,}001$. Rejeitamos H₀: as dietas têm efeitos diferentes.

## Tabela ANOVA típica

| Fonte | SS | gl | MS | F | p |
| --- | --- | --- | --- | --- | --- |
| Entre grupos | 264 | 2 | 132 | 25 | < 0,001 |
| Dentro de grupos | 130 | 27 | 4,8 | | |
| Total | 394 | 29 | | | |

Onde SS = soma de quadrados, MS = SS/gl, $F$ = MS entre / MS dentro.

## E depois? Comparações múltiplas

Se a ANOVA rejeita H₀, sabemos que **alguma média** é diferente, mas não qual. Para identificar, usamos comparações *post hoc*:

| Método | Quando usar |
| --- | --- |
| **Tukey HSD** | Comparações dois a dois, com correção embutida |
| **Bonferroni** | Mais conservador, simples de aplicar |
| **Dunnett** | Comparar grupos com um controle |
| **Scheffé** | Para combinações lineares de médias |

A ideia é controlar o **erro tipo I familiar** (chance de pelo menos um falso positivo entre todas as comparações).

## ANOVA de um fator vs. múltiplos fatores

- **ANOVA one-way**: 1 fator (ex.: tipo de dieta).
- **ANOVA two-way**: 2 fatores (ex.: dieta + sexo).
- **ANOVA multifatorial**: vários fatores, com possíveis **interações**.

A ANOVA two-way permite ver se um fator depende do nível do outro (interação).

## Alternativa não paramétrica

Quando as suposições não se sustentam, usa-se o **teste de Kruskal–Wallis**, que generaliza Mann–Whitney para $k$ grupos.

## Resumo

| Cenário | Teste |
| --- | --- |
| 2 grupos independentes | teste t |
| 3+ grupos independentes | ANOVA |
| 3+ grupos pareados (medidas repetidas) | ANOVA de medidas repetidas |
| Dados não normais | Kruskal–Wallis |
