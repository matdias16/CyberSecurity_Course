# Criar um jogo de par ou ímpar, onde dois jogadores entram com seu palpite (par ou ímpar) e seus valores de 1 a 5. 
# Tomar por base os nomes: Jogador 1 e Jogador 2. 
# Caso um dos valores esteja fora dos parâmetros informados, mostrar uma mensagem informando que esta rodada não valeu. 
# Caso contrário, informa qual jogador ganhou esta rodada.

print("Jogo do PAR OU IMPAR")
print("--------------------------------------")

jogadorPalpite1 = input("Jogador 1: Digite se será par ou ímpar: ")
valor1 = int(input("Jogador 1: Digite um valor de 1 a 5: ")) 
jogadorPalpite2 = input("Jogador 2: Digite se será par ou ímpar: ")
valor2 = int(input("Jogador 2: Digite um valor de 1 a 5: "))
if valor1 < 1 or valor1 > 5 or valor2 < 1 or valor2 > 5:
    print("Essa rodada não valeu, os números devem ser entre 1 a 5")
elif jogadorPalpite1 == jogadorPalpite2:
    print("Essa rodada não valeu, os palpites devem ser diferentes")
else:
    soma = valor1 + valor2
    if soma %2 == 0:
        resultado = "par"
    else:
        resultado = "ímpar"
    print(f"\nA soma foi {soma}, que é {resultado}.")

    if jogadorPalpite1 == resultado:
        print("Jogador 1 venceu")
    else:
        print("Jogador 2 venceu")

