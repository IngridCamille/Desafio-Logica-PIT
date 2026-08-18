# Desafio-Logica-PIT

### 1. Verificador de Par ou Ímpar
```python
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")
```

### 2. Classificador de Idade
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

### 3. Mini Calculadora
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

### 4. Classificador de Triângulos
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

### 5. Equação do 2º Grau
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

### 6. Estado Físico da Água
```python
temp = float(input("Digite a temperatura da água (°C): "))

if temp <= 0:
    print("Estado físico: Sólido")
elif temp < 100:
    print("Estado físico: Líquido")
else:
    print("Estado físico: Gasoso")
```

### 7. Comissão do Corretor
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

### 8. Fechamento de Conta de Hotel
```python
nome_hospede = input("Digite o nome do hóspede: ")
dias = int(input("Digite a quantidade de diárias: "))

taxa = 6.50 if dias > 7 else (12.00 if dias == 7 else 16.50)

print(f"Hóspede: {nome_hospede} | Total: R$ {dias * (290.00 + taxa):,.2f}")
```
