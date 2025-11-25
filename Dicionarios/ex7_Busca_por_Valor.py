# Busca por valor: Peça ao usuário um nome de produto e mostre o preço correspondente, caso ele exista

dic_produto = {"iphone": 5000, "ipad": 10000, "tablet": 15000}

nome_do_produto = input("Digite o nome do produto: ").lower().strip()

if nome_do_produto in dic_produto:
    print(f"O preço do produto é: {dic_produto[nome_do_produto]}")
else:
    print("Produto não encontrado.")