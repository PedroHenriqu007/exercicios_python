# Crie um programa onde o usuário digite uma expressão qualquer que use parêntese. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = input("Digite uma expressão: ")

caracteres = []
parenteses_abertos = 0
parenteses_fechados = 0

for caractere in expressao:
    if "(" in expressao and ")" in expressao:
        caracteres.append(caractere)

for i in caracteres:
    if i == "(":
        parenteses_abertos += 1
        
    if i == ")":
        parenteses_fechados += 1

if parenteses_abertos == parenteses_fechados and parenteses_abertos != 0 and parenteses_fechados != 0:
    print("Expressão válida!")
else:
    print("Sua expressão é inválida.")