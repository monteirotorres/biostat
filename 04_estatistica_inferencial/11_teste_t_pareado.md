# Teste t pareado

Compara duas medidas feitas **no mesmo indivíduo** (ou em pares casados de indivíduos). Cada par é tratado como uma única observação.

## Quando usar

Sempre que houver **dependência natural** entre os dois conjuntos:

- **Antes vs. depois** de uma intervenção no mesmo paciente.
- Dois métodos analíticos aplicados à **mesma amostra**.
- Dois olhos do mesmo paciente.
- Gêmeos.
- Pares casados em design *matched-pairs*.

## A ideia

Em vez de comparar duas distribuições, calculamos a **diferença** $d_i = x_i^{\text{depois}} - x_i^{\text{antes}}$ para cada indivíduo, e testamos se a média dessas diferenças é zero.

$$
H_0: \mu_d = 0
$$

$$
H_1: \mu_d \neq 0
$$

Ou seja: o teste t pareado se reduz a um **teste t para uma amostra** aplicado às **diferenças**.

## Estatística do teste

$$
t = \frac{\bar{d}}{s_d / \sqrt{n}}
$$

Onde:

- $\bar{d}$: média das diferenças;
- $s_d$: desvio padrão das diferenças;
- $n$: número de pares.

Sob H₀, $t$ segue distribuição t com $n - 1$ graus de liberdade.

## Exemplo

Pressão arterial sistólica antes e depois de um remédio em 8 pacientes:

| Paciente | Antes | Depois | $d_i$ |
| --- | --- | --- | --- |
| 1 | 142 | 135 | 7 |
| 2 | 138 | 130 | 8 |
| 3 | 145 | 140 | 5 |
| 4 | 150 | 142 | 8 |
| 5 | 139 | 132 | 7 |
| 6 | 144 | 138 | 6 |
| 7 | 141 | 134 | 7 |
| 8 | 147 | 139 | 8 |

$\bar{d} = 7{,}0$, $s_d \approx 1{,}07$.

$$
t = \frac{7{,}0}{1{,}07 / \sqrt{8}} \approx 18{,}5
$$

Com 7 gl, $p$ é minúsculo. Rejeitamos H₀: o remédio reduz a pressão.

## Por que pareado é mais poderoso

Em estudos pareados, **eliminamos a variabilidade entre indivíduos** — só vemos a variação dentro de cada um. Isso torna o teste muito mais sensível para detectar pequenas diferenças.

Se quiséssemos comparar dois grupos independentes (uns recebem o remédio, outros não), as variações entre pessoas (idade, peso, genética) atrapalhariam mais o sinal. Pareando, cada paciente é seu próprio controle.

## Suposições

- As **diferenças** $d_i$ devem seguir aproximadamente uma distribuição normal (não os dados originais!).
- Os pares devem ser **independentes entre si** (paciente 1 independe do paciente 2).
- Não há outliers extremos nas diferenças.

> Se as diferenças não forem normais, ou se a amostra for muito pequena, use o **teste de Wilcoxon do sinal pareado** (alternativa não paramétrica).

## Versão unilateral

Se a direção do efeito é pré-especificada:

- $H_1: \mu_d > 0$ → teste à direita.
- $H_1: \mu_d < 0$ → teste à esquerda.

## Diferença entre pareado e independente

| Aspecto | Pareado | Independente |
| --- | --- | --- |
| Indivíduos | Os mesmos (ou pares casados) | Diferentes |
| Pergunta | Mudança dentro do indivíduo | Diferença entre grupos |
| Poder | Maior | Menor |
| Aplicação errada | Confunde os pares | Trata pareados como independentes (perde poder) |

## Cuidados

1. Não tratar dados pareados como independentes — isso reduz o poder e **infla os erros padrão**.
2. Não tratar dados independentes como pareados — isso é ainda pior; inverte completamente a análise.
3. Em pareamento com **n pequeno**, considere usar Wilcoxon do sinal pareado por segurança.
