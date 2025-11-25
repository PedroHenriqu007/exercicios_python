# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final mostre a matriz na tela, com a formatação correta.

matriz = [
    [
        0, 0, 0
    ],
    [
        0, 0, 0
    ],
    [
        0, 0, 0
    ]
]

for posicao, valor in enumerate(matriz):
    for pos, numero in enumerate(valor):
       num = int(input(f"Digite um valor para {posicao, pos}: "))
       matriz[posicao][pos] = num

print("-=" * 30)
for posicao, valor in enumerate(matriz):
    for pos, numero in enumerate(valor):
        print(f"[  {matriz[posicao][pos]:^5}  ]", end=" ")
    print()