# Sistema de estoque: Crie um sistema de estoque onde cada produto tem como valor um dicionário com quantidade e preço.
# O programa deve:
# Permitir cadastrar produtos;
# Atualizar quantidades;
# Mostrar o valor total do estoque.

estoque = {"iphone": {"quantidade": 10, "preço": 2500}, "ipad": {"quantidade": 15, "preço": 3500}, "tablet": {"quantidade": 20, "preço": 4000}}

while True:
    
    valores_totais = []
    
    input_inicial = int(input("Digite 1 para cadastrar o produto, 2 para atualizar a quantidade, 3 para ver o custo total do estoque ou 4 para encerrar o programa: "))
    
    if input_inicial == 1:
        nome_do_produto = input("Digite o nome do produto que será cadastrado: ")
    
        if nome_do_produto in estoque:
            print("Você não pode cadastrar um produto que já existe.")
        else:
            quantidade = int(input("Digite a quantidade: "))
            preco = float(input("Digite o preço: "))
            estoque[nome_do_produto] = {"quantidade": quantidade, "preço": preco}
        
            print("Produto cadastrado com sucesso!")
            print(estoque)
        
    elif input_inicial == 2:
        nome_do_produto = input("Digite o nome do produto que será atualizado: ")
    
        if nome_do_produto not in estoque:
            print("Você não pode atualizar um produto que não existe no estoque.")
        else:
            quantidade = int(input("Digite a nova quantidade do produto: "))
            if quantidade == estoque[nome_do_produto]["quantidade"]:
                print("O produto já possui essa quantidade. Por favor, atualize corretamente.")
            else:
                estoque[nome_do_produto]["quantidade"] = quantidade
                print("Atualização concluída!")
                print(estoque)
    elif input_inicial == 3:
        for valor in estoque.values():
            quantidade = valor["quantidade"]
            preco = valor["preço"]
            valor_total = quantidade * preco
            valores_totais.append(valor_total)
        print(f"O valor total do estoque é: {sum(valores_totais)}")
    else:
        print("Encerrando o programa...")
        break