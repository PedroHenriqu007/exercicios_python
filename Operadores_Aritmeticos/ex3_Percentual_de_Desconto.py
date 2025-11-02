# Peça o valor de um produto e o percentual de desconto, e calcule o valor final.

valor = float(input("Digite o valor do produto: "))
percentual_de_desconto = int(input("Digite o percentual de desconto: "))

resultado = valor * percentual_de_desconto / 100

print("O desconto é de: ", resultado)