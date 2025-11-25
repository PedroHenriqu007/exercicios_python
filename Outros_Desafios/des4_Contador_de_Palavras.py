"""Contador de Palavras - Crie um programa que recebe uma frase, e após isso calcula quantas palavras existem naquela frase(considerando que uma palavra é composta por no mínimo 2 palavras)"""

frase = input("Digite uma frase: ")

palavras = frase.split() # Cria uma lista separando as palavras por espaço.

quantidade_de_palavras = len(palavras) # Pega quantos itens tem na lista

for palavra in palavras: # Verifica se a palavra tem menos de 2 caracteres e "remove"
    if len(palavra) < 2:
        quantidade_de_palavras -= 1

print(f"A quantidade de palavras é: {quantidade_de_palavras}")