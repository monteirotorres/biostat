# Nível de significância (α)

O **nível de significância** ($\alpha$) é o limiar que escolhemos para considerar um resultado "estatisticamente significativo".

## Definição

$\alpha$ é a probabilidade que aceitamos de rejeitar $H_0$ **quando ela é verdadeira** (cometer um erro do **tipo I**).

$$
\alpha = P(\text{rejeitar } H_0 \mid H_0 \text{ é verdadeira})
$$

## Valores típicos

| $\alpha$ | Uso |
| --- | --- |
| 0,05 | Mais comum em biologia, ciências sociais |
| 0,01 | Áreas que exigem maior rigor (clínica de risco) |
| 0,001 | Quando o custo do erro tipo I é muito alto |
| $5 \times 10^{-8}$ | Estudos GWAS (correção para milhões de testes) |

> $\alpha = 0{,}05$ significa: aceitamos errar (rejeitar H₀ sem motivo) em 5 de cada 100 análises.

## Como α é usado no teste

1. **Antes** de coletar dados, fixamos $\alpha$ (geralmente 0,05).
2. Calculamos o **valor-p** a partir dos dados.
3. Comparamos:
   - $p < \alpha$ → **rejeitamos** $H_0$ (resultado "significativo").
   - $p \geq \alpha$ → **não rejeitamos** $H_0$.

## Região crítica

A estatística do teste cai em uma **região crítica** com probabilidade $\alpha$ sob H₀:

```
        zona de não-rejeição                rejeição (α/2)
           ←──────────→
   ←─ rej (α/2) ─→               ←────────────→
   ┌──────────────────────────────────────────┐
   │                  H₀                       │
   │                                           │
   └─────────────|──────────────|──────────────┘
              -z*                +z*
```

Para um teste bilateral com $\alpha = 0{,}05$ usando a normal:

- $z^{*} = 1{,}96$
- Rejeita-se H₀ se a estatística cai além de $\pm 1{,}96$.

## A escolha de α é arbitrária

Não há nada de "mágico" em 0,05. É uma **convenção** estabelecida há quase um século. Em algumas áreas, outras escolhas fazem mais sentido:

- **Triagem populacional**: pode-se aceitar $\alpha$ maior (0,10) porque o custo de perder um caso é alto.
- **Genética populacional (GWAS)**: usa-se $\alpha$ extremamente pequeno porque se testam milhões de SNPs simultaneamente.
- **Decisões irreversíveis**: $\alpha$ menor é mais prudente.

## A relação com o IC

Existe uma equivalência:

$$
\text{nível de confiança} + \alpha = 1
$$

- $\alpha = 0{,}05$ ↔ IC 95%.
- $\alpha = 0{,}01$ ↔ IC 99%.

## Erro tipo I e tipo II

Reduzir $\alpha$ diminui a chance de **rejeitar H₀ por engano** (tipo I), mas aumenta a chance de **não detectar um efeito real** (tipo II). Os dois erros estão em **tensão**.

| Decisão | H₀ verdadeira | H₀ falsa |
| --- | --- | --- |
| Rejeitar H₀ | **Erro tipo I** ($\alpha$) | Decisão correta (poder, $1 - \beta$) |
| Não rejeitar H₀ | Decisão correta | **Erro tipo II** ($\beta$) |

## Cuidados com a interpretação de "significativo"

1. **"Significativo" não quer dizer importante.** Um efeito minúsculo pode ser estatisticamente significativo se $n$ for muito grande.
2. **"Não significativo" não quer dizer "sem efeito".** Pode ser falta de poder estatístico.
3. **Reportar apenas "significativo / não significativo" perde informação**: o valor-p exato e o tamanho de efeito carregam mais informação.
