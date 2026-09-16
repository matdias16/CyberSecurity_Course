ano_atual = 2026
nascimento = int(input("Escreva sua ano de nascimento> "))
idade = ano_atual - nascimento

resp = input("você ja fez aniversário esse ano ? (s/n)")

if resp == "n":
    idade = idade - 1

print(f"Sua idade é {idade}")
