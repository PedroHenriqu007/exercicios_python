# Leia um número e diga se ele é positivo, negativo ou zero.

numero = int(input("Digite um número: "))

if(numero > 0):
    print("Número positivo.")
elif(numero < 0):
    print("Número negativo.")
else:
    print("Número zero.")