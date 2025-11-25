#1. Iterador básico com next()
# Explique como você criaria um iterador a partir de uma lista e como usaria a função next() para acessar manualmente os primeiros três elementos dessa lista. Descreva também o que acontece quando você tenta chamar next() mais vezes do que há elementos.

"""
Primeiro eu criaria uma variável e usaria a função iter() para converter a listar para o tipo List Iterator e armazenar nessa variável. Depois, chamaria a função next() passando como parâmetro a nova variável List Iterator que criei e, dessa forma, pegaria o primeiro elemento da lista. Para pegar os três, seria necessário apenas chamar next() mais duas vezes e passar a mesma variável como parâmetro.

Quando você tenta chamar next() mais vezes do que há elementos na lista, ocorre um erro de Stop Iteration.
"""

lista = [1, 2, 3]

iterador_da_lista = iter(lista)

print(next(iterador_da_lista))
print(next(iterador_da_lista))
print(next(iterador_da_lista))