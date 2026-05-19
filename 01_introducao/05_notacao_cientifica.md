# Notação científica

Forma compacta de escrever números muito grandes ou muito pequenos.

## A regra

$$
N = a \times 10^{n}
$$

Onde:

- $1 \leq |a| < 10$ (a chamada **mantissa**);
- $n$ é um inteiro (o **expoente**).

## Exemplos

| Número | Notação científica |
| --- | --- |
| $6\,022\,000\,000\,000\,000\,000\,000\,000$ (número de Avogadro) | $6{,}022 \times 10^{23}$ |
| $0{,}000\,000\,001\,602$ (carga do elétron, em C) | $1{,}602 \times 10^{-9}$ |
| $300\,000\,000$ (velocidade da luz, em m/s) | $3 \times 10^{8}$ |

## Sinal do expoente

- **Positivo** → número grande. Desloca a vírgula para a **direita**.
- **Negativo** → número pequeno. Desloca a vírgula para a **esquerda**.

$$
2{,}5 \times 10^{4} = 25\,000
$$

$$
2{,}5 \times 10^{-4} = 0{,}000\,25
$$

## Operações

Em multiplicação e divisão, os expoentes somam e subtraem:

$$
(a \times 10^{m}) \cdot (b \times 10^{n}) = (a \cdot b) \times 10^{m+n}
$$

$$
\frac{a \times 10^{m}}{b \times 10^{n}} = \frac{a}{b} \times 10^{m-n}
$$

### Exemplo

$$
(3 \times 10^{6}) \times (2 \times 10^{-3}) = 6 \times 10^{3} = 6\,000
$$

## Em Python

Python escreve automaticamente em notação científica para números muito grandes ou pequenos. Use `e` no lugar de "$\times 10$":

| Em ciência | Em Python |
| --- | --- |
| $6{,}022 \times 10^{23}$ | `6.022e23` |
| $1{,}602 \times 10^{-9}$ | `1.602e-9` |

## Em bioestatística

Aparece com frequência quando reportamos:

- p-valores muito pequenos (`p = 3.2e-7`);
- concentrações em biologia molecular (`1 nM = 1e-9 M`);
- contagens muito grandes (`6e9` células no corpo humano).
