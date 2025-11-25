# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = []

while True:
    
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    notas = [nota1, nota2]
    
    media = (nota1 + nota2) / 2
    aluno = [nome, notas, media]
    alunos.append(aluno)
    
    r = input("Adicionado com sucesso, deseja continuar? [S/N] ").strip().upper()
    if r == "N":
        break
print("-" * 30)
print("Nº   NOME    MÉDIA")
print("-" * 30)
for posicao, valor in enumerate(alunos):    
    print(f"{posicao}   {valor[0]:^5}", end="     ")
    print(f"{valor[2]:^5}")

print("-" * 30)
while True:
    mostrar_aluno = int(input("Qual aluno você quer ver as notas? (Digite a posição. 999 interrompe.) "))
    if mostrar_aluno == 999:
        print("FINALIZANDO...")
        print("<<< VOLTE SEMPRE >>>")
        break
    else:
        for posicao, valor in enumerate(alunos):
            if mostrar_aluno == posicao:
                print("-" * 30)
                print(f"As notas de {valor[0]} são: {valor[1]} ")
