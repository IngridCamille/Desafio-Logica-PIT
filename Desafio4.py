# Questão 1
idade = [20, 24, 31, 44, 66, 66, 70, 80, 47, 50]
idade_ordenada = sorted(idade)
print(f"1a) Média: {sum(idade) / len(idade):.2f}")
print(f"1b) Mediana: {(idade_ordenada[4] + idade_ordenada[5]) / 2}")
print(f"1c) Moda: {idade_ordenada[4]}")

# Questão 2
bolas = ["vermelha", "azul", "verde", "vermelha", "amarela", "azul", "vermelha", "verde", "azul", "vermelha"]
print(f"2a) Total: {len(bolas)}")
print(f"2b) Vermelhas: {bolas.count('vermelha')}")
prob = bolas.count('vermelha') / len(bolas)
print(f"2c) Probabilidade: {prob}")
print(f"2d) Fração: {bolas.count('vermelha')}/{len(bolas)} | Porcentagem: {prob * 100:.0f}%")

# Questão 3
alunos = [
    ["Ana", 7.5, 8.0, 9.0],
    ["Bruno", 6.0, 5.5, 7.0],
    ["Carlos", 9.0, 8.5, 10.0],
    ["Daniela", 5.0, 6.0, 4.5],
    ["Eduardo", 8.0, 7.5, 6.5]
]

soma_geral = 0
aprovados = 0
reprovados = 0
maior_media = -1
menor_media = 11
aluno_maior = ""
aluno_menor = ""

print("RELATÓRIO DOS ALUNOS")

for aluno in alunos:
    nome = aluno[0]
    media = (aluno[1] + aluno[2] + aluno[3]) / 3
    soma_geral += media
    
    if media >= 7.0:
        status = "Aprovado"
        aprovados += 1
    else:
        status = "Reprovado"
        reprovados += 1

    print(f"a) Nome: {nome}")
    print(f"b) Média: {media:.2f}")
    print(f"c) Status: {status}")
    print("-" * 30)
    
    if media > maior_media:
        maior_media = media
        aluno_maior = nome
    
    if media < menor_media:
        menor_media = media
        aluno_menor = nome

media_geral_turma = soma_geral / len(alunos)

print(f"\nd) Média geral da turma: {media_geral_turma:.2f}")
print(f"e) Aluno com a maior média: {aluno_maior} ({maior_media:.2f})")
print(f"f) Aluno com a menor média: {aluno_menor} ({menor_media:.2f})")
print(f"g) Alunos aprovados: {aprovados}")
print(f"h) Alunos reprovados: {reprovados}")

# Questão 4
precos = [50, 80, 120, 35, 200, 75]
novos_precos = [preco * 1.10 for preco in precos]
print(f"4) Novos preços: {novos_precos}")

# Questão 5
def calcular_estacionamento(horas):
    if horas <= 1:
        return 5.00
    elif horas <= 3:
        return 10.00
    elif horas <= 5:
        return 15.00
    else:
        return 20.00

print(f"5) Valor estacionamento (2h): R$ {calcular_estacionamento(2):.2f}")

# Questão 6
def calcular_idade(ano_nascimento, ano_atual):
    idade_pessoa = ano_atual - ano_nascimento
    status = "maior de idade" if idade_pessoa >= 18 else "menor de idade"
    return idade_pessoa, status

print(f"6) Idade e status: {calcular_idade(2005, 2026)}")

# Questão 7
def area_triangulo(base, altura):
    return (base * altura) / 2

def area_trapezio(base_maior, base_menor, altura):
    return ((base_maior + base_menor) * altura) / 2

def area_losango(diagonal_maior, diagonal_menor):
    return (diagonal_maior * diagonal_menor) / 2

print(f"7) Triângulo: {area_triangulo(10, 5)} | Trapézio: {area_trapezio(8, 4, 5)} | Losango: {area_losango(6, 4)}")

# Questão 8
def verificar_senha(senha):
    tem_tamanho = len(senha) >= 8
    tem_numero = any(char.isdigit() for char in senha)
    return tem_tamanho and tem_numero

print(f"8) Senha válida (Senha123): {verificar_senha('Senha123')}")
print(f"8) Senha válida (abc): {verificar_senha('abc')}")
