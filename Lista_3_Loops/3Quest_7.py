# Elaborar um programa que solicita várias palavras ao usuário, sendo que o critério de parada é digitar uma palavra vazia. 
# Contar e exibir quantas letras A existem neste conjunto de palavras.

Letras_a = 0

while True:
    palavras = input("Digite uma palavra: ")
    if palavras == "":
        break
    
    Letras_a += palavras.count("a")

print(f"Quantidade de letras A:", Letras_a)

