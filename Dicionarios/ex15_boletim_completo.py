# Boletim completo: Crie um dicionário que armazene, para cada aluno, suas notas, média e situação ("Aprovado" ou "Reprovado").
# Ao final, mostre um boletim formatado com nome, média e situação de cada aluno.

def boletim_formatado():
    print(f"Nome: {nome}")
    print(f"Média: {aluno[nome]["media"]}")
    print(f"Situação: {situacao}")


quantidade_de_alunos = int(input("Digite a quantidade de alunos para cadastrar: "))
contador = 0

while contador < quantidade_de_alunos:

    nome = input("Digite o nome do aluno: ")

    quantidade_de_notas = int(input("Digite a quantidade de notas que deseja cadastrar: "))

    notas = []

    aluno = {nome: {}}

    for nota in range(quantidade_de_notas):
        aluno[nome][f"nota{nota+1}"] = float(input(f"Digite a nota {nota+1}: "))
        notas.append(aluno[nome][f"nota{nota+1}"])
        media = sum(notas) / len(notas)
        aluno[nome]["media"] = media
        
        if aluno[nome]["media"] >= 7:
            situacao = "aprovado"
        else:
            situacao = "reprovado"
    contador += 1
    
    boletim_formatado()