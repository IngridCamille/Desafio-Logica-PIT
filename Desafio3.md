# 🐍 Desafio Prático e Analítico: Lógica, Algoritmos e Programação

---

## 📌 Questão 1

### Código Original
```python
numeros = [0, 0, 0, 0, 0]
x = 0
while x < 5:
    numeros[x] = float(input("Digite um número qualquer:"))
    x += 1
y = 0
while y < 5:
    print(f"{numeros[y]}")
    y += 1
```

---

### a) Refaça o código utilizando a estrutura FOR

```python
numeros = [0, 0, 0, 0, 0]

for x in range(5):
    numeros[x] = float(input("Digite um número qualquer: "))

for y in range(5):
    print(f"{numeros[y]}")
```

---

### b) O que acontece se colocarmos `while x <= 4:`? Justifique.
Vai funcionar do mesmo jeito! Como a lista só tem 5 posições (que vão do índice 0 ao 4), a condição `x <= 4` vai rodar exatamente para os valores 0, 1, 2, 3 e 4 — ou seja, faz as mesmas 5 repetições que o `x < 5` fazia.

---

### c) Esse código funcionaria caso quiséssemos inserir mais de 5 elementos? Justifique.
**Não roda.** A lista foi criada travada em 5 espaços com zeros (`[0, 0, 0, 0, 0]`). Se tentar guardar algo na posição 5 ou acima, o Python vai dar erro de `IndexError` dizendo que a posição não existe.

---

### d) Qual a problemática da alternativa anterior (c) para a realidade dos códigos?
O código fica engessado (*hardcoded*). Na vida real, a gente raramente sabe quantos dados o usuário vai digitar. Deixar o tamanho fixo obriga você a mudar o código na mão toda vez que precisar de mais espaço. O certo em Python é começar com uma lista vazia `[]` e ir usando o `.append()` pra colocar as coisas conforme precisar.

---

### e) Refaça o código melhorando os problemas encontrados na alternativa (c e d)

```python
numeros = []

quantidade = int(input("Quantos números você quer digitar? "))

for i in range(quantidade):
    num = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(num)

print("\nNúmeros que você digitou:")
for num in numeros:
    print(num)
```

---

## 📌 Questão 2

### Código Original
```python
L = [1, 2, 3]
x = 0
while x < 3:
    print(L[x])
    x += 1
```

---

### a) Qual a saída final da variável x?
O valor final de `x` vai ser **`3`**. Ele imprime o elemento do índice 2, soma +1 (virando 3) e aí o laço para porque 3 não é menor que 3.

---

### b) Podemos considerar o resultado final da variável x como o tamanho da lista? Justifique.
**Sim!** Como o `x` começa em 0 e vai somando de 1 em 1 a cada item percorrido, o valor que sobra no `x` no final (3) é exatamente a quantidade de itens que a lista tem (`len(L)`).

---

### c) O que aconteceria se atualizarmos a lista para `L = [7, 8, 9, 10, 11, 12]`? Justifique.
Ele só vai mostrar os **3 primeiros números (`7, 8, 9`)**. Isso acontece porque a trava do `while` continuou como `x < 3`, então ele ignora o resto da lista.

---

### d) Reescreva o código para que o mesmo possa funcionar para qualquer lista L

```python
L = [7, 8, 9, 10, 11, 12]
x = 0

while x < len(L):
    print(L[x])
    x += 1
```

---

## 📌 Questão 3

Faça um programa que leia duas listas, A e B, e que gere uma terceira com os elementos das duas primeiras.

```python
A = ['mouse', 'teclado', 'monitor', 'estabilizador']
B = ['memória', 'cpu', 'ssd', 'chipset', 'rom']

C = A + B

print("Lista juntas (C):", C)
```

---

## 📌 Questão 4

Faça um programa que percorra duas listas, A e B, e gere uma terceira sem elementos repetidos.

```python
A = ['Python', 'Java', 'C', 'PHP', 'JavaScript', 'Dart']
B = ['C++', 'Python', 'Java', 'Julia', 'Go', 'JavaScript']

C = []

for item in A + B:
    if item not in C:
        C.append(item)

print("Lista sem repetidos (C):", C)
```

