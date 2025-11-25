# Meu primeiro desafio Python!

aluno1 = []
aluno2 = []
aluno3 = []
aluno4 = []
aluno5 = []

for i in range(5):
    nome = input("Digite seu nome: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
    dados_do_aluno = [nome, nota1, nota2, nota3]
    
    if i == 0:
        aluno1.extend(dados_do_aluno)
    elif i == 1:
        aluno2.extend(dados_do_aluno)
    elif i == 2:
        aluno3.extend(dados_do_aluno)
    elif i == 3:
        aluno4.extend(dados_do_aluno)
    else:
        aluno5.extend(dados_do_aluno)

soma1 = [item for item in aluno1 if isinstance(item, float)]
soma2 = [item for item in aluno2 if isinstance(item, float)]
soma3 = [item for item in aluno3 if isinstance(item, float)]
soma4 = [item for item in aluno4 if isinstance(item, float)]
soma5 = [item for item in aluno5 if isinstance(item, float)]

media1 = sum(soma1) / len(soma1)
media2 = sum(soma2) / len(soma2)
media3 = sum(soma3) / len(soma3)
media4 = sum(soma4) / len(soma4)
media5 = sum(soma5) / len(soma5)
medias = [media1, media2, media3, media4, media5]

alunos_aprovados = 0

for i in medias:
    if i >= 7:
        alunos_aprovados += 1

maior_media = max(medias)

print(f"O total de alunos aprovados é: {alunos_aprovados}, e a maior média foi: {maior_media}")