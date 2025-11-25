# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionada. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = []

while True:
    num = int(input("Digite um valor: "))
    
    if num in numeros:
        print("Valor duplicado! Não vou adicionar.")
    else:
        numeros.append(num)
        print("Valor adicionado com sucesso...")
    
    while True:
        continuar = input("Deseja continuar? [S/N] ").upper().strip()
    
        if continuar == "S" or continuar == "N":
            break
        else:
            print("Por favor, digite somente S ou N.")
    if continuar == "N":
        break
    

print(sorted(numeros))