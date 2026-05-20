# Distribuição binomial

Exercícios sobre contagem de sucessos em ensaios independentes.

## Exercício 1 — Falsos positivos acumulados

Testando dois grupos controle entre si com nível de confiança de 95%, há 5% de chance de obter um falso positivo. Qual a probabilidade de pelo menos um falso positivo se repetirmos o experimento várias vezes?

<details markdown="1">
<summary>Mostrar resposta</summary>

A maneira mais simples de responder a perguntas do tipo "pelo menos um" é calcular a probabilidade do evento contrário, nenhum falso positivo, e subtrair de 1:

$$
P(\text{ao menos um FP}) = 1 - (0{,}95)^{k}
$$

$$
k=3:\; 1 - 0{,}95^{3} = 0{,}143 \qquad k=10:\; 0{,}401 \qquad k=50:\; 0{,}923
$$

Esse crescimento explica dois problemas reais: comparar três ou mais grupos par a par com testes t infla o nível de significância efetivo, o que motivou a criação da ANOVA, e testar centenas de substâncias produz inevitavelmente muitos falsos positivos, que precisam de análises posteriores para serem filtrados.

</details>

## Exercício 2 — Pôquer

Você joga pôquer com três amigos de habilidade parecida, aposta de valor fixo e obrigatória, sem empates. Qual a probabilidade de não perder dinheiro em dez partidas?

<details markdown="1">
<summary>Mostrar resposta</summary>

Com quatro jogadores de igual habilidade, a probabilidade de vencer cada partida é $p = 1/4$. Em dez partidas, o número de vitórias segue uma binomial com $n = 10$. Não perder dinheiro exige vencer ao menos três das dez partidas, usando a fórmula binomial $P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}$:

$$
P(X \ge 3) = 1 - \big[P(0) + P(1) + P(2)\big] = 1 - (0{,}0563 + 0{,}1877 + 0{,}2816) \approx 0{,}474
$$

Há pouco menos de 50% de chance de sair no zero a zero ou no lucro ao fim de dez rodadas.

</details>

## Exercício 3 — Mudas e fungos

Cada muda pode ser atacada por fungo com probabilidade 0,06, sendo descartada nesse caso. O custo de produção é R$ 1,20 por muda e a venda é R$ 3,50. Considere lotes de cinquenta mudas.

a) Qual o lucro previsto por lote? b) Qual a probabilidade de um lote não ter nenhuma contaminação? c) Qual a probabilidade de menos de dez mudas contaminadas?

<details markdown="1">
<summary>Mostrar resposta</summary>

Para o lucro previsto, espera-se que 94% das cinquenta mudas sobrevivam:

$$
\text{lucro} = (50 \times 0{,}94 \times 3{,}50) - (50 \times 1{,}20) = 164{,}5 - 60 = 104{,}5 \text{ reais}
$$

A probabilidade de nenhuma contaminação é a de todas as cinquenta sobreviverem:

$$
P(0) = (0{,}94)^{50} \approx 0{,}045
$$

A probabilidade de menos de dez contaminadas é a soma de zero a nove numa binomial com $n=50$ e $p=0{,}06$:

$$
P(X \le 9) = \sum_{k=0}^{9}\binom{50}{k}(0{,}06)^k(0{,}94)^{50-k} \approx 0{,}999
$$

Como o número esperado de contaminadas é $np = 50 \times 0{,}06 = 3$, ter dez ou mais é bastante raro.

</details>

## Exercício 4 — Prova de múltipla escolha

Numa prova com cinco alternativas por questão e apenas uma correta, qual a probabilidade de ser aprovado (nota maior ou igual a 5) apenas no chute, com a) dez questões; b) vinte questões?

<details markdown="1">
<summary>Mostrar resposta</summary>

Cada acerto no chute tem probabilidade 1/5. Com dez questões ($p = 0{,}2$), a aprovação exige cinco ou mais acertos:

$$
P(X \ge 5) = 1 - P(X \le 4) \approx 0{,}033
$$

Com vinte questões a nota mínima sobe para dez acertos ($p = 0{,}25$):

$$
P(X \ge 10) = 1 - P(X \le 9) \approx 0{,}0026
$$

Provas mais longas reduzem drasticamente a chance de aprovação pela sorte, porque a distribuição se concentra em torno do número esperado de acertos, que é baixo ($np = 2$ no primeiro caso). A nota mais provável no chute, para dez questões, é 2.

</details>

## Exercício 5 — Controle de qualidade

Uma máquina produz peças com 0,5% de defeito. Retira-se uma amostra de dez peças e a máquina é desligada para revisão se houver mais de uma defeituosa. Qual a probabilidade de desligá-la mesmo estando dentro do padrão?

<details markdown="1">
<summary>Mostrar resposta</summary>

A pergunta é a probabilidade de duas ou mais peças defeituosas numa amostra de dez, com taxa real $p = 0{,}005$:

$$
P(X \ge 2) = 1 - P(0) - P(1) = 1 - (0{,}995)^{10} - 10(0{,}005)(0{,}995)^{9} \approx 0{,}0011
$$

Esse valor, pouco mais de um décimo de por cento, é o risco de um alarme falso da política de manutenção: parar a máquina à toa por causa da variação amostral, mesmo dentro da especificação.

</details>

## Exercício 6 — Genética mendeliana

No cruzamento de plantas heterozigotas, espera-se a proporção 3:1 entre os fenótipos amarelo e verde. Coletando cem sementes, qual a probabilidade de encontrar oitenta ou mais amarelas?

<details markdown="1">
<summary>Mostrar resposta</summary>

A proporção esperada de amarelas é 3/4, então o número de amarelas em cem segue uma binomial com $p = 0{,}75$. O número esperado é $np = 75$, com desvio $\sqrt{np(1-p)} = \sqrt{100 \cdot 0{,}75 \cdot 0{,}25} \approx 4{,}33$. Queremos oitenta ou mais:

$$
P(X \ge 80) = \sum_{k=80}^{100}\binom{100}{k}(0{,}75)^k(0{,}25)^{100-k} \approx 0{,}149
$$

Oitenta está a pouco mais de um desvio acima do esperado, um afastamento plausível, e por isso a probabilidade não é desprezível.

</details>