---

## 📌 Questão 5

### Código Original
```python
L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar:"))
achou = False
x = 0
while x < len(L):
    if L[x] == p:
        achou = True
        break
    x += 1
if achou:
    print(f"{p} achado na posição {x}")
else:
    print(f"{p} não encontrado")
```

---

### a) Explique a função das linhas 20, 24, 25 e 27
* **Linha 20 (`achou = False`):** É um aviso (uma "chave") que começa desligado para dizer que o número ainda não foi achado.
* **Linha 24 (`achou = True`):** Liga a "chave", confirmando que encontrou o número na lista.
* **Linha 25 (`break`):** Manda a busca parar na hora, sem gastar tempo procurando o resto se já achou o que queria.
* **Linha 27 (`if achou:`):** Checa se a chave ficou ligada no final para decidir qual mensagem mostrar na tela.

---

### b) Refaça o código de forma a realizar a mesma tarefa, mas sem utilizar a variável achou

```python
L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))

x = 0
while x < len(L):
    if L[x] == p:
        print(f"{p} achado na posição {x}")
        break
    x += 1
else:
    print(f"{p} não encontrado")
```

---

## 📌 Questão 6

### Código Original
```python
L = []
while True:
    x = 0
    n = int(input("Digite um número ou 0 para sair:"))
    if n == 0:
        break
    L.append(n)
    while x < len(L):
        print(L[x])
        x = x + 1
```

---

### a) Modifique o código usando a estrutura FOR para as duas repetições

```python
from itertools import count

L = []

for _ in count():
    n = int(input("Digite um número ou 0 para sair: "))
    if n == 0:
        break
    L.append(n)
    for x in range(len(L)):
        print(L[x])
```

---

### b) A alternativa anterior teve êxito? Justifique.
**Mais ou menos.** O laço de dentro pra imprimir a lista fica bem melhor com `for`. Mas o laço de fora pra pedir números precisa continuar rodando até a pessoa digitar 0, sem um limite fixo. Se colocar um `for range()` normal de tamanho fixo no laço de fora, o programa para de pedir números antes do tempo se o usuário digitar mais coisas.

---

## 📌 Questão 7

### Código Base
```python
T = [-10, -8, 0, 1, 2, 20, -2, -4]
```

---

### a) Um código para descobrir o maior número da lista

```python
T = [-10, -8, 0, 1, 2, 20, -2, -4]

maior = T[0]

for i in range(1, len(T)):
    if T[i] > maior:
        maior = T[i]

print(f"O maior número é: {maior}")
```

---

### b) Um código para descobrir o menor número da lista

```python
T = [-10, -8, 0, 1, 2, 20, -2, -4]

menor = T[0]

for i in range(1, len(T)):
    if T[i] < menor:
        menor = T[i]

print(f"O menor número é: {menor}")
```

---

### c) Um código para mostrar endereço e elemento na lista

```python
T = [-10, -8, 0, 1, 2, 20, -2, -4]

for i in range(len(T)):
    print(f"Posição {i} -> Elemento: {T[i]}")
```

---

## 📌 Questão 8

Escreva um código que receba números ou palavras. O código deve armazenar cada situação em listas diferentes, ou seja, uma lista só para as palavras e outra só para os números. O programa deve encerrar quando o usuário digitar o `x` ou `X`. No fim, mostre o que foi inserido nas duas listas, a quantidade total de coisas digitadas pelo usuário.

```python
palavras = []
numeros = []

while True:
    entrada = input("Digite algo (ou 'x'/'X' para sair): ").strip()

    if entrada.lower() == 'x':
        break

    if entrada.replace('.', '', 1).isdigit() or (entrada.startswith('-') and entrada[1:].replace('.', '', 1).isdigit()):
        if '.' in entrada:
            numeros.append(float(entrada))
        else:
            numeros.append(int(entrada))
    else:
        palavras.append(entrada)

total = len(palavras) + len(numeros)

print("\n--- RESULTADO ---")
print(f"Palavras: {palavras}")
print(f"Números: {numeros}")
print(f"Total de itens digitados: {total}")
```
