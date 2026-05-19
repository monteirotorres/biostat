# Distribuição binomial

A distribuição binomial conta **quantos sucessos** ocorrem em $n$ tentativas independentes, cada uma com a mesma probabilidade $p$ de sucesso.

## Condições para aplicar

| Condição | Significa |
| --- | --- |
| **Número fixo** de tentativas ($n$) | Você decide $n$ antes de começar |
| Cada tentativa é **binária** | sucesso ou fracasso |
| Probabilidade $p$ **constante** | mesma em todas as tentativas |
| Tentativas **independentes** | uma não afeta a outra |

## Fórmula

A probabilidade de obter exatamente $k$ sucessos em $n$ tentativas é:

$$
P(X = k) = \binom{n}{k} p^{k} (1 - p)^{n - k}
$$

Onde:

- $\binom{n}{k} = \dfrac{n!}{k!\,(n-k)!}$ é o coeficiente binomial (vem da análise combinatória).

## Esperança e variância

$$
E(X) = n \cdot p
$$

$$
\text{Var}(X) = n \cdot p \cdot (1 - p)
$$

## Exemplos típicos em biologia

- Lançar uma moeda 10 vezes; contar caras.
- Aplicar um teste com sensibilidade conhecida em 50 pacientes doentes; contar quantos vão positivar.
- Em uma colônia onde 30% das células expressam um gene, escolher 20 ao acaso e contar quantas expressam.
- Quantos pacientes em um ensaio de 100 vão apresentar um efeito adverso, se a taxa esperada é 5%?

## Calculando probabilidades

### Probabilidade de exatamente $k$ sucessos

$$
P(X = k) = \binom{n}{k} p^{k} (1 - p)^{n - k}
$$

### Probabilidade de no máximo $k$ sucessos (acumulada)

$$
P(X \leq k) = \sum_{i = 0}^{k} \binom{n}{i} p^{i} (1 - p)^{n - i}
$$

### Probabilidade de pelo menos $k$ sucessos

$$
P(X \geq k) = 1 - P(X \leq k - 1)
$$

## Exemplo: moeda

Lançar uma moeda honesta 10 vezes. Qual a probabilidade de obter exatamente 7 caras?

$$
P(X = 7) = \binom{10}{7} (0{,}5)^{7} (0{,}5)^{3} = 120 \cdot 0{,}5^{10} \approx 0{,}117
$$

Ou seja, cerca de 11,7%.

## Aproximação pela normal

Quando $n$ é grande e $p$ não é próximo de 0 ou 1, a binomial pode ser aproximada por uma normal:

$$
X \approx \mathcal{N}\!\left( np, \; \sqrt{np(1-p)} \right)
$$

A regra prática: $np \geq 10$ e $n(1-p) \geq 10$. Essa aproximação é a base de muitos testes para proporções.

## Conexão com Bernoulli

Cada tentativa individual segue uma distribuição **Bernoulli** (caso especial da binomial com $n = 1$). A binomial é a soma de $n$ Bernoullis independentes.

## Visualização

A distribuição binomial tem formato dependente de $p$:

- $p = 0{,}5$ → simétrica.
- $p < 0{,}5$ → assimétrica à direita.
- $p > 0{,}5$ → assimétrica à esquerda.

À medida que $n$ aumenta, a forma se aproxima de uma curva normal (de novo, o TLC!).
