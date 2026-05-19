# Coeficiente de variação

O **coeficiente de variação** (CV) expressa a dispersão de forma **relativa** — como porcentagem da média.

## Fórmula

$$
\text{CV} = \frac{s}{\bar{x}} \cdot 100\%
$$

## Por que usá-lo?

O desvio padrão sozinho não diz muito sem o contexto da média. Um $s = 2$ kg é muito ou pouco?

- Em adultos com peso médio de 70 kg, $s = 2$ é **pequeno** ($\text{CV} \approx 3\%$).
- Em recém-nascidos com peso médio de 3 kg, $s = 2$ é **enorme** ($\text{CV} \approx 67\%$).

O CV permite comparar dispersão entre grupos **com médias muito diferentes** ou **em unidades diferentes**.

## Exemplo

Comparando a variabilidade da pressão arterial e da glicemia:

| Variável | Média | s | CV |
| --- | --- | --- | --- |
| Pressão arterial sistólica | 130 mmHg | 15 mmHg | 11,5% |
| Glicemia em jejum | 95 mg/dL | 8 mg/dL | 8,4% |

Apesar dos desvios padrão estarem em unidades totalmente diferentes, podemos dizer que a pressão é **relativamente mais variável** que a glicemia nessa amostra.

## Usos típicos em biologia

- **Reprodutibilidade de métodos**: um CV de 2–5% é excelente, 5–10% aceitável, >10% pode ser preocupante (em ensaios analíticos).
- **Variação entre indivíduos**: comparar dispersão de um parâmetro entre populações com médias diferentes.
- **Controle de qualidade**: limites de CV em laboratórios clínicos.

## Limitações

1. **Só faz sentido para variáveis em escala de razão** (com zero absoluto natural). Não use para temperatura em Celsius, pH ou pontuações de questionários.

2. **Instável quando a média está próxima de zero**: pequenas variações na média geram CVs enormes.

3. **Não é apropriado** para variáveis que podem assumir valores negativos.

4. **Cuidado com dados muito enviesados** — como a média pode não ser representativa, o CV também pode enganar.

## Outras versões

- **CV em forma decimal**: alguns trabalhos reportam $s / \bar{x}$ sem multiplicar por 100.
- **CV robusto**: $\text{IQR} / \text{mediana}$, mais resistente a outliers.
