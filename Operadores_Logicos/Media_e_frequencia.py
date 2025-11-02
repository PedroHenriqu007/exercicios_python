# Peça média e frquência(%). Aprovado se média >= 7 e frequência >= 75%.

media = float(input("Digite sua média: "))
frequencia = int(input("Digite sua frequência (em porcentagem, Ex: 15): "))

percentual_frequencia = frequencia / 100

if media >= 7 and percentual_frequencia >= 75 / 100:
    print("Aprovado.")
else:
    print("Reprovado.")