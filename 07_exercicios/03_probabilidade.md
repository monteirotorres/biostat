# Probabilidade

Exercícios clássicos de cálculo de probabilidades.

## Exercício 1 — O problema de Chevalier de Méré

O que é mais provável: obter ao menos um seis em quatro lançamentos de um dado, ou obter ao menos um par de seis em vinte e quatro lançamentos de dois dados? O cavalheiro Chevalier de Méré argumentava que as duas situações eram equivalentes, porque o número médio de ocorrências seria 2/3 em ambos os casos.

<details markdown="1">
<summary>Mostrar resposta</summary>

As duas probabilidades não são iguais, e o raciocínio de Méré confunde número esperado com probabilidade. Em ambos os casos calculamos a probabilidade do evento contrário e subtraímos de 1.

$$
P(\text{ao menos um 6 em 4}) = 1 - \left(\frac{5}{6}\right)^{4} = 1 - 0{,}482 = 0{,}518
$$

$$
P(\text{ao menos um duplo-6 em 24}) = 1 - \left(\frac{35}{36}\right)^{24} = 1 - 0{,}509 = 0{,}491
$$

O primeiro evento é um pouco mais provável que não acontecer; o segundo, um pouco menos. A coincidência do valor 2/3 que Méré calculou corresponde ao número médio de ocorrências ($4 \times \tfrac16 = 24 \times \tfrac{1}{36} = \tfrac23$), uma quantidade diferente da probabilidade de pelo menos uma ocorrência. Esse problema histórico foi um dos que motivaram o desenvolvimento formal da teoria da probabilidade.

</details>

## Exercício 2 — Megasena

Qual a probabilidade de ganhar na Megasena com o jogo mínimo de seis números marcados entre sessenta?

<details markdown="1">
<summary>Mostrar resposta</summary>

O número total de resultados possíveis é a combinação de sessenta números tomados seis a seis:

$$
\binom{60}{6} = \frac{60!}{6!\,(60-6)!} = 50\,063\,860
$$

Como só um desses resultados é o vencedor,

$$
P = \frac{1}{50\,063\,860} \approx 2{,}0 \times 10^{-8} \approx 0{,}000002\%
$$

Há um segundo modo de chegar ao mesmo resultado, encadeando eventos:

$$
P = \frac{6}{60}\cdot\frac{5}{59}\cdot\frac{4}{58}\cdot\frac{3}{57}\cdot\frac{2}{56}\cdot\frac{1}{55}
$$

que dá exatamente o mesmo valor, mostrando que a contagem por combinação e o raciocínio sequencial são equivalentes.

</details>

## Exercício 3 — O cientista consciencioso

Um pesquisador só publica um resultado depois de confirmá-lo ao menos uma vez, usando nível de significância de 5%.

a) Qual a probabilidade de uma publicação ser um falso positivo se a repetição for totalmente independente?

b) Como a independência completa é irreal (mesmos reagentes, mesmo protocolo, mesmo experimentador), suponha que a probabilidade de um segundo falso positivo dado o primeiro seja 30%. Qual a probabilidade de publicar um falso positivo nesse caso?

<details markdown="1">
<summary>Mostrar resposta</summary>

Se os dois experimentos fossem independentes, a probabilidade de ambos darem falso positivo seria o produto das probabilidades:

$$
P(\text{FP e FP}) = 0{,}05 \times 0{,}05 = 0{,}0025 = 0{,}25\%
$$

Na prática, porém, os experimentos compartilham reagentes, equipamentos e métodos, então um erro tende a se repetir. Usando a regra da multiplicação com a probabilidade condicional de 30% para o segundo falso positivo,

$$
P(\text{FP e FP}) = P(\text{FP}) \cdot P(\text{FP} \mid \text{FP}) = 0{,}05 \times 0{,}30 = 0{,}015 = 1{,}5\%
$$

A dependência entre as repetições enfraquece a proteção que a confirmação deveria oferecer, e por isso replicações verdadeiramente independentes, em outro laboratório, são tão valorizadas.

</details>
