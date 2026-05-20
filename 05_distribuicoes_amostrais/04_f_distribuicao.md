# A distribuição F

A distribuição **F** (em homenagem a Ronald Fisher) é a base da **ANOVA** e de qualquer teste que compare **variâncias**.

## Como ela surge

A F é a **razão entre duas variâncias** — mais precisamente, a razão entre duas qui-quadrado, cada uma dividida por seus graus de liberdade:

$$
F = \frac{\chi^2_{d_1} / d_1}{\chi^2_{d_2} / d_2}
$$

Como variâncias são sempre positivas, a F só assume valores **positivos**. Ela tem **dois** parâmetros de graus de liberdade: $d_1$ (numerador) e $d_2$ (denominador).

## A intuição: comparar variabilidades

Pense em duas fontes de variação:

- variância **entre** grupos (o quanto as médias dos grupos diferem);
- variância **dentro** dos grupos (a variabilidade natural dentro de cada grupo).

A estatística F é a razão entre as duas:

$$
F = \frac{\text{variância entre grupos}}{\text{variância dentro dos grupos}}
$$

- Se os grupos têm médias **iguais** ($H_0$), as duas variâncias estimam a mesma coisa, e $F \approx 1$.
- Se as médias **diferem**, a variância entre grupos infla, e $F$ fica **grande**.

Por isso a ANOVA é um teste **unilateral à direita**: só valores grandes de F são evidência contra $H_0$.

## Forma

| Situação | Forma |
| --- | --- |
| $d_1$ pequeno | muito assimétrica à direita |
| $d_1, d_2$ grandes | concentra-se em torno de 1 |

O valor esperado de F (para $d_2 > 2$) é próximo de 1, refletindo a ideia de "duas estimativas da mesma variância".

## Relações com as outras distribuições

A F amarra tudo o que vimos:

- O **quadrado** de uma variável t com $k$ gl é uma F com $(1, k)$ gl: $t_k^2 = F_{1,k}$.
- A F é uma **razão de qui-quadrados**.
- Para $d_1 = 1$, a ANOVA de dois grupos equivale ao teste t.

Ou seja, normal → qui-quadrado → t e F formam uma **família coerente**, todas nascidas da amostragem de variáveis normais.

## Onde você vai usá-la

- **ANOVA** (comparação de 3+ médias).
- **Teste F de igualdade de variâncias** (usado, por exemplo, para decidir entre teste t de Student e de Welch).
- **Significância global de modelos de regressão**.

## No notebook

Construímos a F por simulação: sorteamos duas amostras normais, calculamos a razão de suas variâncias (ajustadas pelos graus de liberdade) e acumulamos. O histograma coincide com `scipy.stats.f`. Também verificamos numericamente que $t_k^2 = F_{1,k}$.
