# Criar um jogo de pedra, papel, tesoura entre dois jogadores. 
# Antes de começar o jogo, porém, deve ser escolhido a quantidade de pontos a serem feitos para vencer.

pontosvencer = int(input("Quantos pontos são necessários para vencer? "))

ptsjogador1 = 0
ptsjogador2 = 0

while ptsjogador1 < pontosvencer and ptsjogador2 < pontosvencer:

    print("\nPlacar:")
    print("Jogador 1:", ptsjogador1)
    print("Jogador 2:", ptsjogador2)

    jogador1 = input("Jogador 1 (pedra, papel ou tesoura): ")
    jogador2 = input("Jogador 2 (pedra, papel ou tesoura): ")

    if jogador1 == jogador2:
        print("Empate!")

    elif (
        (jogador1 == "pedra" and jogador2 == "tesoura") or
        (jogador1 == "papel" and jogador2 == "pedra") or
        (jogador1 == "tesoura" and jogador2 == "papel")
    ):
        ptsjogador1 += 1
        print("Jogador 1 venceu a rodada!")

    else:
        ptsjogador2 += 1
        print("Jogador 2 venceu a rodada!")

print("\n=== FIM DE JOGO ===")

if ptsjogador1 == pontosvencer:
    print("Jogador 1 venceu a partida!")
else:
    print("Jogador 2 venceu a partida!")
    
