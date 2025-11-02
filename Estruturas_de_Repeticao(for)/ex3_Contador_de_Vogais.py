# Peça uma palavra e conte quantas vogais há nela.

palavra = input("Digite uma palavra:")

vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

quant_de_vogais = 0

for i in palavra:
    if i in vogais:
        quant_de_vogais += 1

print(quant_de_vogais)