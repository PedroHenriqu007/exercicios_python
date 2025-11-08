""" Calculadora Simples
Crie uma calculadora que realiza operações entre
dois números, o usuário deve ser capaz de informar um número, na
sequência informar qual operação deseja realizar e após isso ser capaz
de informar o segundo número"""

print("BEM-VINDO A CALCULADORA")
print("==============================================")
print("==============================================")

n1 = int(input("Digite um número: "))
operacao = (input("Digite qual operação deseja realizar (+, -, *, /): "))
n2 = int(input("Digite o segundo número: "))

if operacao == "+":
    print(f"{n1} + {n2} = {n1 + n2}")
elif operacao == "-":
    print(f"{n1} - {n2} = {n1 - n2}")
elif operacao == "*":
    print(f"{n1} * {n2} = {n1 * n2}")
elif operacao == "/":
    print(f"{n1} / {n2} = {n1 / n2}")