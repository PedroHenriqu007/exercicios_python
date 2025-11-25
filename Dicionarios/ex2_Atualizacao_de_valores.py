# Atualização de valores: Usando o mesmo dicionário, altere a cidade da pessoa e adicione uma nova chave chamada "profissão".

pessoa = {
    "nome": input("Digite seu nome: "),
    "idade": int(input("Digite sua idade: ")),
    "cidade": input("Digite sua cidade: ")
    }

pessoa["cidade"] = "Xique-xique"
pessoa["profissão"] = input("Digite sua profissão: ")

print(f"Seu nome é: {pessoa["nome"]}")
print(f"Sua idade é: {pessoa["idade"]}")
print(f"Sua cidade é: {pessoa["cidade"]}")
print(f"Sua profissão é: {pessoa["profissão"]}")