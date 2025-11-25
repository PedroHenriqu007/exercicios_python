# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area():
    largura = float(input("Digite a largura: "))
    comprimento = float(input("Digite o comprimento: "))
    area = largura * comprimento
    print("-" * 30)
    print(f"A área do terreno é: {area}")
    print("-" * 30)


area()