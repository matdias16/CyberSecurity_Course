# Elaborar um algoritmo que solicita o nome de um produto, seu valor e
# quantidade, informando o valor de compra calculado.

# início
# texto: produto;
# inteiro: quant;
# real: valor, total;
# escreva(“Por favor, digite o nome do produto: ”);
# leia(produto);
# escreva(“Por favor, digite a quantidade de compra: ”);
# leia(quant);
# escreva(“Por favor, digite o valor do produto: ”);
# leia(valor);
# total ¬ quant * valor;
# escreva(“O valor total da compra de “, produto, ” é”, total);
# fim

produto = input("Por favor, digite o nome do produto: ")
print(produto)
quantidade = int(input("Por favor, digite a quantidade de compra: "))
print(quantidade)
valor = float(input("Por favor, digite o valor do produto: "))
print(valor)
total = quantidade * valor
print(f"O valor total da compra de {produto} é: {total}")
