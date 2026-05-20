# A distribuição t de Student

A distribuição **t** é talvez a mais usada em bioestatística — está por trás do teste t e dos intervalos de confiança para a média.

## O problema que ela resolve

Pelo Teorema do Limite Central, sabemos que a média amostral padronizada é normal:

$$
Z = \frac{\bar{x} - \mu}{\sigma / \sqrt{n}} \sim \mathcal{N}(0,1)
$$

Mas há um problema prático: **quase nunca conhecemos $\sigma$** (o desvio padrão da população). Então o substituímos por $s$ (o desvio padrão da amostra):

$$
t = \frac{\bar{x} - \mu}{s / \sqrt{n}}
$$

Acontece que $s$ é apenas uma **estimativa** de $\sigma$ — ela própria varia de amostra para amostra. Essa incerteza extra faz com que $t$ **não** seja normal: ele segue a **distribuição t de Student** com $n-1$ graus de liberdade.

## Como ela surge formalmente

A distribuição t nasce da razão entre uma normal padrão e a raiz de uma qui-quadrado (dividida por seus graus de liberdade):

$$
t_k = \frac{Z}{\sqrt{\chi^2_k / k}}
$$

Ou seja: ela combina a variabilidade da **média** (numerador normal) com a variabilidade da **variância estimada** (denominador qui-quadrado). Por isso é mais "espalhada" que a normal.

## Forma: caudas pesadas

A distribuição t parece uma normal, mas com **caudas mais pesadas**:

| Graus de liberdade | Comportamento |
| --- | --- |
| $k = 1$ | caudas muito pesadas (distribuição de Cauchy) |
| $k = 5$ | ainda visivelmente mais pesada que a normal |
| $k = 30$ | quase idêntica à normal |
| $k \to \infty$ | converge para a normal padrão |

As caudas pesadas significam que **valores extremos são mais prováveis** com a t do que com a normal. Isso é exatamente o que queremos: com amostras pequenas, há mais incerteza, então o teste precisa ser mais "cauteloso" (exige evidência mais forte para rejeitar $H_0$).

## Consequência prática

É por isso que os valores críticos do teste t são **maiores** que os da normal para amostras pequenas:

| Confiança | $z^*$ (normal) | $t^*$ ($n=5$) | $t^*$ ($n=30$) |
| --- | --- | --- | --- |
| 95% | 1,96 | 2,78 | 2,05 |

Com $n$ pequeno, precisamos ir mais longe na cauda para "fechar" 95% — refletindo nossa maior ignorância sobre $\sigma$.

## Onde você vai usá-la

- **Teste t** de uma amostra, duas amostras e pareado.
- **Intervalos de confiança** para a média (quando $\sigma$ é desconhecido).
- **Testes de significância dos coeficientes** em regressão.

## A história curiosa

A distribuição foi publicada em 1908 por William Sealy Gosset, que trabalhava na cervejaria Guinness. A empresa proibia funcionários de publicar, então ele usou o pseudônimo **"Student"** — daí o nome.

## No notebook

Construímos a t por simulação: a cada iteração, sorteamos uma pequena amostra normal, calculamos $t = (\bar{x}-\mu)/(s/\sqrt{n})$ e acumulamos. O histograma resultante tem caudas mais pesadas que a normal — exatamente a curva do `scipy.stats.t`.
