"""Crie um programa em Python que:
1. Peça o nome do aluno.
2. Solicite duas notas (pode ser float).
3. Calcule a média das duas notas.
4. Mostre o nome do aluno e sua média com duas casas decimais
5. Informe a situação do aluno: 
"Aprovado" se média ≥ 7

"Recuperação" se média entre 5 e 6.9

"Reprovado" se média < 5"""

outra_media = 0

while outra_media != 'N':
    nome_do_aluno = input("Digite seu nome: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    notas = [nota1, nota2]

    media = sum(notas) / 2

    if(media >= 7):
        situacao = "aprovado"
    elif(media >= 5 and media <= 6.9):
        situacao = "de recuperação"
    else:
     situacao = "reprovado"

    print(f"Olá, {nome_do_aluno}! Sua média é: {media:.2f} e você está {situacao}.")
    
    outra_media = str(input("Deseja calcular outra média? (Digite S para Sim e N para não.): "))