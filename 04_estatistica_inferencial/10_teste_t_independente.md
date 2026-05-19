# Teste t para duas amostras independentes

Compara as médias de **dois grupos diferentes** de indivíduos. É o teste mais clássico em estudos comparativos.

## Quando usar

- Variável de interesse **quantitativa**.
- Dois grupos **independentes** (indivíduos diferentes em cada).
- Variável aproximadamente **normal** em cada grupo, ou amostras grandes.

### Exemplos clínicos

- Pacientes que receberam tratamento A vs. tratamento B.
- Homens vs. mulheres em determinada medida fisiológica.
- Camundongos *knock-out* vs. selvagens.

## Hipóteses

$$
H_0: \mu_1 = \mu_2
$$

$$
H_1: \mu_1 \neq \mu_2
$$

## Duas variantes

### Teste t de Student (assume variâncias iguais)

$$
t = \frac{\bar{x}_1 - \bar{x}_2}{s_p \sqrt{\dfrac{1}{n_1} + \dfrac{1}{n_2}}}
$$

Onde $s_p$ é o **desvio padrão combinado** (*pooled*):

$$
s_p = \sqrt{\frac{(n_1 - 1) s_1^{2} + (n_2 - 1) s_2^{2}}{n_1 + n_2 - 2}}
$$

Graus de liberdade: $n_1 + n_2 - 2$.

### Teste t de Welch (não assume variâncias iguais) — recomendado

$$
t = \frac{\bar{x}_1 - \bar{x}_2}{\sqrt{\dfrac{s_1^{2}}{n_1} + \dfrac{s_2^{2}}{n_2}}}
$$

Os graus de liberdade são ajustados por uma fórmula complicada (Welch–Satterthwaite). O `scipy.stats.ttest_ind` com `equal_var=False` faz tudo automaticamente.

> Em **2024**, a recomendação amplamente aceita é usar **Welch por padrão**. Ele é tão bom quanto Student quando as variâncias são iguais, e muito melhor quando são diferentes — sem que precisemos fazer um pré-teste.

## Exemplo

Comparando peso (kg) entre dois grupos:

| Grupo | $n$ | $\bar{x}$ | $s$ |
| --- | --- | --- | --- |
| Tratamento | 25 | 72 | 8 |
| Controle | 28 | 78 | 10 |

Pelo Welch:

$$
t = \frac{72 - 78}{\sqrt{8^{2}/25 + 10^{2}/28}} \approx \frac{-6}{2{,}48} \approx -2{,}42
$$

Valor-p $\approx 0{,}019$. Rejeitamos H₀: há diferença entre os grupos.

## IC para a diferença

$$
(\bar{x}_1 - \bar{x}_2) \pm t^{*} \cdot \sqrt{\dfrac{s_1^{2}}{n_1} + \dfrac{s_2^{2}}{n_2}}
$$

No exemplo: $-6 \pm 2{,}01 \cdot 2{,}48 \approx [-11{,}0;\, -1{,}0]$. Como zero não está no intervalo, há diferença significativa.

## Tamanho de efeito (d de Cohen)

O valor-p depende de $n$; já o tamanho de efeito é independente:

$$
d = \frac{\bar{x}_1 - \bar{x}_2}{s_p}
$$

| $|d|$ | Interpretação |
| --- | --- |
| 0,2 | pequeno |
| 0,5 | médio |
| 0,8 | grande |

> Reportar apenas o valor-p sem o tamanho de efeito é cada vez menos aceitável em revistas científicas.

## Suposições

| Suposição | Como verificar | O que fazer se violar |
| --- | --- | --- |
| Normalidade | histograma, Q-Q plot, Shapiro–Wilk | grande $n$ ou Mann–Whitney |
| Independência | desenho do estudo | usar teste pareado se for o caso |
| Variâncias iguais | teste F, Levene | usar Welch (já cobre isso) |

## Erros comuns

1. **Usar teste t pareado** quando os grupos são independentes — ou vice-versa. Cada um responde a uma pergunta diferente.
2. **Comparar mais de dois grupos** dois a dois usando vários testes t. Isso infla o erro tipo I — use **ANOVA**.
3. **Aplicar em dados ordinais** (escalas de Likert, graus de dor). Use Mann–Whitney.
