from time import sleep

lista_de_produtos = []

def cadastrar_produto(lista):
    if lista:
        nome_do_produto = input("Digite o nome do produto: ").strip().upper()
        for d in lista:
            if nome_do_produto in d:
             print("Produto já existente.")
             break 
        else:
            quantidade = int(input("Digite a quantidade do produto: "))
            preco = float(input("Digite o preço unitário do produto: "))
            if quantidade < 0 or preco < 0:
                print("Quantidade e preço não podem ter valores negativos.")
            else:
                produto = {nome_do_produto : {"Quantidade" : quantidade, "Preço" : preco}}
                lista.append(produto)
    else:    
        nome_do_produto = input("Digite o nome do produto: ").strip().upper()
        quantidade = int(input("Digite a quantidade do produto: "))
        preco = float(input("Digite o preço unitário do produto: "))
        if quantidade < 0 or preco < 0:
            print("Quantidade e preço não podem ter valores negativos.")
        else:
            produto = {nome_do_produto : {"Quantidade" : quantidade, "Preço" : preco}}
            lista.append(produto)

def listar_produtos(lista):
    print("  Nº\tPRODUTO\t\t\t\tQUANTIDADE\tPREÇO")
    print("-" * 90)
    for p, d in enumerate(lista):
        nome = next(iter(d.keys()))
        info = next(iter(d.values()))
        qtd = info["Quantidade"]
        preco = info["Preço"]
        
        print(f"{p:>3}     {nome:<20}      {qtd:>10}       {preco:>10.2f}", flush=True)
        sleep(1)

def buscar_produto(lista):
    busca = input("Digite o nome do produto: ").strip().upper()
    encontrado = False
    for d in lista:
        if busca in d:
            print("Produto encontrado.")
            print(d)
            encontrado = True
            break
    
    if not encontrado:
        print("Produto não encontrado.")

def atualizar_produto(lista):
    busca = input("Digite o nome do produto: ").strip().upper()
    encontrado = False
    for d in lista:
        if busca in d:
            encontrado = True
            res = int(input("O que quer fazer? [1 -> Atualizar quantidade, 2 -> Atualizar preço] "))
            
            if res == 1:
                nova_quantidade = int(input("Digite a nova quantidade: "))
                if nova_quantidade < 0:
                    print("A quantidade não pode ser negativa.")
                else:
                    d[busca]["Quantidade"] = nova_quantidade
                    print("Quantidade atualizado.")
                    print(d)   
            else:
                novo_preco = float(input("Digite o novo preço unitário: "))
                if novo_preco < 0:
                    print("O preço não pode ser negativo.")
                else:    
                    d[busca]["Preço"] = novo_preco
                    print("Preço atualizado.")
                    print(d)
    
    if not encontrado:
        print("Produto não encontrado.")

def remover_produto(lista):
    busca = input("Digite o nome do produto: ").strip().upper()
    encontrado = False
    for d in lista:
        if busca in d:
            lista.remove(d)
            print("Produto removido.")
            encontrado = True
            break
    if not encontrado:
        print("Produto não encontrado.") 

def calcular_valor_total(lista):
    valor_total = 0.0
    for d in lista:
        info = next(iter(d.values()))
        valor_total += info["Quantidade"] * info["Preço"]
    
    print(f"O valor total do estoque é: {valor_total}")

while True:
    r = int(input("O que quer fazer?" 
                  "\n1 = Cadastrar novo produto" 
                  "\n2 = Listar todos os produtos"
                  "\n3 = Buscar produto pelo nome"
                  "\n4 = Atualizar quantidade ou preço de um produto" 
                  "\n5 = Remover um produto do estoque" 
                  "\n6 = Mostrar valor total do estoque" 
                  "\n7 = Sair do programa"
                  "\nEscolha: "))
    
    if r == 7:
        print("Encerrando o programa...")
        break
    elif r == 1:

        while True:
            
            cadastrar_produto(lista_de_produtos)
            
            resposta = input("Quer continuar? [S/N] ").strip().upper()
            if resposta == "N":
                break
    elif r == 2:
        listar_produtos(lista_de_produtos)
        
    elif r == 3:
       buscar_produto(lista_de_produtos)
                
    elif r == 4:
        atualizar_produto(lista_de_produtos)
                    
    elif r == 5:
        remover_produto(lista_de_produtos)
    
    elif r == 6:
        calcular_valor_total(lista_de_produtos)
        
    else:
        print("Essa opção não está no menu. Por favor, digite corretamente.")
            