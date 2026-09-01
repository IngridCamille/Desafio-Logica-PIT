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
Supondo que a população de um país A seja da ordem de 90.000 habitantes com uma taxa anual de crescimento de 5% e que a população de B seja 200.000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. 

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
Resumo estatístico de notas de um curso. Leia as notas de uma turma até que o usuário digite algo para sair. Para cada nota válida, determine se o estudante foi aprovado, ficou em recuperação ou foi reprovado. Considere aprovado para nota maior ou igual a 7,0, recuperação para nota entre 5,0 e 6,9, e reprovação para nota inferior a 5,0. Ao final, apresente a média da turma, a maior nota, a menor nota, o percentual de aprovação e a situação geral da turma. Classifique a turma como “desempenho satisfatório” quando o percentual de aprovação for igual ou superior a 70%. Requisitos: utilizar while; aceitar notas entre 0 e 10; não encerrar a leitura ao receber um valor inválido; impedir divisão por zero; utilizar decisões para a situação individual e para a classificação geral. 

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

Seleção de atributos para um modelo. Um conjunto de dados possui n atributos disponíveis. O analista deseja selecionar r atributos para uma etapa de modelagem, sem considerar a ordem de seleção. Calcule o número de subconjuntos possíveis usando: C(n, r) = n! / (r! * (n-r)!) O programa deve validar 0 <= r <= n e informar se a quantidade de subconjuntos é compatível com uma busca exaustiva. Considere viável a busca quando houver até 10.000 combinações. Requisitos: calcular o resultado sem função pronta de fatorial; utilizar repetição; aplicar decisões para validar os parâmetros e classificar a viabilidade; explicar por que a ordem dos atributos não altera uma combinação. 

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

Uma população inicial de 2727 indivíduos cresce a uma taxa de 4% ao ano. Escreva um programa em Python que simule o crescimento dessa população e mostre o tamanho da população ao final de cada ano, durante 5 anos

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

Probabilidade experimental. Um experimento consiste em lançar um dado 20 vezes. O programa recebe o resultado de cada lançamento e deve contar quantas vezes apareceu um número par. Ao final, deve calcular a probabilidade experimental de obter um número par. 

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
