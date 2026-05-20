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

Aqui entra a distribuição da soma dos pesos. Para sete passageiros independentes:

$$
\mu = 7 \times 70 = 490 \text{ kg} \qquad \sigma = 10\sqrt{7} \approx 26{,}5 \text{ kg}
$$

$$
z = \frac{500 - 490}{26{,}5} \approx 0{,}38 \quad\Rightarrow\quad P(\text{soma} > 500) = 1 - \Phi(0{,}38) \approx 0{,}35
$$

Para seis passageiros, $\mu = 420$ e $\sigma = 10\sqrt{6} \approx 24{,}5$:

$$
z = \frac{500 - 420}{24{,}5} \approx 3{,}27 \quad\Rightarrow\quad P \approx 0{,}0005
$$

Reduzir de sete para seis passageiros torna o estouro do limite praticamente improvável.

</details>

## Exercício 4 — Pressão arterial da população

A pressão arterial segue uma normal de média 100 mmHg e desvio 10 mmHg.

a) Que percentual da população tem pressão entre 80 e 120? b) Qual faixa em torno da média contém 95% das pessoas? c) Apenas 1% da população tem pressão acima de qual valor?

<details markdown="1">
<summary>Mostrar resposta</summary>

A faixa de 80 a 120 corresponde a $z = (120-100)/10 = 2$ para cada lado, então pela regra 95,4% da população está nela.

Para conter exatamente 95%, usamos o valor crítico de 1,96 desvios:

$$
100 \pm 1{,}96 \times 10 = 100 \pm 19{,}6 \;\Rightarrow\; [80{,}4;\; 119{,}6] \text{ mmHg}
$$

Para o ponto acima do qual está apenas 1% da população, usamos o percentil 99 ($z = 2{,}33$):

$$
100 + 2{,}33 \times 10 \approx 123{,}3 \text{ mmHg}
$$

</details>

## Exercício 5 — Média de quatro pessoas

Com a mesma população de pressão (média 100, desvio 10), escolhemos quatro pessoas e calculamos a média.

a) Qual a probabilidade de a média estar entre 80 e 120? b) Que faixa contém 95% das médias? c) E se não soubermos o desvio da população, tendo apenas o desvio amostral de 7,8?

<details markdown="1">
<summary>Mostrar resposta</summary>

Agora trabalhamos com a distribuição da média amostral, cujo desvio (erro padrão) é

$$
\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} = \frac{10}{\sqrt{4}} = 5 \text{ mmHg}
$$

A faixa de 80 a 120 corresponde a $z = (120-100)/5 = 4$ desvios para cada lado, então a média quase certamente cai nela (probabilidade próxima de 99,99%).

Para 95% das médias, usamos 1,96 erros padrão:

$$
100 \pm 1{,}96 \times 5 = 100 \pm 9{,}8 \;\Rightarrow\; [90{,}2;\; 109{,}8] \text{ mmHg}
$$

Essa faixa é bem mais estreita que a da população individual, porque médias variam menos que observações isoladas. Quando o desvio populacional é desconhecido e usamos $s = 7{,}8$, recorremos à distribuição t com três graus de liberdade ($t^* = 3{,}18$):

$$
100 \pm 3{,}18 \times \frac{7{,}8}{\sqrt{4}} = 100 \pm 12{,}4 \text{ mmHg}
$$

A faixa fica mais larga, refletindo a incerteza extra de estimar o desvio a partir de poucos dados.

</details>

## Exercício 6 — Garantia de lavadoras

A vida útil de uma lavadora segue uma normal de média 1,5 anos e desvio 0,3 anos. Que percentual falhará antes de completar um ano de garantia?

<details markdown="1">
<summary>Mostrar resposta</summary>

Um ano está abaixo da média:

$$
z = \frac{1 - 1{,}5}{0{,}3} \approx -1{,}67 \quad\Rightarrow\quad P(T < 1) = \Phi(-1{,}67) \approx 0{,}048
$$

Cerca de 4,8% das lavadoras falharão dentro da garantia. Cálculos como esse são feitos rotineiramente pela indústria para dimensionar custos de garantia e definir prazos.

</details>

## Exercício 7 — Temperatura corporal

A temperatura de homens saudáveis segue uma normal de média 36,8 graus e desvio 0,15 graus.

a) Entre mil indivíduos, quantos se espera na faixa de 36,8 a 37,0? b) Em que intervalo simétrico em torno da média estão 50% dos indivíduos?

<details markdown="1">
<summary>Mostrar resposta</summary>

A faixa de 36,8 a 37,0 vai da média até $z = (37{,}0 - 36{,}8)/0{,}15 \approx 1{,}33$ acima dela:

$$
P(36{,}8 < T < 37{,}0) = \Phi(1{,}33) - 0{,}5 \approx 0{,}409 \;\Rightarrow\; 1000 \times 0{,}409 \approx 409 \text{ indivíduos}
$$

Para conter 50% em torno da média, dividimos em 25% de cada lado ($z = 0{,}674$):

$$
36{,}8 \pm 0{,}674 \times 0{,}15 \;\Rightarrow\; [36{,}70;\; 36{,}90] \text{ graus}
$$

</details>

