# Estatística descritiva

Exercícios sobre média, mediana e a escolha das medidas adequadas.

## Exercício 1 — Quando usar cada medida

Diante de um conjunto grande de dados, quando convém apresentar média, mediana, desvio padrão e desvio interquartil?

<details markdown="1">
<summary>Mostrar resposta</summary>

Não existe uma regra única, porque a melhor escolha depende da forma da distribuição e da pergunta de interesse.

Quando os dados são aproximadamente simétricos, próximos de uma distribuição normal, a média e o desvio padrão bastam, já que a média coincide com a mediana e o desvio padrão é a medida natural de variabilidade nesse caso.

Quando a distribuição é assimétrica, a média e a mediana passam a carregar informações diferentes e complementares. No caso da renda, por exemplo, a mediana descreve o rendimento típico e revela a concentração, enquanto a média reflete o total de recursos disponíveis. Para descrever a variabilidade nesses casos, os quantis ou o desvio interquartil são mais informativos que o desvio padrão. Já para tempo de sobrevivência a média costuma não fazer sentido, e o par mediana com quantis é o mais adequado.

</details>

## Exercício 2 — Salários

Numa empresa de dez mil empregados, mil ganham 2 salários mínimos, três mil ganham 3 e os seis mil restantes ganham 4. Calcule a média e a mediana.

<details markdown="1">
<summary>Mostrar resposta</summary>

Para a mediana, basta ordenar os trabalhadores por salário e localizar o ponto central. Os mil primeiros ganham 2, os três mil seguintes ganham 3 e a partir daí todos ganham 4. O valor central, na posição cinco mil, já está na faixa dos que ganham 4 salários, então a mediana é 4.

Para a média, somamos o que cada grupo recebe e dividimos pelo total:

$$
\bar{x} = \frac{1000 \times 2 + 3000 \times 3 + 6000 \times 4}{10000} = \frac{35000}{10000} = 3{,}5 \text{ SM}
$$

A média ficou abaixo da mediana porque o grupo de salários baixos a puxa para baixo. É um exemplo concreto de como as duas medidas contam histórias diferentes.

</details>

## Exercício 3 — Salário mediano por faixas

A distribuição de pessoas ocupadas por faixa de renda no Brasil (PNAD) foi: menos de 1 salário mínimo, 24,1%; de 1 a 1,5, 20,6%; de 1,5 a 3, 28,5%; de 3 a 5, 11,7%; de 5 a 10, 8,5%; e 10 ou mais, 6,6%. Em que faixa está o salário mediano?

<details markdown="1">
<summary>Mostrar resposta</summary>

A mediana está na faixa que contém a posição de 50% acumulados. Somando as frequências de baixo para cima:

$$
24{,}1\% \;\to\; 24{,}1 + 20{,}6 = 44{,}7\% \;\to\; 44{,}7 + 28{,}5 = 73{,}2\%
$$

O acumulado cruza os 50% justamente ao incluir a terceira faixa. Portanto, o salário mediano cai na faixa de 1,5 a 3 salários mínimos. Note que metade dos trabalhadores ganhava, à época, menos do que essa faixa, um retrato bem diferente do que uma média sozinha sugeriria.

</details>
