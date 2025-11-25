# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

numeros = []

while True:
    num = int(input("Digite um número: "))
    numeros.append(num)
    
    r = input("Deseja continuar? [S/N] ").strip().upper()
    if r == "N":
        break

print(f"O total de números digitados foram: {len(numeros)}")
print(f"A lista de valores é: {sorted(numeros, reverse=True)}")
if 5 in numeros:
    print("5 está na lista.")
else:
    print("Não encontrei o número 5.")