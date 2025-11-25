# Remoção de dados: Remova a chave "idade" do dicionário e mostre o resultado atualizado.

pessoa = {
    "nome": input("Digite seu nome: "),
    "idade": int(input("Digite sua idade: ")),
    "cidade": input("Digite a cidade: ")
}

pessoa.pop("idade")

print(pessoa)