# Crie um programa que:
# 1. Peça ao usuário que digite 5 números inteiros, um por vez.
# 2. Armazene todos esses números em uma lista.
# 3. Depois que a lista estiver completa, o programa deve:
# Mostrar todos os números digitados;
# Exibir quantos deles são maiores que 10;
# Mostrar apenas os números na ordem inversa (do último para o primeiro).

numeros = []
maiores_que_10 = 0

for i in range(5):
    numero = int(input(f"Digite um número para a posição {i}: "))
    if numero > 10:
        maiores_que_10 += 1
    numeros.append(numero)

print(f"Os números digitados foram: {numeros}")
print(f"A quantidade de números maiores que 10 é: {maiores_que_10}")
print(f"A ordem inversa dos números é: {numeros[::-1]}")