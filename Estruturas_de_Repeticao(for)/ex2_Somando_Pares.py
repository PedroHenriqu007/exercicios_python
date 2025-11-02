# Some todos os números pares de 1 a 50 e exiba o resultado

soma = 0

for i in range(1, 51):
    if(i % 2 == 0):
        soma += i
        print("O resultado é:", soma)