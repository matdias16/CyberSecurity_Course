# Elaborar um programa em Python que converta um número decimal em hexadecimal, fazendo uso do método de divisões sucessiva

Decimal_Hexadecimal = ""
Digitos_Hexadecimal = "0123456789ABCDEF"
Decimal = int(input("Digite um número Decimal: "))

while Decimal > 0:
    resto = Decimal%16 #4
    Decimal_Hexadecimal = Digitos_Hexadecimal[resto] + Decimal_Hexadecimal
    Decimal = Decimal//16

print(f"O valor em hexadecimal é: ", Decimal_Hexadecimal)