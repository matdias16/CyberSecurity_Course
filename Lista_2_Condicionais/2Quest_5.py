# Implemente um programa que leia o destino do passageiro, se a viagem inclui retorno (ida e volta)
# e informar o preço da passagem conforme a tabela a seguir:

# Condição                 Ida           Ida e volta
# Região Norte           R$ 500,00        R$ 900,00
# Região Nordeste        R$ 350,00        R$ 650,00
# Região Centro-Oeste    R$ 350,00        R$ 600,00
# Região Sul             R$ 300,00        R$ 550,00

Viagem = int(input(
    "Digite o número do tipo de passagem:\n" \
    "1 - Ida\n"
    "2 - Ida e volta\n"))
Destino = int(input(
    "Digite o número da região de destino:\n"
    "1 - Região Norte \n"
    "2 - Região Nordeste\n"
    "3 - Região Centro-Oeste \n"
    "4 - Região Sul\n"))
if Viagem == 1:
    if Destino == 1:
        print(f"O valor da passagem de ida é R$500,00")
    elif Destino == 2:
        print(f"O valor da passagem de ida é R$350,00")
    elif Destino == 3:
        print(f"O valor da passagem de ida é R$350,00")
    elif Destino == 4:
        print(f"O valor da passagem de ida é R$300,00")
    else:
        print(f"O destino selecionado é inválido")
elif Viagem == 2:
    if Destino == 1:
        print(f"O valor da passagem de ida e volta é R$900,00")
    elif Destino == 2:
        print(f"O valor da passagem de ida e volta é R$650,00")
    elif Destino == 3:
        print(f"O valor da passagem de ida e volta é R$600,00")
    elif Destino == 4:
        print(f"O valor da passagem de ida e volta é R$550,00")
    else:
        print(f"O destino selecionado é inválido")
else:
    print(f"O tipo de passagem escolhido é inválido")


