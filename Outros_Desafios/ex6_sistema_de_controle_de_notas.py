total_de_alunos = int(input("Digite quantos alunos deseja cadastrar: "))
contador = 0
aprovados = 0
maior_media = 0
menor_media = float("inf")
media_geral = float(0)
lista_de_medias = []
lista_de_alunos = []
nome_menor_media = ""
nome_maior_media = ""

def mostrar_alunos():
    for aluno in lista_de_alunos:
        print(f"Nome: {aluno["nome"]}")
        print(f"Nota 1: {aluno["nota1"]}")
        print(f"Nota 2: {aluno["nota2"]}")
        print(f"Nota 3: {aluno["nota3"]}")
        print(f"Média: {aluno["media"]}")
        print('===========================')

while contador < total_de_alunos:
    aluno = {
    "nome": input("Digite o nome do aluno: "),
    "nota1": float(input("Digite a primeira nota: ")),
    "nota2": float(input("Digite a segunda nota: ")),
    "nota3": float(input("Digite a terceira nota: ")),
}
    lista_de_alunos.append(aluno)
    contador += 1

for aluno in lista_de_alunos:
    notas = [aluno["nota1"], aluno["nota2"], aluno["nota3"]]

    media = sum(notas) / len(notas)

    aluno["media"] = media
    
    lista_de_medias.append(media)
    
    if media > maior_media:
        maior_media = media
        nome_maior_media = aluno["nome"]
        
    if media < menor_media:
        menor_media = media
        nome_menor_media = aluno["nome"]

    if media >= 7:
        aprovados += 1

media_geral = sum(lista_de_medias) / len(lista_de_medias)
        
print(f"A quantidade de aprovados é: {aprovados}")
print(f"A menor média é: {menor_media} do aluno {nome_menor_media}")
print(f"A maior média é: {maior_media} do aluno {nome_maior_media}")
print(f"A média geral é: {media_geral}")

entrada = input("Deseja ver a lista completa de todos os alunos com suas médias? (Digite S para sim e N para não.): ").strip().upper()

if entrada == "S":
    mostrar_alunos()
else:
    print("Encerrando o programa...")