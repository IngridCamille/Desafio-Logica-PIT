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

## Questão 4
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

##Questão 4
