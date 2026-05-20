# Probabilidade

Exercícios clássicos de cálculo de probabilidades.

## Exercício 1 — O problema de Chevalier de Méré

O que é mais provável: obter ao menos um seis em quatro lançamentos de um dado, ou obter ao menos um par de seis em vinte e quatro lançamentos de dois dados? O cavalheiro Chevalier de Méré argumentava que as duas situações eram equivalentes, porque o número médio de ocorrências seria 2/3 em ambos os casos.

<details markdown="1">
<summary>Mostrar resposta</summary>

As duas probabilidades não são iguais, e o raciocínio de Méré confunde número esperado com probabilidade.

No primeiro caso, a probabilidade de não sair nenhum seis em quatro lançamentos é (5/6) elevado a 4. A probabilidade de sair ao menos um seis é o complemento, aproximadamente 0,518. No segundo caso, a probabilidade de não sair nenhum par de seis em vinte e quatro lançamentos é (35/36) elevado a 24, e o complemento é aproximadamente 0,491.

Ou seja, o primeiro evento é um pouco mais provável que não acontecer, enquanto o segundo é um pouco menos. A coincidência do valor 2/3 que Méré calculou corresponde ao número médio de ocorrências, uma quantidade diferente da probabilidade de pelo menos uma ocorrência. Esse problema histórico foi um dos que motivaram o desenvolvimento formal da teoria da probabilidade.

</details>

## Exercício 2 — Megasena

Qual a probabilidade de ganhar na Megasena com o jogo mínimo de seis números marcados entre sessenta?

<details markdown="1">
<summary>Mostrar resposta</summary>

O número total de resultados possíveis é a combinação de sessenta números tomados seis a seis, que vale 50.063.860. Como só um desses resultados é o vencedor, a probabilidade é 1 dividido por esse total, aproximadamente 2×10⁻⁸, ou seja, cerca de 0,000002%.

Há um segundo modo de chegar ao mesmo resultado, encadeando eventos. Você tem seis chances de acertar uma das seis posições numa cartela de sessenta, depois cinco chances entre os cinquenta e nove números restantes, e assim por diante até a última. Multiplicando essas frações chega-se exatamente ao mesmo valor, o que mostra que a contagem por combinação e o raciocínio sequencial são equivalentes.

</details>

## Exercício 3 — O cientista consciencioso

Um pesquisador só publica um resultado depois de confirmá-lo ao menos uma vez, usando nível de significância de 5%.

a) Qual a probabilidade de uma publicação ser um falso positivo se a repetição for totalmente independente?

b) Como a independência completa é irreal (mesmos reagentes, mesmo protocolo, mesmo experimentador), suponha que a probabilidade de um segundo falso positivo dado o primeiro seja 30%. Qual a probabilidade de publicar um falso positivo nesse caso?

<details markdown="1">
<summary>Mostrar resposta</summary>

Se os dois experimentos fossem independentes, a probabilidade de ambos darem falso positivo seria o produto 0,05 × 0,05 = 0,0025, ou seja, 0,25%. Exigir uma confirmação reduz bastante a chance de publicar algo espúrio.

Na prática, porém, os experimentos compartilham reagentes, equipamentos e métodos, então um erro tende a se repetir. Com a probabilidade condicional de 30% para o segundo falso positivo, a chance de publicar um falso positivo passa a ser 0,05 × 0,30 = 0,015, ou 1,5%. A dependência entre as repetições enfraquece a proteção que a confirmação deveria oferecer, e por isso replicações verdadeiramente independentes, em outro laboratório, são tão valorizadas.

</details>
