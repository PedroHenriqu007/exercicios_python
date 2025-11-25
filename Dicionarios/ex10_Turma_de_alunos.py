# Turma de alunos
# Crie um dicionário onde cada chave é o nome de um aluno e o valor é outro dicionário com as notas das provas. Depois, calcule e mostre a média de cada aluno.

contador = 0
medias = []
quantidade_de_alunos = int(input("Digite quantos alunos deseja cadastrar: "))

if quantidade_de_alunos == 0:
    print("Encerrando o programa...")

while contador < quantidade_de_alunos:
    
    notas = []

    nome = input("Digite o nome do aluno: ")

    while True:
        quantidade_de_notas = int(input("Digite quantas notas deseja cadastrar: "))
    
        if quantidade_de_notas == 0 or quantidade_de_notas < 0:
            print("A quantidade de notas não pode ser zero e nem um número negativo.")
        else:
            break
    
    aluno = {nome: {}}
    
    for nota in range(quantidade_de_notas):
        aluno[nome][f"nota{nota+1}"] = float(input(f"Digite a nota {nota+1}: "))
        notas.append(aluno[nome][f"nota{nota+1}"])
        
    media = sum(notas) / len(notas)
    medias.append((nome, media))
    contador += 1

for nome, media in medias:
    print(f"A média de {nome} é {media}")