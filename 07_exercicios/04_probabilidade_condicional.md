# Probabilidade condicional

Exercícios sobre o teorema de Bayes e a interpretação de testes diagnósticos.

## Exercício 1 — Rastreio de doença rara

Pretende-se rastrear uma população para uma doença cuja incidência é de 0,01%. O teste detecta a doença em 99% dos doentes e identifica corretamente a ausência da doença em 95% dos saudáveis. Uma pessoa testou positivo. Qual a probabilidade de ela realmente ter a doença?

<details markdown="1">
<summary>Mostrar resposta</summary>

A pergunta inverte a direção do teste: conhecemos a probabilidade de positivo dado doente, mas queremos a probabilidade de doente dado positivo. O teorema de Bayes faz essa inversão.

No numerador entra a fração de pessoas que são doentes e testam positivo, igual a 0,0001 × 0,99. No denominador entra a probabilidade total de testar positivo, somando os verdadeiros positivos com os falsos positivos: 0,0001 × 0,99 + 0,9999 × 0,05. O resultado é aproximadamente 0,002, ou seja, cerca de 0,2%.

Apesar de o teste parecer muito bom, a doença é tão rara que a grande maioria dos positivos vem de pessoas saudáveis. Ainda assim, o teste foi útil: a probabilidade saltou de 0,01% para 0,2%, um fator de vinte. Esse é o motivo de rastreios em massa de doenças raras gerarem tantos falsos positivos.

</details>

## Exercício 2 — Previsão do tempo

Um meteorologista acerta 80% dos dias em que chove e 90% dos dias de bom tempo. Chove em 10% dos dias. Se a previsão for de chuva, qual a probabilidade de realmente chover?

<details markdown="1">
<summary>Mostrar resposta</summary>

O problema é idêntico ao do teste diagnóstico, tratando a chuva como a "doença" e a previsão como o resultado do teste. A sensibilidade é 0,8, a especificidade é 0,9 e a prevalência é 0,1.

Aplicando Bayes, o numerador é 0,1 × 0,8 e o denominador soma verdadeiros positivos e falsos positivos, 0,1 × 0,8 + 0,9 × 0,1. O resultado é 8/17, aproximadamente 47%.

Uma forma intuitiva de ver isso é montar uma tabela com mil dias. Cem chovem e novecentos não. Dos cem dias de chuva, oitenta são previstos corretamente. Dos novecentos de bom tempo, noventa recebem previsão errada de chuva. No total há 170 previsões de chuva, das quais oitenta acertam, e 80/170 dá os mesmos 47%.

</details>

## Exercício 3 — AVC e pressão alta

Sabe-se que 10% dos idosos sofrerão um AVC nos próximos cinco anos. Entre os que tiveram AVC, 40% apresentavam pressão arterial elevada. Entre os que não tiveram AVC, 20% tinham pressão elevada aos 70 anos. Qual a probabilidade de um idoso com pressão alta vir a sofrer um AVC?

<details markdown="1">
<summary>Mostrar resposta</summary>

Identificando o AVC como a "doença" e a pressão elevada como o "teste", a prevalência é 10%, a sensibilidade é 40% e a especificidade é 80%, já que 20% dos que não tiveram AVC tinham um indicador falso.

Montando uma tabela com cem idosos, dez terão AVC e noventa não. Dos dez com AVC, quatro têm pressão elevada. Dos noventa sem AVC, dezoito têm pressão elevada. Entre todos os que têm pressão alta, portanto, há 22 pessoas, das quais quatro sofrerão AVC. A probabilidade procurada é 4/22, aproximadamente 18%.

A mesma lógica serve para estimar o efeito de qualquer fator de risco, como fumo e câncer, e pode ser estendida para combinar mais de um fator.

</details>
