# Qui-quadrado

Exercícios sobre aderência a um modelo e comparação de frequências.

## Exercício 1 — Dado honesto

Um dado lançado sessenta vezes apresentou as frequências 8, 11, 7, 12, 15 e 7. O dado é honesto? E se multiplicarmos todas as frequências por dez, mantendo a mesma tendência?

<details markdown="1">
<summary>Mostrar resposta</summary>

Para um dado honesto, a frequência esperada de cada face em sessenta lançamentos é dez. O qui-quadrado soma, para cada face, o quadrado da diferença entre observado e esperado dividido pelo esperado. O resultado é cerca de 5,2, com cinco graus de liberdade, o que corresponde a um valor-p de aproximadamente 0,39. Não há evidência para rejeitar a hipótese de dado honesto.

Multiplicando todas as frequências por dez, as proporções não mudam, mas o número absoluto de lançamentos vira seiscentos, com esperado de cem por face. Agora o qui-quadrado vira 52, dez vezes maior, com valor-p da ordem de 10⁻¹⁰. A conclusão se inverte: o dado é considerado viciado. A lição é que o teste depende do número absoluto de observações, não apenas das proporções; com mais dados, desvios da mesma magnitude relativa tornam-se estatisticamente convincentes.

</details>

## Exercício 2 — Mendel 9:3:3:1

Mendel observou os fenótipos 315, 108, 101 e 32, num total de 556 sementes. O modelo 9:3:3:1 explica os dados? E um modelo linear alternativo, com valores 264, 181, 97 e 14, explicaria igualmente bem?

<details markdown="1">
<summary>Mostrar resposta</summary>

Para o modelo de Mendel, os valores esperados a partir da proporção 9:3:3:1 sobre 556 são aproximadamente 312,75, 104,25, 104,25 e 34,75. Somando os quatro termos do qui-quadrado, chega-se a cerca de 0,47, com três graus de liberdade, o que dá um valor-p em torno de 0,93. Esse valor altíssimo indica um ajuste excelente: não há motivo para rejeitar a proporção mendeliana.

Para o modelo linear, com os valores esperados 264, 181, 97 e 14, o qui-quadrado salta para cerca de 62,6, com valor-p essencialmente zero. O modelo linear é rejeitado com folga. Embora os dois conjuntos de valores esperados pareçam próximos num gráfico, o teste mostra que o modelo de Mendel descreve os dados de forma incomparavelmente melhor.

</details>
