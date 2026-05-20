# Probabilidade e intuição

Exercícios que exploram como a intuição costuma falhar diante de probabilidades.

## Exercício 1 — Reformular "ganhar na Megasena"

Qual das reformulações abaixo é realmente equivalente à definição de "ganhar na Megasena"? (a) acertar os seis números sorteados; (b) ganhar o prêmio da Megasena; (c) ficar rico com a Megasena; (d) acertar os seis números e ter o prêmio depositado na conta; (e) nenhuma das anteriores.

<details markdown="1">
<summary>Mostrar resposta</summary>

A resposta é (e). Cada tentativa de reformular muda sutilmente o significado. Acertar os seis números não basta se você perde o bilhete. Ganhar o prêmio pode acontecer com outra pessoa que depois te doa o valor, e ninguém diria que foi você quem ganhou. Ficar rico também funciona se o cônjuge ganha. E ter o dinheiro na conta exclui quem acertou mas morreu antes do depósito.

A lição vale para toda a teoria de probabilidade: definir um evento com precisão é difícil, e refrasear quase sempre introduz erros. Quando o enunciado já traz uma definição, o mais seguro é trabalhar com ela, em vez de substituí-la por uma versão "equivalente".

</details>

## Exercício 2 — Problema do aniversário

Numa sala com quarenta pessoas reunidas ao acaso, qual a probabilidade de pelo menos duas fazerem aniversário no mesmo dia? Estime entre muito pequena, pequena, em torno de 50%, grande ou muito grande.

<details markdown="1">
<summary>Mostrar resposta</summary>

A probabilidade é muito grande, em torno de 89%. O resultado surpreende porque a intuição compara cada pessoa com uma data fixa, quando na verdade comparamos todos os pares possíveis de pessoas.

O caminho mais simples é calcular a probabilidade do evento contrário, que é todas as datas serem diferentes:

$$
P(\text{todas diferentes}) = \frac{365}{365}\cdot\frac{364}{365}\cdot\frac{363}{365}\cdots\frac{326}{365} = \frac{365!}{(365-40)!\;365^{40}} \approx 0{,}109
$$

$$
P(\text{ao menos duas iguais}) = 1 - 0{,}109 \approx 0{,}891
$$

Com apenas 23 pessoas a probabilidade já passa de 50%.

</details>

## Exercício 3 — O andar do bêbado

Geramos passos aleatórios de +1 ou −1 e os somamos um após o outro, formando uma caminhada aleatória. Depois de muitos passos, o que se pode dizer sobre a posição final? (Há uma simulação no notebook.)

<details markdown="1">
<summary>Mostrar resposta</summary>

Em média, a posição final é zero, porque os passos para frente e para trás se cancelam na média de muitas repetições. Isso não significa, porém, que o bêbado fique parado: a dispersão da posição cresce com o número de passos.

Cada passo $X_i$ vale $+1$ ou $-1$ com variância 1. Como os passos são independentes, as variâncias se somam, e o desvio padrão da posição após $n$ passos é

$$
\text{DP}(S_n) = \sqrt{\operatorname{Var}(X_1) + \cdots + \operatorname{Var}(X_n)} = \sqrt{n}
$$

Após cem passos, o afastamento típico é $\sqrt{100} = 10$ unidades, não cem. Essa relação com a raiz quadrada é a mesma que aparece no erro padrão da média.

</details>
