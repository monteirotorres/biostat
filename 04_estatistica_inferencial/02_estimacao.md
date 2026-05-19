# Estimação

A **estimação** consiste em usar dados de uma amostra para chutar (com algum embasamento matemático) o valor de um parâmetro populacional.

## Parâmetros vs. estatísticas — revisão

| População | Amostra | Símbolo populacional | Símbolo amostral |
| --- | --- | --- | --- |
| Média | Média | $\mu$ | $\bar{x}$ |
| Desvio padrão | Desvio padrão | $\sigma$ | $s$ |
| Proporção | Proporção | $\pi$ ou $p$ | $\hat{p}$ |
| Variância | Variância | $\sigma^{2}$ | $s^{2}$ |

A média, desvio padrão etc. da amostra **são** os estimadores naturais dos respectivos parâmetros da população.

## Estimação pontual

Um único número como melhor "chute" para o parâmetro:

$$
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_{i} \quad \text{estima} \quad \mu
$$

$$
\hat{p} = \frac{k}{n} \quad \text{estima} \quad \pi
$$

## Estimação intervalar

A estimação pontual é insatisfatória porque **nunca é exata**. A cada amostra teríamos uma estimativa um pouco diferente. Por isso preferimos um **intervalo** que contenha o valor verdadeiro com alta probabilidade.

A forma geral é:

$$
\text{estimativa pontual} \pm \text{margem de erro}
$$

A "margem de erro" depende:

- da **variabilidade** dos dados (mais variável → maior margem);
- do **tamanho da amostra** (mais dados → menor margem);
- do **nível de confiança** desejado (95% padrão).

## Propriedades de um bom estimador

| Propriedade | Significado |
| --- | --- |
| **Não viesado** | $E(\hat{\theta}) = \theta$ — em média, acerta o parâmetro |
| **Eficiente** | tem variância pequena |
| **Consistente** | quando $n \to \infty$, $\hat{\theta} \to \theta$ |
| **Robusto** | pouco afetado por suposições violadas ou outliers |

A média amostral $\bar{x}$ é não viesada e consistente para $\mu$. Por isso é o estimador padrão.

## Erro padrão

Toda estimativa amostral tem variabilidade — ela mesma é uma variável aleatória. O **erro padrão** mede essa variabilidade:

$$
\text{EP}(\bar{x}) = \frac{s}{\sqrt{n}}
$$

> O erro padrão diminui à medida que $n$ aumenta — por isso amostras maiores dão estimativas mais precisas.

## Estimadores em pacotes

A maioria dos pacotes estatísticos calcula automaticamente as estimativas pontuais junto com seus erros padrão e intervalos de confiança. No `scipy.stats`, por exemplo:

- `stats.sem(x)` → erro padrão da média.
- `stats.t.interval(...)` → intervalo de confiança para a média.

Veremos os intervalos de confiança em detalhes no próximo tópico.
