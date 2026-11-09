import random
import math
import re

# Questão 4: Módulo de Validação de Senhas
def verificar_senha(senha):
    criterios_atendidos = True
    mensagens = []
    
    if len(senha) < 8:
        criterios_atendidos = False
        mensagens.append("- A senha deve ter pelo menos 8 caracteres.")
        
    if not re.search(r'[A-Z]', senha):
        criterios_atendidos = False
        mensagens.append("- A senha deve conter pelo menos uma letra maiúscula.")
        
    if not re.search(r'\d', senha):
        criterios_atendidos = False
        mensagens.append("- A senha deve conter pelo menos um número.")
        
    if criterios_atendidos:
        print("Senha aprovada nos critérios de segurança da empresa!")
        return True
    else:
        print("Critérios não seguidos:")
        for msg in mensagens:
            print(msg)
        return False

# Questão 1: Jogo de Adivinhação
def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    palpites = []
    
    print("--- Jogo de Adivinhação (1 a 100) ---")
    
    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
            continue
            
        palpites.append(palpite)
        
        if palpite == numero_secreto:
            print("Parabéns! Você acertou!")
            print(f"Números digitados: {palpites}")
            print(f"Quantidade de tentativas: {len(palpites)}")
            break
        elif palpite < numero_secreto:
            print("Errou! O número a ser descoberto é MAIOR.")
        else:
            print("Errou! O número a ser descoberto é MENOR.")

# Questão 2: Áreas de Figuras Planas
def area_retangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_quadrado(lado):
    return lado ** 2

def area_trapezio(base_maior, base_menor, altura):
    return ((base_maior + base_menor) * altura) / 2

def area_circulo(raio):
    return math.pi * (raio ** 2)

def area_losango(diagonal_maior, diagonal_menor):
    return (diagonal_maior * diagonal_menor) / 2

def calculadora_areas():
    print("\n--- Calculadora de Áreas de Figuras Planas ---")
    print("1. Retângulo")
    print("2. Triângulo")
    print("3. Quadrado")
    print("4. Trapézio")
    print("5. Círculo")
    print("6. Losango")
    
    opcao = input("Escolha a figura (1-6): ")
    
    if opcao == '1':
        b = float(input("Digite a base: "))
        h = float(input("Digite a altura: "))
        print(f"Área do Retângulo: {area_retangulo(b, h):.2f}")
    elif opcao == '2':
        b = float(input("Digite a base: "))
        h = float(input("Digite a altura: "))
        print(f"Área do Triângulo: {area_triangulo(b, h):.2f}")
    elif opcao == '3':
        l = float(input("Digite o lado: "))
        print(f"Área do Quadrado: {area_quadrado(l):.2f}")
    elif opcao == '4':
        B = float(input("Digite a base maior: "))
        b = float(input("Digite a base menor: "))
        h = float(input("Digite a altura: "))
        print(f"Área do Trapézio: {area_trapezio(B, b, h):.2f}")
    elif opcao == '5':
        r = float(input("Digite o raio: "))
        print(f"Área do Círculo: {area_circulo(r):.2f}")
    elif opcao == '6':
        D = float(input("Digite a diagonal maior: "))
        d = float(input("Digite a diagonal menor: "))
        print(f"Área do Losango: {area_losango(D, d):.2f}")
    else:
        print("Opção inválida.")

# Questão 3: Equação do 2º Grau
def calcular_equacao_segundo_grau(a, b, c):
    if a == 0:
        print("O coeficiente 'a' deve ser diferente de zero para uma equação do 2º grau.")
        return
        
    delta = (b ** 2) - (4 * a * c)
    print(f"Valor do Delta (Δ): {delta:.2f}")
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("A equação possui duas raízes reais distintas:")
        print(f"x1 = {x1:.2f}")
        print(f"x2 = {x2:.2f}")
    elif delta == 0:
        x = -b / (2 * a)
        print("A equação possui uma raiz real (ou duas raízes reais iguais):")
        print(f"x = {x:.2f}")
    else:
        print("A equação não possui raízes reais (duas raízes complexas).")

# Questão 4: Teste do Validador de Senhas
def testar_senha():
    senha_usuario = input("Digite a senha para verificação: ")
    verificar_senha(senha_usuario)

# Execução Principal (Menu do Trabalho)
if __name__ == "__main__":
    print(" DESAFIO PRÁTICO ")
    print("1. Jogo de Adivinhação")
    print("2. Calculadora de Áreas")
    print("3. Equação do 2º Grau")
    print("4. Validador de Senhas")
    
    escolha = input("\nEscolha qual questão executar (1-4): ")
    
    if escolha == '1':
        jogo_adivinhacao()
    elif escolha == '2':
        calculadora_areas()
    elif escolha == '3':
        a = float(input("Digite o coeficiente a: "))
        b = float(input("Digite o coeficiente b: "))
        c = float(input("Digite o coeficiente c: "))
        calcular_equacao_segundo_grau(a, b, c)
    elif escolha == '4':
        testar_senha()
    else:
        print("Opção inválida.")
