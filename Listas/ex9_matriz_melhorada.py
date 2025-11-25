# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
soma_terceira_coluna = 0
maior_valor = 0

for l in range(3):
    for c in range(3):
        numero = int(input("Digite um número: "))
        matriz[l][c] = numero
print("-=" * 30)
for l in range(3):
    soma_terceira_coluna += matriz[l][2]
    for c in range(3):
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        print(f"[{matriz[l][c]:^5}]", end=" ")
    print()
print("-=" * 30)
print(f"A soma total dos números pares é: {soma}")
print(f"A soma total dos números da terceira coluna é: {soma_terceira_coluna}")
print(f"O maior valor da segunda linha é: {max(matriz[1])}")