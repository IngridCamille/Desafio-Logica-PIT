# Desafio-Logica-PIT

### 1. Verificador de Par ou Ímpar. Peça ao usuário um número inteiro e diga se ele 
é par ou ímpar.
```python
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")
```

### 2. Classificador de Idade. Solicite a idade de uma pessoa. Classifique-a como 
"Criança" (0-12 anos), "Adolescente" (13-17 anos), "Adulto" (18-64 anos) ou "Idoso" 
(65 anos ou mais).
```python
idade = int(input("Qual a sua idade? "))

if idade <= 12:
    print(f"Você é criança, sua idade é {idade}")
elif 13 <= idade <= 17:
    print(f"Você é adolescente, sua idade é {idade}")
elif 18 <= idade <= 64:
    print(f"Você é adulto, sua idade é {idade}")
else:
    print(f"Você é idoso, sua idade é {idade}")
```

### 3. Mini Calculadora. Crie uma mini calculadora que permita ao usuário escolher 
entre as operações de soma, subtração, multiplicação e divisão. Peça dois 
números e a operação desejada. Imprima o resultado.
```python
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Escolha a operação (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
    print(f"Resultado: {resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"Resultado: {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"Resultado: {resultado}")
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {resultado}")
    else:
        print("Erro: Não é possível dividir por zero!")
else:
    print("Operação inválida!")
```

### 4. Classificador de Triângulos. Peça ao usuário para digitar o comprimento de 
três lados de um triângulo. Determine se os lados formam um triângulo válido 
e, em caso afirmativo, classifique-o como Equilátero, Isósceles ou Escaleno. 
Regras: 
a) Para ser um triângulo, a soma de dois lados deve ser maior que o terceiro 
lado (a + b > c, a + c > b, b + c > a). 
b) Equilátero: Todos os três lados são iguais. 
c) Isósceles: Dois lados são iguais. 
d) Escaleno: Todos os três lados são diferentes.
```python
a = float(input("Digite o comprimento do lado A: "))
b = float(input("Digite o comprimento do lado B: "))
c = float(input("Digite o comprimento do lado C: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Os lados formam um triângulo EQUILÁTERO.")
    elif a == b or a == c or b == c:
        print("Os lados formam um triângulo ISÓSCELES.")
    else:
        print("Os lados formam um triângulo ESCALENO.")
else:
    print("Os lados digitados NÃO formam um triângulo válido.")
```

### 5. Solicite os coeficientes a, b e c de uma equação do segundo grau (ax² + bx + c 
= 0). Determine e mostre o número de raízes reais distintas que a equação 
possui. Regra: O número de raízes reais depende do discriminante (delta), 
Δ = b² - 4ac: 
• Δ > 0: Duas raízes reais distintas. 
• Δ = 0: Uma raiz real (ou duas raízes reais iguais). 
• Δ < 0: Nenhuma raiz real (duas raízes complexas).
```python
a = float(input("Digite o valor do coeficiente a: "))
b = float(input("Digite o valor do coeficiente b: "))
c = float(input("Digite o valor do coeficiente c: "))

delta = (b ** 2) - (4 * a * c)

if delta > 0:
    print(f"Delta = {delta}. A equação possui duas raízes reais distintas.")
elif delta == 0:
    print(f"Delta = {delta}. A equação possui uma raiz real (duas raízes iguais).")
else:
    print(f"Delta = {delta}. A equação não possui raízes reais (duas raízes complexas).")
```

### 6. Peça ao usuário a temperatura da água (em graus Celsius). Determine o 
estado físico da água (sólido, líquido ou gasoso). Regras:
• Temperatura <= 0°C: Sólido 
• 0°C < Temperatura < 100°C: Líquido 
• Temperatura >= 100°C: Gasoso
```python
temp = float(input("Digite a temperatura da água (°C): "))

if temp <= 0:
    print("Estado físico: Sólido")
elif temp < 100:
    print("Estado físico: Líquido")
else:
    print("Estado físico: Gasoso")
```

### 7. Uma empresa de vendas possui corretores. A empresa paga ao corretor uma 
comissão calculada de acordo com o valor de suas vendas. Se o valor da venda 
de um corretor for até R$ 500.000 a comissão será de 6% do valor vendido. Se o 
valor da venda do corretor estiver acima de R$ 500.000 até R$ 700.000 a 
comissão será de 8.5%. Se o valor da venda do corretor estiver acima de R$ 
700.000 até R$ 1.000.000 a comissão será de 10%. Se o valor da venda de um 
corretor for maior que R$ 1.000.000 a comissão será de 12% do valor vendido. 
Escreva um código que imprima um relatório contendo o nome, valor da venda 
e a comissão do corretor.
```python
nome_corretor = input("Digite o nome do corretor: ")
venda = float(input("Digite o valor total da venda (R$): "))

if venda <= 500000:
    taxa = 0.06
elif venda <= 700000:
    taxa = 0.085
elif venda <= 1000000:
    taxa = 0.10
else:
    taxa = 0.12

print(f"Corretor: {nome_corretor} | Comissão: R$ {venda * taxa:,.2f}")
```

### 8. Ajude um hotel da cidade a calcular o valor da hospedagem. O hotel cobra R$ 
290,00 a diária e mais uma taxa de serviços. A taxa de serviços é de: 
• R$ 6,50 por dia, se o número de diárias for maior que 7; 
• R$ 12,00 por dia, se o número de diárias for igual a 7; 
• R$ 16,50 por diária, se o número de diárias for menor que 7. 
Você deve pedir a informação de quantos dias o hóspede ficou hospedado. 
Construa um código que mostre o nome do hóspede e o total da conta a pagar.
```python
nome_hospede = input("Digite o nome do hóspede: ")
dias = int(input("Digite a quantidade de diárias: "))

taxa = 6.50 if dias > 7 else (12.00 if dias == 7 else 16.50)

print(f"Hóspede: {nome_hospede} | Total: R$ {dias * (290.00 + taxa):,.2f}")
```
