# Implementar um programa que valide um CPF. Para tanto, solicitar em separado cada um dos 11 dígitos do CPF.

# Definição
# O CPF é formado por 11 dígitos numéricos que seguem a máscara "###.###.###-##", a verificação do CPF acontece utilizando os 9 primeiros dígitos e, ~
# com um cálculo simples, verificando se o resultado corresponde aos dois últimos dígitos (depois do sinal "-").
# Vamos usar como exemplo, um CPF fictício "529.982.247-25".

# Validação do primeiro dígito
# Primeiramente multiplica-se os 9 primeiros dígitos pela sequência decrescente de números de 10 à 2 e soma os resultados. Assim:
# 5 * 10 + 2 * 9 + 9 * 8 + 9 * 7 + 8 * 6 + 2 * 5 + 2 * 4 + 4 * 3 + 7 * 2
# O resultado do nosso exemplo é:  295
#
# O próximo passo da verificação também é simples, basta multiplicarmos esse resultado por 10 e dividirmos por 11. 
# 295 * 10 / 11
# O resultado que nos interessa na verdade é o RESTO da divisão. Se ele for igual ao primeiro dígito verificador (primeiro dígito depois do '-')
# a primeira parte da validação está correta.
# Observação Importante: Se o resto da divisão for igual a 10, nós o consideramos como 0.
# O resultado da divisão acima é '268' e o RESTO é 2. Isso significa que o nosso CPF exemplo passou na validação do primeiro dígito.

# Validação do segundo dígito
# A validação do segundo dígito é semelhante à primeira, porém vamos considerar os 9
# primeiros dígitos, mais o primeiro dígito verificador, e vamos multiplicar esses 10
# números pela sequencia decrescente de 11 a 2. Vejamos:
# 5 * 11 + 2 * 10 + 9 * 9 + 9 * 8 + 8 * 7 + 2 * 6 + 2 * 5 + 4 * 4 + 7 * 3 + 2 * 2
# O resultado é: 347

# Seguindo o mesmo processo da primeira verificação, multiplicamos por 10 e dividimos por 11.
# 347 * 10 / 11
# Verificando o RESTO, como fizemos anteriormente, temos:
# O resultado da divisão é '315' e o RESTO é 5
# Verificamos, se o resto corresponde ao segundo dígito verificador.

# Com essa verificação, constatamos que o CPF 529.982.247-25 é válido.

print("Validação do CPF")
print("=====================")

Digito1 = int(input("Digite o primeiro digito: "))
Digito2 = int(input("Digite o segundo digito: "))
Digito3 = int(input("Digite o terceiro digito: "))
Digito4 = int(input("Digite o quarto digito: "))
Digito5 = int(input("Digite o quinto digito: "))
Digito6 = int(input("Digite o sexto digito: "))
Digito7 = int(input("Digite o sétimo digito: "))
Digito8 = int(input("Digite o oitavo digito: "))
Digito9 = int(input("Digite o nono digito: "))
Digito10 = int(input("Digite o décimo digito: "))
Digito11= int(input("Digite o décimo primeiro digito: "))
print(f"{Digito1}{Digito2}{Digito3}.{Digito4}{Digito5}{Digito6}.{Digito7}{Digito8}{Digito9}-{Digito10}{Digito11}")

Verificação1 = (
    Digito1*10 +
    Digito2*9 +
    Digito3*8 +
    Digito4*7 +
    Digito5*6 +
    Digito6*5 +
    Digito7*4 +
    Digito8*3 +
    Digito9*2 
)

Resto1 = (Verificação1*10)%11
if Resto1 == 10:
    Resto1 = 0

Verificação2 = (
    Digito1*11 +
    Digito2*10 +
    Digito3*9 +
    Digito4*8 +
    Digito5*7 +
    Digito6*6 +
    Digito7*5 +
    Digito8*4 +
    Digito9*3 +
    Digito10*2 
)

Resto2 = (Verificação2*10)%11
if Resto2 == 10:
    Resto2 = 0

if Resto1 == Digito10 and Resto2 == Digito11:
    print("O cpf é válido")
else:
    print("O cpf não é válido")
