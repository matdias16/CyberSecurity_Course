# Implemente um programa que calcule o que deve ser pago por um produto,
# considerando o preço normal de etiqueta e a escolha da condição de pagamento. 
# Utilize os códigos da tabela a seguir para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.
# Código Condição de pagamento
# • 1 – À vista em dinheiro ou cheque, recebe 10% de desconto
# • 2 – À vista no cartão de crédito, recebe 15% de desconto
# • 3 – Em duas vezes, preço normal de etiqueta sem juros
# • 4 – Em duas vezes, preço normal de etiqueta mais juros de 10%


Produto = input("Digite o nome do produto: ")
Preço = float(input("Qual o valor do produto ? R$"))
FormaPgt = int(input(
    "Insira a forma de pagamento:\n"
    "1 - À vista em dinheiro ou cheque (10% desconto)\n"
    "2 - À vista no cartão de crédito (15% desconto)\n"
    "3 - Em duas vezes (sem juros)\n"
    "4 - Em duas vezes (10% de juros)\n"
    ))
if FormaPgt == 1:
    Total1 = Preço - (Preço * 0.10)
    print(f"O valor total do produto fica R$ {Total1}")
elif FormaPgt == 2:
    Total2 = Preço - (Preço * 0.15)
    print(f"O valor total do produto fica R$ {Total2}")
elif FormaPgt == 3:
    print(f"O valor total do produto fica R$ {Preço}, preço normal da etiqueta sem juros")
elif FormaPgt == 4:
    Total3 = Preço + (Preço * 0.10)
    print(f"O valor total do produto fica R$ {Total3}, preço normal da etiqueta com 10% de juros")
else:
    print("Forma de pagamento inválida")