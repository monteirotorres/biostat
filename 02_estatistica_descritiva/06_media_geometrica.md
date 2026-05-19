# Média geométrica

A média geométrica é a "média natural" para dados **multiplicativos**: taxas de crescimento, fatores de diluição, títulos de anticorpos.

## Fórmula

Para $n$ valores positivos:

$$
\bar{x}_g = \sqrt[n]{x_1 \cdot x_2 \cdots x_n} = \left( \prod_{i=1}^{n} x_i \right)^{1/n}
$$

Equivalentemente, em termos de logaritmos (forma muito usada nas implementações):

$$
\bar{x}_g = \exp\!\left( \frac{1}{n} \sum_{i=1}^{n} \ln x_i \right)
$$

Em palavras: **calculamos a média aritmética dos logaritmos** e depois aplicamos a função inversa.

## Quando faz sentido?

Sempre que os dados crescem (ou diminuem) **multiplicativamente**, e não somando uma quantidade fixa.

### Exemplo 1 — taxa de crescimento bacteriano

Uma cultura cresce a taxas (vezes/h) de: 1,5; 2,0; 1,8; 2,2; 1,9.

Se quisermos saber a taxa "típica" de crescimento, queremos o número que, repetido, daria o mesmo crescimento acumulado. Esse número é a média **geométrica**, não a aritmética.

$$
\bar{x}_g = \sqrt[5]{1{,}5 \cdot 2{,}0 \cdot 1{,}8 \cdot 2{,}2 \cdot 1{,}9} \approx 1{,}87
$$

### Exemplo 2 — diluições em série

Em imunologia, títulos de anticorpos são comumente $1/40, 1/80, 1/160, \ldots$ — uma série geométrica. A média geométrica respeita essa escala.

### Exemplo 3 — retorno de investimentos

Se um ativo rende +10% num ano e -10% no outro, a média aritmética dos retornos é 0% (que seria voltar ao mesmo valor). Mas isso é falso: $1{,}10 \cdot 0{,}90 = 0{,}99$. O retorno médio **real** é dado pela média geométrica.

## Comparação com a aritmética

Para qualquer conjunto de valores positivos:

$$
\bar{x}_g \leq \bar{x}
$$

A igualdade só ocorre quando todos os valores são iguais. Quanto mais variados os dados, maior a diferença entre as duas médias.

## Restrições

- **Só funciona para valores positivos** (não definida para 0 ou negativos).
- Pouca interpretabilidade em escalas aditivas (a média geométrica de alturas em cm é estranha).

## Como reconhecer um caso de média geométrica

Pergunte: **"Se eu repetir esse valor $n$ vezes, multiplicando, recupero o produto original?"** Se sim, é caso de média geométrica.

> Em escala log, a média geométrica vira simplesmente a média aritmética dos logaritmos. Por isso, é comum **transformar dados** com $\log$ antes de aplicar testes estatísticos quando a distribuição é multiplicativa.
