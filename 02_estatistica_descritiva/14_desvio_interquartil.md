# Desvio interquartil (IQR)

Mede a dispersão dos **50% centrais** dos dados, ignorando os 25% mais altos e os 25% mais baixos. É a alternativa robusta ao desvio padrão.

## Definição

$$
\text{IQR} = Q_3 - Q_1
$$

Onde:

- $Q_1$ é o **primeiro quartil** (percentil 25);
- $Q_3$ é o **terceiro quartil** (percentil 75).

## Quartis

Os quartis dividem os dados ordenados em **quatro partes iguais**:

```
| 25% | 25% | 25% | 25% |
^     ^     ^     ^     ^
min   Q1    Q2    Q3   max
            (mediana)
```

## Exemplo

Dados ordenados: $4, 6, 7, 8, 10, 12, 14, 18, 20, 25$.

- $Q_1$ (entre o 2º e o 3º valor): $\approx 6{,}75$.
- $Q_2 = 11$ (mediana).
- $Q_3 \approx 17$.
- $\text{IQR} = 17 - 6{,}75 = 10{,}25$.

> Existem várias convenções para calcular quartis em amostras pequenas — diferentes pacotes podem dar valores ligeiramente diferentes. Em amostras grandes, todas convergem.

## Boxplot — IQR visualizado

O **boxplot** é o gráfico construído em torno do IQR:

| Elemento | Significado |
| --- | --- |
| Linha do meio da caixa | mediana ($Q_2$) |
| Bordas da caixa | $Q_1$ e $Q_3$ |
| Altura da caixa | IQR |
| "Bigodes" | tipicamente até $Q_1 - 1{,}5 \cdot \text{IQR}$ e $Q_3 + 1{,}5 \cdot \text{IQR}$ |
| Pontos isolados | outliers (além dos bigodes) |

## Por que usar IQR em vez de desvio padrão?

| IQR | Desvio padrão |
| --- | --- |
| Robusto a outliers | Muito sensível a outliers |
| Não depende da forma da distribuição | Bem interpretável só na normal |
| Vai bem com **mediana** | Vai bem com **média** |

A regra prática:

- Reportou a **mediana**? Reporte o **IQR** junto.
- Reportou a **média**? Reporte o **desvio padrão** junto.

## Detectando outliers

Uma regra prática (mas não universal):

$$
\text{outlier} \iff x < Q_1 - 1{,}5 \cdot \text{IQR} \quad \text{ou} \quad x > Q_3 + 1{,}5 \cdot \text{IQR}
$$

> Atenção: outlier "estatístico" não significa "valor errado". Pode ser um caso raro mas legítimo (um paciente com doença atípica, por exemplo). Antes de remover, **investigue**.
