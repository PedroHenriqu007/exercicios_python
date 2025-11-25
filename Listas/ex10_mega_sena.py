# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from time import sleep
import random

lista_de_numeros = []

print("-" * 28)
print("     JOGA NA MEGA SENA     ")
print("-" * 28)

jogos = int(input("Quantos jogos você quer que eu sorteie? "))
print("-=" * 3, end= " ")
print(f"SORTEANDO {jogos} JOGOS", end=" ")
print("-=" * 3)

while len(lista_de_numeros) != jogos:
    numeros = []
    for i in range(6):
        numero = random.randint(1, 60)
        if numero not in numeros:
            numeros.append(numero)
        elif numero in numeros:
            while numero in numeros:
                numero = random.randint(1, 60)
                if numero not in numeros:
                    numeros.append(numero)
                    break
                
    lista_de_numeros.append(numeros)
    
for k, v in enumerate(lista_de_numeros):
    print(f"Jogo {k+1}: {v}", flush=True)
    sleep(0.75)

print("-=" * 5, "< BOA SORTE! >", "-=" * 5)