""" Receba duas notas e calcule a média. 
    - Se for >= 7: "Aprovado"
    - Se for entre 5 e 6.9: "Recuperação"
    - Senão: "Reprovado
"""

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if(media >= 7):
    print("Aprovado.")
elif(media >= 5 and media <= 6.9):
    print("Recuperação.")
else:
    print("Reprovado.")