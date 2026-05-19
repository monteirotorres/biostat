# Curva normal

A **curva normal** (também chamada **gaussiana** ou **curva em sino**) é a distribuição mais importante da estatística. Várias medidas biológicas seguem (ou se aproximam) dessa forma.

## Forma e equação

A curva normal é definida por dois parâmetros: a média $\mu$ e o desvio padrão $\sigma$. A função de densidade é:

$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}} \cdot e^{-\frac{1}{2} \left( \frac{x - \mu}{\sigma} \right)^{2}}
$$

Não precisa decorar essa fórmula. O que importa é entender:

- $\mu$ define **onde está o centro** da curva;
- $\sigma$ define **quão larga** ela é.

## Propriedades importantes

1. **Simétrica** em torno da média.
2. **Média = mediana = moda** (no centro).
3. A área total sob a curva é **1** (ou 100%).
4. Tem caudas que se estendem para $-\infty$ e $+\infty$, mas a densidade fica muito pequena longe do centro.

## A regra 68-95-99,7

A propriedade mais útil da normal:

| Intervalo | Porcentagem dos valores |
| --- | --- |
| $\mu \pm 1\sigma$ | ~68% |
| $\mu \pm 2\sigma$ | ~95% |
| $\mu \pm 3\sigma$ | ~99,7% |

> Exemplo: se a altura segue $\mathcal{N}(170, 8)$, então cerca de 95% das pessoas medem entre 154 e 186 cm.

## A normal padrão (Z)

Quando $\mu = 0$ e $\sigma = 1$, chamamos a distribuição de **normal padrão** e representamos a variável por $Z$.

Qualquer normal pode ser convertida para Z pela **padronização**:

$$
Z = \frac{X - \mu}{\sigma}
$$

Isso é útil porque permite comparar valores que vieram de distribuições normais diferentes — todos passam a estar na mesma escala.

## Por que ela aparece tanto?

Pelo **Teorema do Limite Central**: quando uma medida resulta da soma de muitos pequenos efeitos independentes, a distribuição resultante tende à normal. A altura, por exemplo, é influenciada por genética, alimentação, sono, doenças na infância — cada um contribuindo um pouco. O resultado se aproxima de uma normal.

## Cuidado!

Nem tudo é normal. Antes de assumir normalidade, **olhe o histograma** ou faça um teste formal. Distribuições assimétricas (renda, tempo de sobrevida, contagens raras) precisam de outra abordagem.
