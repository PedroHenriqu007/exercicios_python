# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(texto_qualquer):
    print("-" * len(texto_qualquer))
    print(texto_qualquer)
    print("-" * len(texto_qualquer))


txt = input("Digite um texto: ")
escreva(txt)