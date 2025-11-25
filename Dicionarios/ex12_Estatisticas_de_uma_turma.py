# Estatísticas de uma turma: Peça para cadastrar vários alunos com nome e média em um dicionário. Depois, mostre:
# Quantos alunos foram cadastrados;
# Quantos estão aprovados (média >= 7);
# O nome do aluno com a maior média e o da menor média.

contador = 0
aprovados = 0
maior_media = float("-inf")
menor_media = float("inf") # Obs: Não estou usando "max" nem "min" porque a lista alunos contém tanto nomes quanto médias, então não funcionaria. Além disso, são dicionários e max e min funcionam apenas para listas.
nome_com_maior_media = ""
nome_com_menor_media = ""
alunos = []

quantidade_de_alunos = int(input("Digite quantos alunos deseja cadastrar: "))

while contador < quantidade_de_alunos:
    
    aluno = {"nome": input("Digite o nome do aluno: "), "media": float(input("Digite a média do aluno: "))}
    alunos.append(aluno)
    
    if aluno["media"] >= 7:
        aprovados += 1
    
    contador += 1

for aluno in alunos:
    if aluno["media"] > maior_media:
        maior_media = aluno["media"]
        nome_com_maior_media = aluno["nome"]
    
    if aluno["media"] < menor_media:
        menor_media = aluno["media"]
        nome_com_menor_media = aluno["nome"]

print(f"O aluno {nome_com_maior_media} teve a maior média: {maior_media}")
print(f"O aluno {nome_com_menor_media} teve a menor média: {menor_media}")
print(f"A quantidade de alunos cadastrados foi: {quantidade_de_alunos}")
print(f"A quantidade de aprovados foi: {aprovados}")