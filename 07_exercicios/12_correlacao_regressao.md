# Correlação e regressão

Exercícios sobre associação entre variáveis e ajuste de retas.

## Exercício 1 — Peso e altura

A partir de uma pequena tabela de altura e peso, com pares como (152, 38) até (193, 68), calcule o coeficiente de correlação, o R², a reta de melhor ajuste e critique o uso da regressão.

<details markdown="1">
<summary>Mostrar resposta</summary>

O coeficiente de correlação de Pearson fica em torno de 0,77, uma associação positiva forte: pessoas mais altas tendem a pesar mais. O R² é o quadrado desse valor:

$$
R^2 = (0{,}767)^2 \approx 0{,}59
$$

ou seja, aproximadamente 59% da variação do peso pode ser atribuída à variação da altura no modelo linear. A reta de melhor ajuste, obtida por mínimos quadrados, é

$$
\hat{y} = 0{,}89\,x - 91
$$

o peso previsto aumenta cerca de 0,89 kg para cada centímetro de altura. O intercepto negativo é apenas uma extrapolação matemática, sem sentido biológico.

A crítica é que, embora seja plausível que mais altura cause mais peso, muitos outros fatores influenciam o peso, e os 41% de variação não explicada são grandes. A reta serve bem para descrever a tendência geral, mas não para prever o peso de um indivíduo com confiança.

</details>

## Exercício 2 — Experimento contra estudo de correlação

Qual a diferença entre um experimento verdadeiro e um estudo de correlação?

<details markdown="1">
<summary>Mostrar resposta</summary>

Num experimento verdadeiro, o pesquisador manipula a variável independente e mantém todas as demais sob controle. Com esse controle, é possível afirmar que a manipulação de uma variável causa a alteração da outra, estabelecendo uma relação de causa e efeito.

Num estudo de correlação, nada é controlado. Coletam-se os valores de duas ou mais variáveis numa mesma amostra e observa-se como elas variam juntas. Estudos de correlação são úteis para revelar associações e gerar hipóteses, mas não provam causalidade, porque sempre pode haver uma terceira variável por trás da associação. Depois de levantar uma hipótese a partir de uma correlação, o passo seguinte é planejar um experimento verdadeiro para testá-la.

</details>

## Exercício 3 — As quatro explicações de uma correlação

Se o coeficiente de correlação entre duas variáveis é diferente de zero, quais explicações são possíveis?

<details markdown="1">
<summary>Mostrar resposta</summary>

Existem quatro possibilidades. A primeira é que mudanças em X causem mudanças em Y. A segunda é o inverso, que mudanças em Y causem mudanças em X. A terceira é que uma ou mais variáveis externas alterem X e Y ao mesmo tempo, criando uma associação sem relação direta entre elas. A quarta é que X e Y não tenham qualquer ligação e a correlação observada tenha surgido por acaso, situação cuja frequência é justamente medida pelo valor-p.

A consequência prática é que uma correlação, por mais forte que seja, nunca prova causalidade sozinha. Coleções de correlações absurdas mas estatisticamente fortes, como consumo de certos produtos contra eventos sem nenhuma relação, ilustram bem o ponto.

</details>
