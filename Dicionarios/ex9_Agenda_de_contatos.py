# Crie um dicionário chamado agenda, onde cada chave é o nome de uma pessoa e o valor é outro dicionário com "telefone" e "email".
# Permita cadastrar 3 pessoas e, depois, exibir todos os contatos com suas informações.

lista_de_agendas = []

for i in range(3):
    nome = input("Digite seu nome: ")

    agenda = {
    nome: {"telefone": int(input("Digite seu telefone: ")), "email": input("Digite seu email: ")}
    }
    lista_de_agendas.append(agenda)
print(lista_de_agendas)