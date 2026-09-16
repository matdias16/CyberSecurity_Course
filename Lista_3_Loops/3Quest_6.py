# Elaborar um programa que receba o nome completo do usuário, e imprima apenas o primeiro e último nome
# Mateus dos Santos Dias
# Split
#   0     1    2     3
#   -4   -3   -2    -1

nome_completo = input("Digite seu nome completo: ")

nomes = nome_completo.split()

primeiro_nome = nomes[0]
ultimo_nome = nomes[-1]

print("Primeiro nome:", primeiro_nome)
print("Último nome:", ultimo_nome)


