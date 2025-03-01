# Karatsuba_algorithm

## Sobre o Projeto

Este projeto implementa o **Algoritmo de Karatsuba**, um método eficiente para multiplicação de números inteiros grandes. O objetivo é demonstrar sua aplicação prática e analisar sua complexidade computacional.

## O que é o Algoritmo de Karatsuba?

O **Algoritmo de Karatsuba** foi desenvolvido por **Anatolii Alexeevitch Karatsuba** em 1960, é uma técnica que multiplica números grandes de forma eficiente, dividindo-os recursivamente em partes menores. Ele reduz a complexidade da multiplicação tradicional **O(n²)** para aproximadamente **O(n^(log₂3)) ≈ O(n^1.585)**, tornando-se um dos algoritmos mais rápidos para multiplicação de grandes inteiros.

## Como funciona o algoritmo?

O método de Karatsuba divide os números de entrada em duas partes e usa a seguinte fórmula abaixo para calcular o produto.

**A**l, **A**r, **B**l e **B**r são as partes dos números X e Y, que são divididos para facilitar a multiplicação. Para explicar melhor, digamos que X e Y são números grandes, e queremos dividi-los ao meio para realizar a multiplicação de forma mais eficiente.

Seja **X** e **Y** dois números a serem multiplicados, então:

1. **Divida** os números em duas partes:

   * X = Al \* 10^m + Ar
     * Onde Al é a **parte esquerda** de X e Ar é a **parte direita**.
     * **m** é a metade do número de dígitos de X, ou seja,m = [ ( dígitos de X ) / 2]
   * Y = Bl \* 10^m + Br
     * Onde Bl é a **parte esquerda** de Y e Br é a **parte direita**.
2. **Calcule três produtos menores**:

   * P = Al \* Bl (Multiplicação das partes esquerdas)
   * Q = Ar \* Br (Multiplicação das partes direitas)
   * R = (Al + Ar) \* (Bl + Br) - P - Q (Multiplicação cruzada das partes)
3. **Combine os resultados** para obter o produto final:

   * X \* Y = P \* 10^(2m) + R \* 10^m + Q

## Como executar o projeto

### Pré-requisitos

Este projeto requer **Python 3.x** e **Git** instalados, e ele **não exige a instalação de nenhuma dependência adicional**

### Rodando o código

1. Clone este repositório:
   ```sh
   git clone https://github.com/anacarv/Karatsuba_algorithm.git
   cd karatsuba
   ```
2. Execute o script:
   ```sh
   python main.py
   ```
3. Digite números inteiros quando solicitado e dê enter para ver o resultado da multiplicação usando o método de Karatsuba.

## Análise da Complexidade

### Complexidade Assintótica

A notação Big-O mede como o tempo de execução ou o uso de memória de um algoritmo cresce em relação ao tamanho da entrada. Ela ajuda a prever a escalabilidade do código.

* **Melhor caso:** O(n)
* **Caso médio:** O(n^(log₂3)) ou O(n^1.585)
* **Pior caso:** O(n^(log₂3)) ou O(n^1.585)

#### Diferença para a complexidade ciclomática:

* **Big-O:** Foca no tempo e espaço (eficiência).
* **Complexidade Ciclomática:** Foca no número de caminhos possíveis (fluxo de controle).

### Complexidade Ciclomática

A complexidade ciclomática é uma métrica usada para medir a complexidade do fluxo de controle de um programa. Ela calcula o número de caminhos independentes no código, considerando estruturas como loops (`for`, `while`) e condicionais (`if`, `try/except`). Quanto maior o valor, mais complexo é o código.

**Fórmula:**
( M = E - N + 2P )

Onde:

* (M): Complexidade Ciclomática
* (E): Número de arestas (transições) no grafo do controle de fluxo
* (N): Número de nós (blocos de código)
* (P): Componentes conectados (geralmente 1 para programas simples)

M = 7 - 5 + 2(1)

M = 7 − 5 + 2

M = 4

Para a implementação atual, a complexidade ciclomática do algoritmo de Karatsuba é **4**, devido às chamadas recursivas e condições presentes no código.

#### **Grafo de Fluxo**

![](https://diagrams.helpful.dev/d-r2/d-r2:XJWspkYG)

### Análise da Complexidade Ciclomática por Função

### Função: `findSum`

**Complexidade Ciclomática:** 3

- A complexidade ciclomática é 3 devido às três possíveis bifurcações: uma para a verificação da condição `if len(str1) > len(str2)`, uma no loop e outra para a verificação de `carry`.

### Função: `findDiff`

**Complexidade Ciclomática:** 3

- Similar à função `findSum`, a complexidade é 3 devido às bifurcações no loop (para verificar o valor de `sub`) e o tratamento do `carry`.

### Função: `removeLeadingZeros`

**Complexidade Ciclomática:** 2

- A função utiliza apenas uma operação de substituição regular e retorna a string, então possui uma complexidade ciclomática de 2.

### Função: `multiply`

**Complexidade Ciclomática:** 5

- A complexidade é 5 devido às bifurcações para verificar o tamanho dos números (len(A) < 10), o cálculo recursivo de `p`, `q` e `r`, e a combinação dos resultados. As chamadas recursivas geram maior complexidade.

## Estrutura do Código & Explicação das Funções

### Arquivo `main.py`

#### `findSum(str1, str2)`

Soma dois números grandes representados como strings, manipulando os dígitos de forma individual e considerando o transporte (carry).

#### `findDiff(str1, str2)`

Subtrai dois números grandes representados como strings, manipulando os dígitos individualmente e considerando o transporte (carry) negativo quando necessário.

#### `removeLeadingZeros(s)`

Remove os zeros à esquerda de uma string numérica.

#### `multiply(A, B)`

Multiplica dois números grandes representados como strings usando o algoritmo de Karatsuba. Se o tamanho dos números for menor que 10, utiliza multiplicação direta. Caso contrário, divide os números, calcula os produtos parciais e combina os resultados.

### Arquivo `functions.py`

Este arquivo contém exemplos de funções com diferentes complexidades:

- **findSum** (O(n)): Soma dois números grandes, onde n é o tamanho do número maior.
- **findDiff** (O(n)): Subtrai dois números grandes, onde n é o tamanho do número maior.
- **removeLeadingZeros** (O(n)): Remove os zeros à esquerda de uma string numérica.
- **multiply** (O(n^log₂3)): Multiplica dois números grandes usando o algoritmo de Karatsuba, onde n é o tamanho dos números.

## Exemplo de Entrada e Saída

```
Digite o primeiro número: 1456
Digite o segundo número: 6533
Resultado da multiplicação: 9512048
```
