# Peça 5 nomes e exiba-os em ordem alfabética.
"""
nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")
nome3 = input("Digite o terceiro nome")
nome4 = input("Digite o quarto nome: ")
nome5 = input("Digite o quinto nome: ")

lista_de_nomes = [nome1, nome2, nome3, nome4, nome5]

print(sorted(lista_de_nomes))"""

total_de_perguntas = 5

lista_de_nomes = []

for i in range(total_de_perguntas):
    nomes = input(f"Digite 5 nomes ({total_de_perguntas - i} restantes.): ")
    lista_de_nomes.append(nomes)

print(sorted(lista_de_nomes))