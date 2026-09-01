 # Desafio Prático 2

---

## Questão 1
Utilizando uma estrutura de repetição, escreva um programa em Python que calcule o fatorial de um número informado pelo usuário.

```python
num = int(input("Insira um número: "))
fatorial = 1 

for i in range(num, 1, -1):
    fatorial *= i

print(f"O fatorial de {num} é {fatorial}")
```

---

## Questão 2
Supondo que a população de um país A seja da ordem de 90.000 habitantes com uma taxa anual de crescimento de 5% e que a população de B seja 200.000 habitantes com uma taxa de crescimento de 1.5%.

```python
pais_a = 90000
pais_b = 200000
anos = 0

while pais_a < pais_b:
    pais_a += pais_a * 0.05
    pais_b += pais_b * 0.015
    anos += 1

print(f"Serão necessários {anos} anos.")
```
---

## Questão 3
Resumo Estatístico de Notas

```python
soma_notas = 0
total_alunos = 0

entrada = input("Digite a nota do aluno (ou 'sair' para encerrar): ")

while entrada != "sair":
    nota = float(entrada)
    
    if nota >= 7.0:
        print("Situação: Aprovado")
    elif nota >= 5.0:
        print("Situação: Recuperação")
    else:
        print("Situação: Reprovado")
        
    soma_notas += nota
    total_alunos += 1
    
    entrada = input("Digite a próxima nota (ou 'sair' para encerrar): ")

if total_alunos > 0:
    media = soma_notas / total_alunos
    print(f" Média da turma: {media:.2f}")
```
---

---

## Questão 4 - Seleção de Atributos e Combinatória

Escreva um programa que leia o total de atributos disponíveis (n) e quantos serão selecionados (r), calculando o número de subconjuntos possíveis e verificando a viabilidade de uma busca exaustiva.

```python
n = int(input("Digite o total de atributos (n): "))
r = int(input("Digite quantos vai selecionar (r): "))

if 0 <= r <= n:
    fat_n = 1
    for i in range(1, n + 1):
        fat_n *= i

    fat_r = 1
    for i in range(1, r + 1):
        fat_r *= i

    fat_nr = 1
    for i in range(1, (n - r) + 1):
        fat_nr *= i

    combinacoes = fat_n // (fat_r * fat_nr)

    print(f"Combinações possíveis: {combinacoes}")

    if combinacoes <= 10000:
        print("Viabilidade: Busca exaustiva é VIÁVEL")
    else:
        print("Viabilidade: Busca exaustiva é INVIÁVEL")
else:
    print("Erro: 'r' deve estar entre 0 e 'n'.")
```

---


## Questão 5 - Simulação de Crescimento Populacional

Escreva um programa que simule o crescimento de uma população de 2.727 indivíduos ao longo de 5 anos, considerando uma taxa constante de 4% ao ano.

```python
populacao = 2727
taxa = 0.04

print(f"População inicial: {populacao} indivíduos")

for ano in range(1, 6):
    populacao += populacao * taxa
    print(f"Ano {ano}: {int(populacao)} indivíduos")

 ```
---

## Questão 6 - Probabilidade Experimental de Dados

Escreva um programa que simule ou receba o resultado de 20 lançamentos de um dado de 6 faces, determinando a contagem de números pares obtidos e calculando a probabilidade experimental.

```python
total_lancamentos = 20
pares = 0

print("Digite os 20 resultados do dado (de 1 a 6):")

for i in range(1, total_lancamentos + 1):
    dado = int(input(f"Lançamento {i}: "))
    
    if dado % 2 == 0:
        pares += 1

probabilidade = (pares / total_lancamentos) * 100

print(f"Total de pares: {pares}")
print(f"Probabilidade experimental)
```
