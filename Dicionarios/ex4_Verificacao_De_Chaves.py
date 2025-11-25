# Verificação de chaves: Peça uma chave ao usuário e verifique se ela existe no dicionário. Exiba uma mensagem informando se foi encontrado ou não.

produto = {"iphone": 5000, "ipad": 6000, "tablet": 7000}

nome_do_produto = input("Digite o nome do produto: ")

if nome_do_produto in produto:
    print("Produto encontrado.")
else:
    print("Produto não encontrado.")