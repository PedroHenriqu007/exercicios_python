# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves

pessoas = []
pesos = []
mais_pesados = []
mais_leves = []

while True:
    pessoa = []
    nome = input("Digite o nome da pessoa: ")
    peso = float(input("Digite o seu peso: "))
    pessoa.append(nome)
    pessoa.append(peso)
    pessoas.append(pessoa)
    
    continuar = input("Adicionado com sucesso. Deseja continuar? [S/N] ").strip().upper()
    if continuar == "N":
        break  

for p in pessoas:
    for i in p:
        if isinstance(i, float):
            pesos.append(i)
            
    # if p[1] == max(pesos):
    #     mais_pesados.append(p[0])

for j in pessoas:
    if j[1] == max(pesos):
        mais_pesados.append(j[0])
        
    if j[1] == min(pesos):
        mais_leves.append(j[0])
        
print("-=" * 30)
print(f"O total de pessoas cadastradas foi: {len(pessoas)}")
print(f"O maior peso foi {max(pesos)}kg. Peso de {mais_pesados}")
print(f"O menor peso foi de {min(pesos)}kg. Peso de {mais_leves}")
