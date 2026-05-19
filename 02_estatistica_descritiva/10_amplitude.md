# Amplitude

A medida de dispersão mais simples: a diferença entre o maior e o menor valor.

## Definição

$$
A = x_{\max} - x_{\min}
$$

## Exemplo

Notas: $4, 5, 6, 7, 8, 9, 10$.

$$
A = 10 - 4 = 6
$$

## Quando usar

A amplitude é útil para:

- **Comunicação rápida**: dá uma ideia imediata do intervalo dos dados.
- **Controle de qualidade** simples: serve para detectar quando algo sai do esperado.
- **Decisões iniciais** sobre escala de gráficos.

## Limitações

| Problema | Por quê |
| --- | --- |
| Usa **apenas dois valores** | descarta toda a informação intermediária |
| **Muito sensível a outliers** | um valor extremo faz a amplitude explodir |
| **Cresce com o tamanho da amostra** | quanto mais dados, maior a chance de encontrar valores extremos |

Por exemplo:

| Dados | Amplitude |
| --- | --- |
| $\{10, 12, 14, 16, 18\}$ | 8 |
| $\{10, 12, 14, 16, 500\}$ | 490 |

Apenas um valor extremo mudou tudo.

## Alternativa robusta: o IQR

O **intervalo interquartil** (IQR) é uma versão robusta da amplitude:

$$
\text{IQR} = Q_3 - Q_1
$$

Ele descreve a amplitude dos **50% centrais** dos dados, ignorando os 25% mais altos e os 25% mais baixos. É muito menos afetado por outliers.

## Quando reportar

Em artigos científicos, a amplitude raramente é a única medida reportada — mas costuma aparecer **junto com** outras medidas, escrita como `mínimo–máximo`:

> "Idade dos participantes: 32 ± 8 anos (intervalo: 18–62)."

Esse formato dá uma noção rápida dos extremos sem comprometer-se com eles como medida de dispersão.
