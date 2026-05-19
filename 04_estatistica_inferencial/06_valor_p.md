# Valor-p

O **valor-p** (p-value) é talvez o número mais usado e mais mal interpretado da estatística.

## Definição correta

> O **valor-p** é a probabilidade de obter dados **tão ou mais extremos** que os observados, **supondo que H₀ seja verdadeira**.

Formalmente:

$$
p = P(T \geq t_{\text{obs}} \mid H_0)
$$

(ou bilateral, conforme a hipótese).

## Como interpretar

| Valor-p | Interpretação informal |
| --- | --- |
| Muito pequeno (< 0,001) | Dados muito improváveis sob H₀ → forte evidência contra H₀ |
| Pequeno (< 0,05) | Dados improváveis sob H₀ → evidência razoável contra H₀ |
| Grande (> 0,05) | Dados compatíveis com H₀ → não há evidência para rejeitá-la |

## A regra de decisão

$$
\text{rejeitar } H_0 \iff p < \alpha
$$

## O que o valor-p NÃO é

**Erros comuns** que aparecem até em artigos publicados:

1. **NÃO é** a probabilidade de H₀ ser verdadeira.
   - $p \neq P(H_0 \mid \text{dados})$.
2. **NÃO é** a probabilidade de o resultado ser por acaso.
3. **NÃO mede** o tamanho do efeito — apenas a evidência **contra** H₀.
4. **NÃO indica** importância prática. Um $p$ minúsculo pode ser irrelevante clinicamente.

## A famosa "linha mágica" de 0,05

A escolha de 0,05 é histórica e arbitrária. Em 2016, a *American Statistical Association* publicou um manifesto alertando contra a interpretação binária ("significativo / não significativo"). Algumas recomendações modernas:

- Reportar **valores-p exatos** (ex.: $p = 0{,}034$), e não apenas "p < 0,05".
- Sempre acompanhar de **tamanho de efeito** e **intervalo de confiança**.
- Evitar dicotomizar resultados em "achou / não achou".

## Exemplos numéricos

### Moeda viciada?

Lancei 100 vezes uma moeda e deu 60 caras. Se ela fosse honesta:

$$
p = P(X \geq 60 \mid p = 0{,}5) + P(X \leq 40 \mid p = 0{,}5)
$$

Em uma distribuição binomial(100, 0,5), $p \approx 0{,}057$. **Não rejeitamos** H₀ ao nível 5% — não temos evidência forte de que a moeda é viciada.

### Pressão arterial antes e depois

Comparando 30 pacientes antes e depois de um remédio, $p = 0{,}002$. Isso significa que se o remédio não tivesse efeito, dados como esses (ou mais extremos) apareceriam em apenas 2 de cada 1000 estudos. **Rejeitamos** H₀.

## Valor-p unilateral vs. bilateral

- **Bilateral**: considera desvios em qualquer direção.
- **Unilateral**: considera desvios apenas em uma direção. O valor-p costuma ser **a metade** do bilateral, mas só é apropriado se a direção do efeito for **pré-especificada**.

## Múltiplas comparações

Se fizermos 20 testes independentes com $\alpha = 0{,}05$, esperamos **em média 1 falso positivo** por puro acaso. Por isso, em análises com muitos testes (por exemplo, microarranjos genéticos), precisamos **corrigir** o valor-p:

- **Bonferroni**: divide $\alpha$ pelo número de testes (conservador).
- **FDR (Benjamini–Hochberg)**: controla a taxa de descobertas falsas (menos conservador).

## Resumo

| Pergunta | Quem responde |
| --- | --- |
| "Há evidência contra H₀?" | Valor-p |
| "Qual o tamanho do efeito?" | Estimativa pontual + IC |
| "O efeito é clinicamente importante?" | Conhecimento da área, não a estatística |

> Aprender a interpretar o valor-p corretamente é **a habilidade mais importante** ao consumir literatura científica.
