# Adivinhação de Número
# - Crie um programa que gera um número aleatório,
# recebe um número do usuário e permite que o usuário chute o número até ele acertar (sempre
# dando feedback caso ele tenha acertado ou não)

import random

numero_aleatorio = random.randint(1, 100)

while True:
    
    numero_do_usuario = int(input("Tente adivinhar o número: "))

    if numero_do_usuario == numero_aleatorio:
        print("Você acertou!")
        break
    else:
        print("Que pena, você errou...")