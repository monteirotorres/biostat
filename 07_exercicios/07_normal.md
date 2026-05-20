# Distribuição normal

Exercícios sobre a curva normal e o cálculo de áreas e percentis.

## Exercício 1 — A regra 68-95-99,7

Que percentual da população está compreendido em torno da média a uma distância de um, dois e três desvios padrão?

<details markdown="1">
<summary>Mostrar resposta</summary>

Em qualquer distribuição normal, independentemente da média e do desvio padrão, cerca de 68,3% dos valores ficam entre a média menos um desvio e a média mais um desvio. Ampliando para dois desvios, a cobertura sobe para 95,4%, e para três desvios chega a 99,7%.

Esses números mostram que a normal é uma distribuição concentrada: embora se estenda em teoria de menos infinito a mais infinito, quase toda a massa está próxima da média. É essa propriedade que justifica falar em "a faixa típica" de uma medida biológica.

</details>

## Exercício 2 — Variáveis só positivas

A distribuição normal se estende a valores negativos. Como podemos usá-la para variáveis que só podem ser positivas, como a altura das pessoas?

<details markdown="1">
<summary>Mostrar resposta</summary>

A primeira parte da resposta vem da regra anterior: como a distribuição é concentrada, uma altura média de 170 cm com desvio de 15 cm praticamente nunca chega a valores negativos, pois isso exigiria afastamentos de mais de onze desvios padrão.

A segunda parte, mais importante, é que a normal é um modelo da massa principal dos dados, não dos extremos. Quem estuda nanismo ou gigantismo não usa a normal da população inteira; define uma subpopulação e a estuda separadamente. A normal descreve bem o comportamento típico, e os casos raros são tratados como objetos de estudo próprios.

</details>

## Exercício 3 — Capacidade do elevador

Um elevador suporta 500 kg. Os pesos dos usuários seguem uma normal de média 70 kg e desvio 10 kg. Qual a probabilidade de sete passageiros ultrapassarem o limite? E seis?

<details markdown="1">
<summary>Mostrar resposta</summary>

Aqui entra a distribuição da soma dos pesos. A soma de sete pesos independentes tem média 7 × 70 = 490 kg e desvio padrão 10 vezes a raiz de sete, cerca de 26,5 kg. A probabilidade de a soma passar de 500 kg corresponde a um afastamento de cerca de 0,38 desvios acima da média, o que dá aproximadamente 0,35.

Para seis passageiros, a soma tem média 420 kg e desvio 10 vezes a raiz de seis, cerca de 24,5 kg. Agora 500 kg está bem acima da média, a mais de três desvios, e a probabilidade cai para cerca de 0,0005. Reduzir de sete para seis passageiros torna o estouro do limite praticamente improvável.

</details>

## Exercício 4 — Pressão arterial da população

A pressão arterial segue uma normal de média 100 mmHg e desvio 10 mmHg.

a) Que percentual da população tem pressão entre 80 e 120? b) Qual faixa em torno da média contém 95% das pessoas? c) Apenas 1% da população tem pressão acima de qual valor?

<details markdown="1">
<summary>Mostrar resposta</summary>

A faixa de 80 a 120 corresponde a dois desvios para cada lado, então pela regra 95,4% da população está nela.

Para conter exatamente 95%, usamos o valor crítico de 1,96 desvios, o que dá a média mais ou menos 19,6 mmHg, ou seja, de cerca de 80,4 a 119,6 mmHg.

Para o ponto acima do qual está apenas 1% da população, procuramos o percentil 99, que fica a cerca de 2,33 desvios acima da média. Isso dá aproximadamente 123,3 mmHg.

</details>

## Exercício 5 — Média de quatro pessoas

Com a mesma população de pressão (média 100, desvio 10), escolhemos quatro pessoas e calculamos a média.

a) Qual a probabilidade de a média estar entre 80 e 120? b) Que faixa contém 95% das médias? c) E se não soubermos o desvio da população, tendo apenas o desvio amostral de 7,8?

<details markdown="1">
<summary>Mostrar resposta</summary>

Agora trabalhamos com a distribuição da média amostral, cujo desvio é o desvio populacional dividido pela raiz de quatro, ou seja, 5 mmHg. A faixa de 80 a 120 corresponde a quatro desvios da média para cada lado, então a média quase certamente cai nela, com probabilidade próxima de 99,99%.

Para 95% das médias, usamos 1,96 desvios da média amostral, o que dá a média mais ou menos 9,8 mmHg, de cerca de 90,2 a 109,8 mmHg. Repare como essa faixa é bem mais estreita que a da população individual, porque médias variam menos que observações isoladas.

Quando o desvio populacional é desconhecido e usamos o desvio amostral de 7,8, precisamos da distribuição t com três graus de liberdade, cujo valor crítico é cerca de 3,18, maior que 1,96. A faixa fica em torno de 100 mais ou menos 12,4 mmHg, mais larga, refletindo a incerteza extra de estimar o desvio a partir de poucos dados.

</details>

## Exercício 6 — Garantia de lavadoras

A vida útil de uma lavadora segue uma normal de média 1,5 anos e desvio 0,3 anos. Que percentual falhará antes de completar um ano de garantia?

<details markdown="1">
<summary>Mostrar resposta</summary>

Um ano está a 0,5 anos abaixo da média, o que corresponde a cerca de 1,67 desvios padrão. A área da normal abaixo desse ponto é aproximadamente 0,048, ou seja, cerca de 4,8% das lavadoras falharão dentro da garantia.

Cálculos como esse são feitos rotineiramente pela indústria para dimensionar custos de garantia e definir prazos.

</details>

## Exercício 7 — Temperatura corporal

A temperatura de homens saudáveis segue uma normal de média 36,8 graus e desvio 0,15 graus.

a) Entre mil indivíduos, quantos se espera na faixa de 36,8 a 37,0? b) Em que intervalo simétrico em torno da média estão 50% dos indivíduos?

<details markdown="1">
<summary>Mostrar resposta</summary>

A faixa de 36,8 a 37,0 vai da média até cerca de 1,33 desvios acima dela. A área entre a média e esse ponto é aproximadamente 0,409, então de mil indivíduos espera-se em torno de 409 nessa faixa.

Para conter 50% em torno da média, dividimos os 50% em 25% de cada lado, o que corresponde a cerca de 0,674 desvios para cada direção. Isso dá um intervalo de aproximadamente 36,7 a 36,9 graus.

</details>
