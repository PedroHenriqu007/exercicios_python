# Leia vários números e some-os. O programa para quando o usuário digitar 0, e mostra a soma final.

soma_total = 0

while True:
    numero = int(input("Digite um número: "))
    
    soma_total += numero
    if(numero == 0):
        print(soma_total)
        break