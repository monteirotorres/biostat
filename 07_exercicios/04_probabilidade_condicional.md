# Probabilidade condicional

Exercícios sobre o teorema de Bayes e a interpretação de testes diagnósticos.

## Exercício 1 — Rastreio de doença rara

Pretende-se rastrear uma população para uma doença cuja incidência é de 0,01%. O teste detecta a doença em 99% dos doentes e identifica corretamente a ausência da doença em 95% dos saudáveis. Uma pessoa testou positivo. Qual a probabilidade de ela realmente ter a doença?

<details markdown="1">
<summary>Mostrar resposta</summary>

A pergunta inverte a direção do teste: conhecemos a probabilidade de positivo dado doente, mas queremos a probabilidade de doente dado positivo. O teorema de Bayes faz essa inversão:

$$
P(D \mid +) = \frac{P(+ \mid D)\,P(D)}{P(+ \mid D)\,P(D) + P(+ \mid S)\,P(S)}
$$

Substituindo a prevalência $P(D) = 0{,}0001$, a sensibilidade $P(+\mid D) = 0{,}99$ e o falso positivo $P(+\mid S) = 1 - 0{,}95 = 0{,}05$:

$$
P(D \mid +) = \frac{0{,}0001 \times 0{,}99}{0{,}0001 \times 0{,}99 + 0{,}9999 \times 0{,}05} \approx 0{,}00198 \approx 0{,}2\%
$$

Apesar de o teste parecer muito bom, a doença é tão rara que a grande maioria dos positivos vem de pessoas saudáveis. Ainda assim, o teste foi útil: a probabilidade saltou de 0,01% para 0,2%, um fator de vinte. Esse é o motivo de rastreios em massa de doenças raras gerarem tantos falsos positivos.

</details>

## Exercício 2 — Previsão do tempo

Um meteorologista acerta 80% dos dias em que chove e 90% dos dias de bom tempo. Chove em 10% dos dias. Se a previsão for de chuva, qual a probabilidade de realmente chover?

<details markdown="1">
<summary>Mostrar resposta</summary>

O problema é idêntico ao do teste diagnóstico, tratando a chuva como a "doença" e a previsão como o resultado do teste. A sensibilidade é 0,8, a especificidade é 0,9 e a prevalência é 0,1. Por Bayes:

$$
P(\text{chuva} \mid +) = \frac{0{,}1 \times 0{,}8}{0{,}1 \times 0{,}8 + 0{,}9 \times 0{,}1} = \frac{0{,}08}{0{,}17} = \frac{8}{17} \approx 0{,}471
$$

Uma forma intuitiva de chegar ao mesmo resultado é montar uma tabela com mil dias. Cem chovem e novecentos não. Dos cem dias de chuva, $100 \times 0{,}8 = 80$ são previstos corretamente. Dos novecentos de bom tempo, $900 \times 0{,}1 = 90$ recebem previsão errada de chuva. No total há $80 + 90 = 170$ previsões de chuva, das quais 80 acertam: $80/170 \approx 47\%$.

</details>

## Exercício 3 — AVC e pressão alta

Sabe-se que 10% dos idosos sofrerão um AVC nos próximos cinco anos. Entre os que tiveram AVC, 40% apresentavam pressão arterial elevada. Entre os que não tiveram AVC, 20% tinham pressão elevada aos 70 anos. Qual a probabilidade de um idoso com pressão alta vir a sofrer um AVC?

<details markdown="1">
<summary>Mostrar resposta</summary>

Identificando o AVC como a "doença" e a pressão elevada como o "teste", a prevalência é 10%, a sensibilidade é 40% e a especificidade é 80%, já que 20% dos que não tiveram AVC tinham um indicador falso.

Montando uma tabela com cem idosos:

$$
\text{com AVC e PA alta} = 100 \times 0{,}10 \times 0{,}40 = 4
$$

$$
\text{sem AVC e PA alta} = 100 \times 0{,}90 \times 0{,}20 = 18
$$

Entre todos os que têm pressão alta há $4 + 18 = 22$ pessoas, das quais 4 sofrerão AVC:

$$
P(\text{AVC} \mid \text{PA alta}) = \frac{4}{22} \approx 0{,}182
$$

A mesma lógica serve para estimar o efeito de qualquer fator de risco, como fumo e câncer, e pode ser estendida para combinar mais de um fator.

</details>
