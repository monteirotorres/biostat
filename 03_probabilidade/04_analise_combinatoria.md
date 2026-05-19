# Análise combinatória

Ferramenta para **contar** o número de resultados possíveis quando organizamos ou escolhemos elementos.

## Princípio fundamental da contagem

Se um experimento tem $a$ resultados possíveis em uma etapa e $b$ na próxima, o total de resultados é $a \cdot b$.

Exemplo: 3 camisas e 4 calças → $3 \cdot 4 = 12$ combinações.

## Fatorial

$$
n! = n \cdot (n-1) \cdot (n-2) \cdots 2 \cdot 1
$$

Por convenção, $0! = 1$.

Exemplos:

- $5! = 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 120$.
- $10! = 3\,628\,800$.

## Permutações — a ordem importa

Quantas formas de **organizar** $n$ objetos em fila?

$$
P_n = n!
$$

Exemplo: 4 pessoas em 4 cadeiras → $4! = 24$ arranjos.

### Permutações de $k$ entre $n$

Quantas formas de escolher $k$ objetos **em ordem** entre $n$ disponíveis?

$$
P(n, k) = \frac{n!}{(n - k)!}
$$

Exemplo: pódio de uma corrida de 10 atletas → $P(10, 3) = 10 \cdot 9 \cdot 8 = 720$.

## Combinações — a ordem NÃO importa

Quantas formas de **escolher** $k$ objetos entre $n$, sem se importar com a ordem?

$$
C(n, k) = \binom{n}{k} = \frac{n!}{k! \cdot (n - k)!}
$$

Exemplo clássico: jogo da Mega-Sena. Quantos resultados possíveis?

$$
\binom{60}{6} = 50\,063\,860
$$

Logo, a probabilidade de acertar um jogo simples é $1 / 50\,063\,860 \approx 2 \times 10^{-8}$.

## Permutações com repetição

Se temos $n$ objetos, dos quais $n_1$ são iguais entre si, $n_2$ iguais entre si, etc.:

$$
P_{\text{rep}} = \frac{n!}{n_1! \, n_2! \cdots}
$$

Exemplo: anagramas da palavra "ESTATÍSTICA" (11 letras, com repetições).

## Quando usar cada um

```mermaid
flowchart TD
    A[Escolhendo k entre n] --> B{Ordem importa?}
    B -->|Sim| P[Permutação<br>n!/(n-k)!]
    B -->|Não| C[Combinação<br>C(n,k)]
```

## Em bioestatística

A análise combinatória aparece principalmente em:

- cálculo de probabilidades em **distribuição binomial** (quantas sequências de sucessos);
- problemas de **amostragem** sem reposição;
- combinações em **estudos de associação genética**;
- montagem de **brackets** em ensaios clínicos.
