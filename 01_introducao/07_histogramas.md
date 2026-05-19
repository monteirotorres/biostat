# Histogramas

O histograma é o gráfico padrão para visualizar a distribuição de uma **variável quantitativa**.

## Como funciona

1. Dividimos o intervalo dos dados em **faixas** (em inglês, *bins*).
2. Contamos quantos valores caem em cada faixa.
3. Desenhamos uma barra com **altura proporcional** à contagem.

O resultado é uma "fotografia" da distribuição.

## O que ele revela

| Característica | O que observar |
| --- | --- |
| **Forma** | simétrica, assimétrica, multimodal? |
| **Centro** | onde está a "massa" dos dados? |
| **Dispersão** | as barras se espalham por uma faixa larga ou estreita? |
| **Outliers** | barras isoladas longe do resto? |

## Formas comuns

- **Simétrica em forma de sino** → distribuição normal.
- **Assimétrica à direita** (cauda longa para valores altos) → renda, tempo de espera, contagens.
- **Assimétrica à esquerda** (cauda para valores baixos) → notas em provas fáceis, idade ao morrer.
- **Bimodal** (duas cumes) → mistura de duas populações.

## Quantas barras usar?

| Poucas barras | Muitas barras |
| --- | --- |
| Perde detalhe | Vira ruído |

Algumas regras de bolso:

- **Raiz quadrada:** $k = \lceil \sqrt{n} \rceil$;
- **Sturges:** $k = \lceil 1 + \log_2 n \rceil$;
- **Freedman–Diaconis:** ajusta para dados com outliers.

Mas o melhor é experimentar alguns valores e escolher o que **revela a estrutura** sem mostrar ruído.

## Histograma vs. gráfico de barras

| Histograma | Gráfico de barras |
| --- | --- |
| Variável **contínua** | Variável **categórica** |
| Barras encostadas | Barras separadas |
| Eixo x = números | Eixo x = categorias |

## Histograma de densidade

Quando o eixo y mostra **densidade** (em vez de contagem), a área total sob o histograma vale 1. Isso permite comparar amostras de tamanhos diferentes na mesma escala.

$$
\text{densidade} = \frac{\text{contagem}}{n \cdot \text{largura da faixa}}
$$
