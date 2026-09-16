# Implemente um programa para calcular as raízes de uma equação do 2º grau, sendo que
# os valores dos coeficientes A, B, e C devem ser fornecidos pelo usuário, e os valores das
# raízes devem ser calculadas pela fórmula de Bhaskara, como segue:
# x = (-b + - raíz b**2 - 4ac) / 2a

print("Fórmula de Bhaskara")
print("======================")

a = float(input("Digite o valor de a:"))
b = float(input("Digite o valor de b:"))
c = float(input("Digite o valor de c:"))
if a == 0:
    print("Não é uma equação do 2º grau")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Não existem raízes em números reais")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Como o delta é igual a 0, o resultado é apenas uma raíz, sendo {x}")
    else:
        raiz_quadrada = delta ** (0.5)
        bhaskara1 = (-b + raiz_quadrada) / 2*a
        bhaskara2 = (-b - raiz_quadrada) / 2*a
        print(f"raíz 1 = {bhaskara1}")
        print(f"raíz 2 = {bhaskara2}")


