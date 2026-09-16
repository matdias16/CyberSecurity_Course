# Funções

# Não tem parâmetros de entrada
# Não tem retorno

def saudacao():
    print("Boas Vindas !")


# Com parâmetros de entrada
# Não tem retorno

def saudacao2(nome):
    print(f"Boas Vindas {nome}!")



def somar(num1, num2, num3):
    resultado = num1 + num2 + num3
    return resultado

saudacao()
saudacao2("Joaquinzinho")
saudacao2("Mariazinha")

print("================================")

valor = somar(10, 15, 7)
print(valor)
