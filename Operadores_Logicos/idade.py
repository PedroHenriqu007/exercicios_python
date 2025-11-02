# Peça a idade e se a pessoa tem carteirinha de estudante (S/N). Ela pode entrar se: idade < 18 ou tiver carteirinha.

idade = int(input("Digite sua idade: "))
tem_carteirinha = input("Você tem carteirinha de estudante? (Digite 'S' para 'Sim' e 'N' para 'Não'.): ")

if idade < 18 or tem_carteirinha == 'S':
    print("Pode entrar!")
else:
    print("Não pode entrar.")