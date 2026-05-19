# Testes não paramétricos

Os testes paramétricos (t, ANOVA, etc.) assumem que os dados seguem alguma distribuição (geralmente normal). Quando essa suposição falha, ou quando os dados são **ordinais**, recorremos aos **testes não paramétricos**.

## Quando usar

| Situação | Por que testes paramétricos podem falhar |
| --- | --- |
| Dados ordinais (escalas tipo Likert, graus de dor) | Não fazem sentido em escala numérica |
| Distribuição muito assimétrica em amostras pequenas | TLC ainda não "salvou" |
| Outliers extremos não removíveis | Distorcem média e desvio padrão |
| Amostras muito pequenas | Difícil verificar normalidade |

## A ideia geral

A maioria dos testes não paramétricos opera com **postos** (em inglês, *ranks*) em vez dos valores brutos:

1. Ordenam-se todos os valores.
2. Cada valor recebe um posto (1 para o menor, $n$ para o maior).
3. Testam-se hipóteses sobre os postos.

Por usar postos, ficam imunes a outliers e não exigem normalidade.

## Os principais testes

### Mann–Whitney U — substitui o teste t independente

Compara **duas amostras independentes**.

- $H_0$: as duas distribuições são iguais.
- $H_1$: uma tende a ter valores maiores que a outra.

Em pacotes, está como `mannwhitneyu` ou *Wilcoxon rank-sum* (são equivalentes).

### Wilcoxon do sinal pareado — substitui o teste t pareado

Compara **duas medidas no mesmo indivíduo**.

- $H_0$: a mediana das diferenças é zero.
- $H_1$: a mediana das diferenças não é zero.

### Kruskal–Wallis — substitui a ANOVA one-way

Compara **três ou mais grupos independentes**.

- $H_0$: as distribuições dos grupos são iguais.
- $H_1$: pelo menos um grupo difere.

Se rejeita H₀, usa-se Dunn ou Wilcoxon pareados com correção de Bonferroni para identificar quais grupos diferem.

### Friedman — substitui a ANOVA de medidas repetidas

Para **três ou mais medidas pareadas** no mesmo indivíduo.

### Spearman / Kendall — substituem Pearson

Para correlação. Vistos no tópico de correlação.

### Qui-quadrado / Fisher exato

Para variáveis categóricas. Esses são "não paramétricos" no sentido de não pressuporem distribuição contínua.

## Mapa de equivalências

| Pergunta | Teste paramétrico | Teste não paramétrico |
| --- | --- | --- |
| Média ≠ valor de referência? | Teste t uma amostra | Wilcoxon do sinal |
| Duas médias independentes diferem? | Teste t independente | Mann–Whitney U |
| Duas medidas pareadas diferem? | Teste t pareado | Wilcoxon do sinal pareado |
| Três ou mais grupos independentes diferem? | ANOVA one-way | Kruskal–Wallis |
| Três ou mais medidas pareadas diferem? | ANOVA medidas repetidas | Friedman |
| Duas variáveis numéricas se associam? | Pearson | Spearman ou Kendall |
| Variáveis categóricas se associam? | – | Qui-quadrado / Fisher |

## Vantagens e desvantagens

### Vantagens

- Não exigem normalidade.
- Robustos a outliers.
- Aplicáveis a dados ordinais.

### Desvantagens

- Menor **poder estatístico** quando as suposições paramétricas são válidas.
- Testam **distribuições** ou **medianas**, não médias — interpretação pode ser menos intuitiva.
- IC para mediana é mais difícil de calcular.

## Quando preferir paramétrico

- Amostra grande ($n \geq 30$) e dados não muito assimétricos: paramétrico costuma ser mais poderoso.
- Necessidade de modelos complexos (regressão, modelos mistos): mais natural em paramétrico.

## Quando preferir não paramétrico

- Amostras pequenas com clara violação da normalidade.
- Dados ordinais.
- Outliers extremos que não dá para remover.
- Quando o foco é a **mediana** ou a **distribuição**, não a média.

## Resumo

A escolha não é uma religião — depende dos dados e da pergunta. Em muitos estudos, os autores reportam **ambos** os testes e mostram que dão a mesma conclusão. Isso fortalece a robustez da análise.

> Regra prática: olhe a distribuição **antes** de escolher o teste. Se for clara e razoável a aproximação normal (especialmente com $n \geq 30$), use paramétrico. Se houver dúvida, use o não paramétrico — ou ambos.
