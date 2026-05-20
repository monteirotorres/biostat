# Amostra e população

Quando estudamos um fenômeno biológico, normalmente queremos tirar conclusões sobre **todos** os indivíduos de um determinado grupo. Mas, na prática, é quase sempre impossível medir todos eles. Por isso, medimos apenas alguns e tentamos generalizar o resultado.

## População

A **população** é o conjunto completo de todos os indivíduos, objetos ou medidas que nos interessa estudar.

Exemplos de população em pesquisa biomédica:

- todos os adultos brasileiros com hipertensão;
- todos os camundongos de uma determinada linhagem;
- todas as células de uma cultura;
- todos os pacientes que receberam um determinado tratamento.

> A população é definida pela **pergunta** de pesquisa, não pelo tamanho. Pode ser pequena (todos os pacientes de um hospital) ou enorme (toda a humanidade).

## Amostra

A **amostra** é um subconjunto da população, escolhido para representá-la.

Trabalhamos com amostras porque:

- medir toda a população é caro;
- medir toda a população demora muito;
- em muitos casos é fisicamente impossível.

## Parâmetro vs. estatística

Esta distinção é fundamental e aparecerá ao longo de todo o curso:

| Conceito | Refere-se a | Símbolo da média | Símbolo do desvio padrão |
| --- | --- | --- | --- |
| **Parâmetro** | População inteira | $\mu$ (mi) | $\sigma$ (sigma) |
| **Estatística** | Amostra | $\bar{x}$ (x-barra) | $s$ |

- O **parâmetro** é o valor *verdadeiro*, mas geralmente desconhecido.
- A **estatística** é o valor *calculado* a partir da amostra. Ela é o que usamos para *estimar* o parâmetro.

## Por que amostragem aleatória?

Para que uma amostra represente bem a população, ela precisa ser **aleatória** — ou seja, cada indivíduo da população deve ter a mesma chance de ser escolhido.

Uma amostra mal coletada gera conclusões erradas, mesmo com matemática perfeita. Por exemplo, se você quer saber o peso médio dos adultos brasileiros e mede apenas frequentadores de academia, sua amostra é **enviesada** (em inglês, *biased*).

## Resumo

```mermaid
flowchart LR
    P["População (μ, σ desconhecidos)"] -->|amostragem aleatória| A["Amostra (x̄, s calculados)"]
    A -->|inferência| P
```

Repare na ideia central da estatística: **medimos a amostra para aprender sobre a população**.
