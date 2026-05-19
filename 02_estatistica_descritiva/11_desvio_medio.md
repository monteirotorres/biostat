# Desvio médio

Mede a **distância média** de cada valor até a média do conjunto.

## A motivação

Já vimos que a soma dos desvios $(x_i - \bar{x})$ sempre dá zero — os positivos cancelam os negativos. Para evitar esse cancelamento, podemos usar o **valor absoluto** das diferenças.

## Fórmula

$$
\text{DM} = \frac{1}{n} \sum_{i=1}^{n} \left| x_i - \bar{x} \right|
$$

Em palavras: para cada valor, calcule a distância (sem sinal) até a média; depois tire a média dessas distâncias.

## Exemplo

Dados: $2, 4, 4, 4, 5, 5, 7, 9$. Média $\bar{x} = 5$.

| $x_i$ | $|x_i - \bar{x}|$ |
| --- | --- |
| 2 | 3 |
| 4 | 1 |
| 4 | 1 |
| 4 | 1 |
| 5 | 0 |
| 5 | 0 |
| 7 | 2 |
| 9 | 4 |

Soma das distâncias = 12. Desvio médio = $12 / 8 = 1{,}5$.

## Interpretação

> Em média, cada valor está a 1,5 unidade de distância da média.

## Por que o desvio médio é pouco usado?

Apesar de intuitivo, o desvio médio quase não aparece em estatística clássica. A razão é matemática: a função valor absoluto tem um **bico** em zero e é mais difícil de manipular (não tem derivada nesse ponto). Por isso, o padrão é elevar ao quadrado em vez de tirar o módulo — chegando à **variância** e ao **desvio padrão**, que veremos a seguir.

## Em estatística robusta

Existe uma versão robusta chamada **MAD** (*median absolute deviation*):

$$
\text{MAD} = \text{mediana}\,(\,|\,x_i - \tilde{x}\,|\,)
$$

Onde $\tilde{x}$ é a mediana. É bem mais resistente a outliers que o desvio médio comum e aparece em métodos modernos como *robust statistics* e detecção de anomalias.
