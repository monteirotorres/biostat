# Média aritmética

A medida de tendência central mais conhecida. Soma todos os valores e divide pelo número deles.

## Fórmula

Para uma **amostra** com $n$ valores:

$$
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i = \frac{x_1 + x_2 + \cdots + x_n}{n}
$$

Para uma **população** com $N$ valores:

$$
\mu = \frac{1}{N} \sum_{i=1}^{N} x_i
$$

A fórmula é a mesma — muda apenas o símbolo, dependendo se estamos falando de amostra ($\bar{x}$, "x-barra") ou de população ($\mu$, "mi").

## Exemplo

Cinco notas de uma prova: $6{,}0; 7{,}5; 8{,}0; 5{,}5; 9{,}0$.

$$
\bar{x} = \frac{6{,}0 + 7{,}5 + 8{,}0 + 5{,}5 + 9{,}0}{5} = \frac{36{,}0}{5} = 7{,}2
$$

## Propriedades importantes

1. **Usa todos os valores** — diferente da mediana, que usa só o do meio.
2. **Sensível a outliers** — um único valor extremo pode puxar a média muito.
3. **A soma dos desvios em relação à média é zero**:

$$
\sum_{i=1}^{n} (x_i - \bar{x}) = 0
$$

Isso significa que a média é o **"ponto de equilíbrio"** dos dados — se colocássemos cada valor como um pesinho numa régua, a régua se equilibraria sobre a média.

## Quando usar

A média é apropriada quando:

- a distribuição é **aproximadamente simétrica**;
- não há outliers extremos;
- os dados são **quantitativos** (não categóricos).

## Quando NÃO usar

- Em distribuições **muito assimétricas** (renda, tempo de sobrevida) — a mediana é mais informativa.
- Em variáveis **ordinais** — a média entre "leve", "moderada" e "intensa" não significa nada.
- Em variáveis **nominais** — não dá nem para calcular.

## Atenção ao jargão

Quando alguém diz "a média", geralmente está se referindo à média aritmética. Mas existem outras médias (geométrica, harmônica, cortada, ponderada) que você verá nos próximos tópicos.
