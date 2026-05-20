# Qui-quadrado

Exercícios sobre aderência a um modelo e comparação de frequências.

## Exercício 1 — Dado honesto

Um dado lançado sessenta vezes apresentou as frequências 8, 11, 7, 12, 15 e 7. O dado é honesto? E se multiplicarmos todas as frequências por dez, mantendo a mesma tendência?

<details markdown="1">
<summary>Mostrar resposta</summary>

Para um dado honesto, a frequência esperada de cada face em sessenta lançamentos é $E = 60/6 = 10$. O qui-quadrado soma, para cada face, o quadrado da diferença entre observado e esperado dividido pelo esperado:

$$
\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i} = \frac{(8-10)^2 + (11-10)^2 + \cdots + (7-10)^2}{10} = 5{,}2
$$

Com cinco graus de liberdade, isso corresponde a um valor-p de aproximadamente 0,39. Não há evidência para rejeitar a hipótese de dado honesto.

Multiplicando todas as frequências por dez, as proporções não mudam, mas o esperado vira cem por face e cada termo fica dez vezes maior:

$$
\chi^2 = \frac{(80-100)^2 + \cdots + (70-100)^2}{100} = 52
$$

com valor-p da ordem de $10^{-10}$. A conclusão se inverte: o dado é considerado viciado. O teste depende do número absoluto de observações, não apenas das proporções; com mais dados, desvios da mesma magnitude relativa tornam-se estatisticamente convincentes.

</details>

## Exercício 2 — Mendel 9:3:3:1

Mendel observou os fenótipos 315, 108, 101 e 32, num total de 556 sementes. O modelo 9:3:3:1 explica os dados? E um modelo linear alternativo, com valores 264, 181, 97 e 14, explicaria igualmente bem?

<details markdown="1">
<summary>Mostrar resposta</summary>

Para o modelo de Mendel, os valores esperados a partir da proporção 9:3:3:1 sobre 556 são $556 \times \tfrac{9}{16} = 312{,}75$, depois 104,25, 104,25 e 34,75. Somando os quatro termos:

$$
\chi^2 = \frac{(315 - 312{,}75)^2}{312{,}75} + \cdots + \frac{(32 - 34{,}75)^2}{34{,}75} \approx 0{,}47
$$

Com três graus de liberdade, o valor-p fica em torno de 0,93. Esse valor altíssimo indica um ajuste excelente: não há motivo para rejeitar a proporção mendeliana.

Para o modelo linear, com os valores esperados 264, 181, 97 e 14, o qui-quadrado salta para cerca de 62,6, com valor-p essencialmente zero. O modelo linear é rejeitado com folga. Embora os dois conjuntos de valores esperados pareçam próximos num gráfico, o teste mostra que o modelo de Mendel descreve os dados de forma incomparavelmente melhor.

</details>
