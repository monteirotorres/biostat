# A distribuição qui-quadrado (χ²)

A distribuição **qui-quadrado** é a primeira das três distribuições derivadas da normal — e a base para entender as outras.

## Como ela surge

Pegue uma variável **normal padrão** $Z \sim \mathcal{N}(0,1)$ e eleve ao quadrado. Some $k$ dessas variáveis ao quadrado, todas independentes:

$$
\chi^2_k = Z_1^2 + Z_2^2 + \cdots + Z_k^2
$$

O resultado segue uma distribuição **qui-quadrado com $k$ graus de liberdade**.

> Em palavras: a qui-quadrado é a distribuição de uma **soma de quadrados** de variáveis normais. Como são quadrados, ela só assume valores **positivos**.

## Forma

| Graus de liberdade | Forma |
| --- | --- |
| $k = 1$ | muito assimétrica, concentrada perto de zero |
| $k = 3$ | assimétrica à direita |
| $k$ grande | quase simétrica, aproxima-se da normal |

A média de uma $\chi^2_k$ é exatamente $k$, e a variância é $2k$.

## Por que aparece na variância amostral

Quando estimamos a variância de uma amostra normal, a quantidade

$$
\frac{(n-1)\,s^2}{\sigma^2}
$$

segue uma distribuição $\chi^2$ com $n-1$ graus de liberdade. É por isso que a qui-quadrado é a distribuição natural para tudo que envolve **variabilidade** (somas de desvios ao quadrado).

## Onde você vai usá-la

1. **Teste qui-quadrado de aderência e independência** (tabelas de contingência): comparamos contagens observadas e esperadas, e a soma

$$
\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}
$$

segue aproximadamente uma distribuição qui-quadrado.

2. **Intervalos de confiança para a variância**.

3. Como **bloco de construção** das distribuições t e F (próximos tópicos).

## Interpretação intuitiva

A qui-quadrado mede **"distância acumulada ao quadrado"**. Valores grandes significam que os dados observados estão **longe** do esperado — exatamente o que queremos detectar em um teste de aderência. Por isso o teste qui-quadrado é sempre **unilateral à direita**: só nos interessa o quanto a discrepância é grande.

## No notebook

No notebook que acompanha esta seção, construímos a qui-quadrado **do zero**: sorteamos variáveis normais, elevamos ao quadrado, somamos, e vemos o histograma coincidir com a curva teórica do `scipy.stats.chi2`.
