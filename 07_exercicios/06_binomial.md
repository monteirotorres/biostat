# Distribuição binomial

Exercícios sobre contagem de sucessos em ensaios independentes.

## Exercício 1 — Falsos positivos acumulados

Testando dois grupos controle entre si com nível de confiança de 95%, há 5% de chance de obter um falso positivo. Qual a probabilidade de pelo menos um falso positivo se repetirmos o experimento várias vezes?

<details markdown="1">
<summary>Mostrar resposta</summary>

A maneira mais simples de responder a perguntas do tipo "pelo menos um" é calcular a probabilidade do evento contrário, que é nenhum falso positivo, e subtrair de 1. Se cada teste tem 95% de chance de não dar falso positivo, então a probabilidade de nenhum em k repetições é 0,95 elevado a k.

Para três repetições, a chance de ao menos um falso positivo é 1 − 0,95³, cerca de 14%. Para dez repetições sobe para 40%, e para cinquenta passa de 92%. Esse crescimento explica dois problemas reais: comparar três ou mais grupos par a par com testes t infla o nível de significância efetivo, o que motivou a criação da ANOVA, e testar centenas de substâncias produz inevitavelmente muitos falsos positivos, que precisam de análises posteriores para serem filtrados.

</details>

## Exercício 2 — Pôquer

Você joga pôquer com três amigos de habilidade parecida, aposta de valor fixo e obrigatória, sem empates. Qual a probabilidade de não perder dinheiro em dez partidas?

<details markdown="1">
<summary>Mostrar resposta</summary>

Com quatro jogadores de igual habilidade, a probabilidade de vencer cada partida é 1/4. Em dez partidas, o número de vitórias segue uma distribuição binomial com n igual a 10 e p igual a 1/4.

Não perder dinheiro significa terminar com saldo maior ou igual a zero, o que exige vencer ao menos três das dez partidas. A probabilidade é 1 menos a probabilidade de vencer zero, uma ou duas vezes, o que dá aproximadamente 0,474. Em outras palavras, há pouco menos de 50% de chance de sair no zero a zero ou no lucro ao fim de dez rodadas.

</details>

## Exercício 3 — Mudas e fungos

Cada muda pode ser atacada por fungo com probabilidade 0,06, sendo descartada nesse caso. O custo de produção é R$ 1,20 por muda e a venda é R$ 3,50. Considere lotes de cinquenta mudas.

a) Qual o lucro previsto por lote? b) Qual a probabilidade de um lote não ter nenhuma contaminação? c) Qual a probabilidade de menos de dez mudas contaminadas?

<details markdown="1">
<summary>Mostrar resposta</summary>

Para o lucro previsto, espera-se que 94% das cinquenta mudas sobrevivam, ou seja, cerca de 47 mudas vendidas a R$ 3,50, gerando uma receita em torno de R$ 164. Descontando o custo de produção das cinquenta mudas, 50 × 1,20 = R$ 60, o lucro previsto fica em torno de R$ 104 por lote.

A probabilidade de nenhuma contaminação é a de todas as cinquenta sobreviverem, 0,94 elevado a 50, aproximadamente 0,045. A probabilidade de menos de dez contaminadas é a soma das probabilidades de zero a nove contaminações numa binomial com n igual a 50 e p igual a 0,06, que dá aproximadamente 0,999. Como o número esperado de contaminadas é apenas três, ter dez ou mais é bastante raro.

</details>

## Exercício 4 — Prova de múltipla escolha

Numa prova com cinco alternativas por questão e apenas uma correta, qual a probabilidade de ser aprovado (nota maior ou igual a 5) apenas no chute, com a) dez questões; b) vinte questões?

<details markdown="1">
<summary>Mostrar resposta</summary>

Cada acerto no chute tem probabilidade 1/5. Com dez questões, o número de acertos segue uma binomial com p igual a 0,2, e a aprovação exige cinco ou mais acertos. A probabilidade é cerca de 0,033, ou seja, pouco mais de 3%.

Com vinte questões, a nota mínima sobe para dez acertos numa binomial com p igual a 0,25, e a probabilidade despenca para cerca de 0,0026. Provas mais longas reduzem drasticamente a chance de aprovação pela sorte, porque a distribuição se concentra cada vez mais em torno do número esperado de acertos, que é baixo. Para dez questões, aliás, a nota mais provável obtida no chute é 2.

</details>

## Exercício 5 — Controle de qualidade

Uma máquina produz peças com 0,5% de defeito. Retira-se uma amostra de dez peças e a máquina é desligada para revisão se houver mais de uma defeituosa. Qual a probabilidade de desligá-la mesmo estando dentro do padrão?

<details markdown="1">
<summary>Mostrar resposta</summary>

A pergunta é a probabilidade de encontrar duas ou mais peças defeituosas numa amostra de dez, quando a taxa real é 0,5%. Isso é 1 menos a probabilidade de zero defeituosas menos a probabilidade de exatamente uma, numa binomial com n igual a 10 e p igual a 0,005.

O resultado é aproximadamente 0,0011, ou seja, pouco mais de um décimo de por cento. Esse valor é o risco de um alarme falso da política de manutenção: parar a máquina à toa por causa da variação amostral, mesmo quando a produção está dentro da especificação.

</details>

## Exercício 6 — Genética mendeliana

No cruzamento de plantas heterozigotas, espera-se a proporção 3:1 entre os fenótipos amarelo e verde. Coletando cem sementes, qual a probabilidade de encontrar oitenta ou mais amarelas?

<details markdown="1">
<summary>Mostrar resposta</summary>

A proporção esperada de amarelas é 3/4, então o número de sementes amarelas em cem segue uma binomial com p igual a 0,75. O número esperado é setenta e cinco, e queremos a probabilidade de obter oitenta ou mais.

Somando as probabilidades de oitenta até cem, chega-se a aproximadamente 0,149, ou cerca de 15%. Embora oitenta esteja acima do valor esperado, ainda é um desvio plausível pela variação amostral, e por isso a probabilidade não é desprezível.

</details>
