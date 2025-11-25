# Cadastro simples: Crie um dicionário para armazenar as informações de uma pessoa: nome, idade e cidade. Depois, exiba cada valor com uma mensagem descritiva.

pessoa = {
    "nome": input("Digite seu nome: "),
    "idade": int(input("Digite sua idade: ")),
    "cidade": input("Digite sua cidade: ")
}

print(f"O seu nome é: {pessoa["nome"]}")
print(f"A sua idade é: {pessoa["idade"]}")
print(f"A sua cidade é: {pessoa["cidade"]}")