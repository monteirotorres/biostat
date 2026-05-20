# Lógica da inferência estatística

A inferência estatística é o conjunto de ferramentas que permite **tirar conclusões sobre uma população a partir de uma amostra**.

## A pergunta fundamental

Toda análise inferencial responde, em essência, à seguinte pergunta:

> Os padrões que vejo na minha amostra refletem **algo real** sobre a população, ou podem ser apenas **acaso**?

Por exemplo:

- Um novo remédio realmente reduz a pressão arterial, ou a diferença observada foi coincidência?
- Pinguins de duas ilhas diferentes têm pesos diferentes, ou a variação seria igual por acaso?
- Existe associação entre fumar e câncer, ou os números parecidos são casualidade?

## A estratégia geral

A inferência usa uma lógica que pode parecer estranha à primeira vista. Em vez de tentar "provar" diretamente que existe um efeito, fazemos o caminho inverso:

1. **Assumimos que não existe efeito** (hipótese nula, $H_0$).
2. **Calculamos a probabilidade** de observar os dados (ou algo mais extremo) sob essa suposição.
3. Se essa probabilidade for **muito baixa**, concluímos que $H_0$ provavelmente é falsa e rejeitamos.

É a mesma lógica de um julgamento criminal: o acusado é considerado **inocente** (H₀) até que as evidências (dados) sejam fortes o suficiente para afastar essa hipótese.

## As duas grandes famílias

A inferência se divide em duas tarefas relacionadas:

### Estimação

Atribuir um valor (ou intervalo de valores) plausível a um parâmetro populacional desconhecido.

- **Estimação pontual**: um único número (ex.: $\bar{x} = 170$ cm).
- **Estimação intervalar**: um intervalo (ex.: IC 95% = [168, 172] cm).

### Teste de hipóteses

Decidir entre duas afirmações concorrentes ($H_0$ vs. $H_1$), com base nos dados.

## A incerteza está sempre lá

Como toda inferência se baseia em uma amostra finita, **sempre há risco de erro**. A estatística não elimina esse risco — ela o **quantifica**.

Isso leva aos dois tipos de erro:

| Erro | O que é | Probabilidade |
| --- | --- | --- |
| **Tipo I** | Rejeitar $H_0$ quando ela é verdadeira | $\alpha$ |
| **Tipo II** | Não rejeitar $H_0$ quando ela é falsa | $\beta$ |

Veremos esses conceitos em detalhes mais à frente.

## O papel da inferência

Sem inferência estatística, qualquer um pode olhar para qualquer diferença na amostra e gritar "achei algo!". A estatística estabelece **critérios consensuais** para considerar uma diferença confiável. É um filtro contra o acaso e contra o viés do pesquisador.

## Estrutura desta parte do curso

Nos próximos tópicos, vamos:

1. Aprender a **estimar** parâmetros (pontual e por intervalos de confiança).
2. Entender a estrutura de um **teste de hipóteses**.
3. Conhecer os principais testes em bioestatística (t, z, ANOVA, qui-quadrado, correlação, regressão).
4. Ver alternativas **não paramétricas** quando as suposições falham.
