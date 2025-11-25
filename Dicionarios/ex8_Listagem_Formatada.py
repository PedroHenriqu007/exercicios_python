# Listagem formatada: Mostre todos os produtos com preços acima de R$50,00.

lista_formatada = {}

dic_produtos = {"iphone": 5000, "ipad": 10000, "cartela de ovos": 24, "tablet": 15000, "suco tang": 0.99}

for produto, preco in dic_produtos.items():
    if preco > 50:
        lista_formatada[produto] = preco
        
print(lista_formatada)