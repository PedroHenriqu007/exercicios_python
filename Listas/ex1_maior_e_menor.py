# Faça um programa que leia 5 valores númericos e guarda-os numa lista. No final, mostra qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista_numerica = []
posicoes_maior = []
posicoes_menor = []

for i in range(5):
    numero = int(input(f"Digite um valor para a posição {i}: "))
    lista_numerica.append(numero)

maior_numero = max(lista_numerica)
menor_numero = min(lista_numerica)

for posicao, num in enumerate(lista_numerica):
    if num == maior_numero:
        posicoes_maior.append(posicao)
    
    if num == menor_numero:
        posicoes_menor.append(posicao)

print("=" * 30)
print(f"O maior valor é: {maior_numero}, nas posições: {posicoes_maior}")
print(f"O menor valor é: {menor_numero}, nas posições: {posicoes_menor}")