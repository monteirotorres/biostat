# Hipótese nula (H₀) e alternativa (H₁)

Todo teste de hipóteses compara duas afirmações concorrentes sobre a população.

## Hipótese nula (H₀)

A hipótese de **não-efeito**, **não-diferença**, **status quo**. É a hipótese que pretendemos colocar em prova.

### Exemplos

- "O novo remédio **não** altera a pressão arterial."
- "**Não** há diferença entre as médias dos dois grupos."
- "Os dados seguem **distribuição normal**."
- "As variáveis são **independentes**."

> A hipótese nula é sempre formulada como uma **igualdade** ou ausência de relação.

## Hipótese alternativa (H₁ ou Hₐ)

A hipótese que afirma **algum efeito** ou **alguma diferença**. É o que você normalmente está tentando demonstrar.

### Exemplos

- "O novo remédio reduz a pressão arterial."
- "As médias são diferentes."
- "Os dados não são normais."
- "Há associação entre as variáveis."

## Formulações

H₁ pode ser **bilateral** (também chamada *two-sided*) ou **unilateral** (*one-sided*).

### Bilateral

Detecta diferença em qualquer direção:

$$
H_0: \mu = \mu_0 \quad \text{vs.} \quad H_1: \mu \neq \mu_0
$$

### Unilateral à direita

Só rejeita H₀ se o efeito for "para mais":

$$
H_0: \mu \leq \mu_0 \quad \text{vs.} \quad H_1: \mu > \mu_0
$$

### Unilateral à esquerda

Só rejeita H₀ se o efeito for "para menos":

$$
H_0: \mu \geq \mu_0 \quad \text{vs.} \quad H_1: \mu < \mu_0
$$

## Quando usar cada uma?

| Caso | Hipótese |
| --- | --- |
| Não tenho ideia do sentido do efeito | Bilateral |
| Sei (por razões biológicas/clínicas) que o efeito só pode ser em uma direção | Unilateral |

> Atenção: a escolha **deve ser feita antes** de olhar os dados. Mudar para unilateral após ver os resultados é uma forma de manipulação.

## A analogia do júri

| Estatística | Júri criminal |
| --- | --- |
| H₀ | "Réu é inocente" |
| H₁ | "Réu é culpado" |
| Dados | Evidências |
| Rejeitar H₀ | Condenar |
| Não rejeitar H₀ | Absolver (por insuficiência de provas) |

**Não rejeitar H₀ ≠ provar H₀.** Falta de evidências para condenar não é prova de inocência. Em estatística, é a mesma coisa: dizer "não rejeitamos H₀" significa apenas que **os dados não fornecem evidência suficiente** contra ela.

## Exemplos práticos

### Ensaio clínico

- H₀: O remédio A e o remédio B têm a mesma eficácia.
- H₁: A eficácia é diferente.

### Estudo de associação

- H₀: Não há associação entre tabagismo e câncer.
- H₁: Há associação.

### Validação de método de laboratório

- H₀: Os dois métodos dão o mesmo resultado.
- H₁: Os métodos diferem.

## Resumo

| Etapa | Pergunta |
| --- | --- |
| Formular H₀ | "O que significa 'nada acontece'?" |
| Formular H₁ | "Qual é o efeito que eu quero demonstrar?" |
| Coletar dados | Observar a amostra |
| Calcular estatística | Comparar dados com H₀ |
| Calcular valor-p | Quão extremos os dados são se H₀ for verdadeira? |
| Decidir | Rejeitar ou não rejeitar H₀ |
