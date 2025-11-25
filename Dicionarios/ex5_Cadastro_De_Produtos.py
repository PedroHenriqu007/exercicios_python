# Cadastro de produtos: Crie um dicionário onde as chaves são nomes de produtos e os valores são seus preços. Mostre todos os produtos com seus respectivos preços, um por linha.

dic_produtos = {"iphone": 1000, "ipad": 3000, "tablet": 5000, "celular": 7000}

for produto, preco in dic_produtos.items():
    print(f"{produto}: {preco} R$")