# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realiza a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada

from time import sleep

def contador(inicio, fim, passo):
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    if passo == 0:
        passo = 1
    if inicio < fim:
        for i in range(inicio, fim+1, passo):
            print(i, end=" ", flush=True)
            sleep(0.5)
        print("FIM!")
    elif inicio > fim and passo > 0 and fim != 0:
        for i in range(inicio, fim-1, -passo):
            print(i, end=" ", flush=True)
            sleep(0.5)
        print("FIM!")
    else:
        for i in range(inicio, fim-1, passo):
            print(i, end=" ", flush=True)
            sleep(0.5)
        print("FIM!")
    print("-=" * 30)

print("-=" * 30)
contador(1, 10, 1)
contador(10, 0, -2)
print("Agora é sua vez de personalizar a contagem!")
n1 = int(input("Início: "))
n2 = int(input("Fim: "))
n3 = int(input("Passo: "))

contador(n1, n2, n3)