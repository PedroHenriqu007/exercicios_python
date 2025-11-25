# Ranking de pontuação: Crie um dicionário para registrar o nome de jogadores e suas pontuações.
# Mostre o jogador com a maior e a menor pontuação.

jogadores = []
contador = 0
pontuacao_maior = float("-inf")
pontuacao_menor = float("inf")
nome_maior = ""
nome_menor = ""

total_de_jogadores = int(input("Digite quantos jogadores deseja cadastrar: "))

while contador < total_de_jogadores:

    jogador = {"nome": input("Digite seu nome: "), "pontuação": float(input("Digite sua pontuação: "))}
    jogadores.append(jogador)
    contador += 1

for jogador in jogadores:
    if jogador["pontuação"] > pontuacao_maior:
        pontuacao_maior = jogador["pontuação"]
        nome_maior = jogador["nome"]
        
    if jogador["pontuação"] < pontuacao_menor:
        pontuacao_menor = jogador["pontuação"]
        nome_menor = jogador["nome"]

print(f"A maior pontuação é de {pontuacao_maior}, do jogador {nome_maior}!")
print(f"A menor pontuação é de {pontuacao_menor} do jogador {nome_menor}")