# Erros tipo I e tipo II

Como toda inferência é baseada em uma amostra finita, existem **dois tipos de erro** que podemos cometer ao tomar uma decisão sobre H₀.

## A tabela 2x2 da decisão

|   | H₀ é verdadeira | H₀ é falsa |
| --- | --- | --- |
| **Rejeitar H₀** | Erro tipo I (α) | Decisão correta (poder, $1-\beta$) |
| **Não rejeitar H₀** | Decisão correta (1−α) | Erro tipo II (β) |

## Erro tipo I (α)

**Falso positivo**: rejeitar H₀ quando ela era verdadeira. Concluir que há efeito quando na verdade não há.

$$
\alpha = P(\text{rejeitar } H_0 \mid H_0 \text{ verdadeira})
$$

> Em pesquisa, um erro tipo I leva a "**falsas descobertas**" — afirmar que um remédio funciona quando não funciona.

Controlamos diretamente: escolhemos $\alpha$ (geralmente 0,05) **antes** do teste.

## Erro tipo II (β)

**Falso negativo**: não rejeitar H₀ quando ela era falsa. Perder uma diferença real.

$$
\beta = P(\text{não rejeitar } H_0 \mid H_0 \text{ falsa})
$$

> Em pesquisa, um erro tipo II leva a perder uma descoberta real — concluir que um remédio não funciona quando ele funciona.

$\beta$ **não** é escolhido diretamente; depende de:

- tamanho real do efeito (quanto maior, menor o β);
- tamanho da amostra (n maior reduz β);
- variabilidade dos dados (menor σ reduz β);
- nível de significância (α menor aumenta β).

## Poder estatístico

O **poder** do teste é a probabilidade de **detectar** um efeito real:

$$
\text{poder} = 1 - \beta = P(\text{rejeitar } H_0 \mid H_0 \text{ falsa})
$$

Convencionalmente, um estudo é considerado bem dimensionado quando o poder é **≥ 80%**.

## A tensão entre α e β

Reduzir $\alpha$ **aumenta** $\beta$ (e vice-versa), para um $n$ fixo:

```
α pequeno → critério mais rigoroso → ↑ β (perde efeitos reais)
α grande  → critério mais leniente → ↓ β (mas mais falsos positivos)
```

A única forma de reduzir **os dois** ao mesmo tempo é **aumentar n** ou **reduzir a variabilidade**.

## Analogia com julgamento criminal

| Estatística | Justiça |
| --- | --- |
| Erro tipo I | Condenar inocente |
| Erro tipo II | Absolver culpado |
| α baixo | "Inocente até prova em contrário" |
| Poder alto | Sistema judicial eficiente |

Sociedades preferem $\alpha$ baixo (preferem deixar culpados livres a condenar inocentes). A estatística geralmente faz a mesma escolha: prioriza evitar falsos positivos.

## Como aumentar o poder

| Estratégia | Como afeta o poder |
| --- | --- |
| Aumentar $n$ | ↑ |
| Aumentar o efeito real (impossível controlar) | ↑ |
| Reduzir variabilidade (controle experimental) | ↑ |
| Aumentar $\alpha$ | ↑ (mas aumenta erro tipo I) |
| Usar teste unilateral em vez de bilateral | ↑ (apenas quando justificável) |
| Usar teste mais eficiente | ↑ |

## Cálculo do tamanho de amostra

A pergunta clássica de planejamento de estudo:

> Quantos pacientes preciso recrutar para ter 80% de chance de detectar um efeito de tamanho $d$, com $\alpha = 0{,}05$?

Existem fórmulas e calculadoras para isso. Em comparação de médias com teste t, uma aproximação útil:

$$
n \approx 2 \cdot \left( \frac{z_{1-\alpha/2} + z_{1-\beta}}{d} \right)^{2}
$$

Onde $d = \dfrac{\mu_1 - \mu_2}{\sigma}$ é o **tamanho de efeito** padronizado (d de Cohen).

| d | Tamanho do efeito |
| --- | --- |
| 0,2 | Pequeno |
| 0,5 | Médio |
| 0,8 | Grande |

## Consequências de um estudo subdimensionado

Um estudo **subdimensionado** (com poder baixo) é eticamente questionável:

- Expõe pacientes a procedimentos sem ter chance real de chegar a uma conclusão.
- Pode gerar resultados negativos espúrios, levando a descartar tratamentos eficazes.
- Resultados positivos em estudos subdimensionados tendem a **exagerar o tamanho do efeito** (winner's curse).

Por isso o **cálculo amostral** deve ser feito **antes** de iniciar o estudo, e reportado.
