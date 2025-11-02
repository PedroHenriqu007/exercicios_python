# Peça três números e mostre a média aritmética.

lista_numerica = []
restante = 3

for i in range(3):
    numeros = int(input(f"Digite três números ({restante - i} restantes.): "))
    lista_numerica.append(numeros)

quantidade_de_numeros = len(lista_numerica)

media = sum(lista_numerica) / quantidade_de_numeros

print("A média é: ", media)