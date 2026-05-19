# Teorema do limite central (TLC)

Talvez o resultado mais importante da estatística. Em palavras:

> **A média de muitas amostras tende a uma distribuição normal**, mesmo que a população original não seja normal.

## Enunciado

Seja uma população com média $\mu$ e desvio padrão $\sigma$ (finito). Tiramos amostras de tamanho $n$ e calculamos a média $\bar{x}$ de cada uma. À medida que $n$ cresce, a distribuição de $\bar{x}$ se aproxima de uma normal:

$$
\bar{x} \sim \mathcal{N}\!\left( \mu, \; \frac{\sigma^{2}}{n} \right)
$$

Ou, em forma padronizada:

$$
Z = \frac{\bar{x} - \mu}{\sigma / \sqrt{n}} \;\to\; \mathcal{N}(0, 1)
$$

A quantidade $\sigma / \sqrt{n}$ tem nome especial: **erro padrão da média** (em inglês, *standard error of the mean*, SEM).

## Pontos-chave

1. **A média da distribuição amostral** é $\mu$ (a mesma da população).
2. **O desvio padrão da distribuição amostral** é $\sigma / \sqrt{n}$, sempre menor que $\sigma$.
3. **A forma** se aproxima da normal — independentemente da forma da população original — desde que $n$ seja "grande o bastante".

## Quão grande é "grande"?

- Se a população já é normal, o TLC vale para qualquer $n$.
- Se é moderadamente assimétrica, $n \geq 30$ costuma ser suficiente.
- Para distribuições muito enviesadas (ex.: exponencial com cauda muito longa), pode ser necessário $n \gtrsim 100$.

## Por que isso é fantástico?

Muitos testes estatísticos (t, z, ANOVA, regressão) assumem que **alguma média** segue distribuição normal. O TLC garante que, com amostras razoáveis, isso é aproximadamente verdade — **mesmo que os dados originais não sejam normais**. Por isso podemos aplicar esses testes em uma variedade enorme de situações.

## A intuição visual

Imagine jogar dois dados e somar. A soma:

- mínima: 2 (1+1);
- máxima: 12 (6+6);
- mais provável: 7 (várias combinações: 1+6, 2+5, 3+4, etc.).

Mesmo que cada dado tenha distribuição **uniforme** (cada face com 1/6 de chance), a distribuição da **soma** tem cara de sino. Com 3, 4 ou 5 dados, fica cada vez mais parecida com uma normal.

A média é apenas a soma dividida por $n$ — então o mesmo efeito acontece com qualquer média de muitas variáveis independentes.

## O que o TLC NÃO diz

- **Não** diz que a população é normal. Ela continua sendo o que era.
- **Não** ajuda quando a amostra é única — ele descreve o comportamento de **muitas amostras**.
- **Não** vale se a variância da população for infinita (algumas distribuições matemáticas extremas).

## A consequência mais importante

Quando você calcula a média de uma amostra grande de qualquer coisa razoavelmente bem comportada, sabe **automaticamente** como essa média se comporta. É isso que permite construir intervalos de confiança e testes de hipótese para a média.
