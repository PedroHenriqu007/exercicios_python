# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

valores = []

for i in range(5):
    numero = int(input("Digite um valor: "))
    if not valores:
        valores.append(numero)
        print("Adicionado ao final da lista...")
    else:
        for posicao, valor in enumerate(valores):
            if valor > numero:
                valores.insert(posicao, numero)
                print(f"Adicionado na posição {posicao} da lista...")
                break
        else:
            valores.append(numero)
            print("Adicionado ao final da lista...")

print("-=" * 30)
print(f"Os valores digitados em ordem foram: {valores}")
    