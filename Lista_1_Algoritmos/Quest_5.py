# Estender o exercício 4 anterior informando que para pagamento à vista tem
# 15% de desconto, calculando e exibindo este valor.

# início
# texto: produto;
# inteiro: quant;
# real: valor, desconto, total, totalComDesc;
# escreva(“Por favor, digite o nome do produto: ”);
# leia(produto);
# escreva(“Por favor, digite a quantidade de compra: ”);
# leia(quant);
# escreva(“Por favor, digite o valor do produto: ”);
# leia(valor);
# total ¬ quant * valor;
# desconto ¬ total * 0.15;
# totalComDesc ¬ total – totalComDesc;
# escreva(“O valor total da compra de “, produto, ” é”, total);
# escreva(“Pagando à vista, o valor total fica “, totalComDesconto, ”,
# tendo um desconto de”, desconto);
# fim

produto = input("Por favor, digite o nome do produto: ")
print(produto)
quantidade = int(input("Por favor, digite a quantidade de compra: "))
print(quantidade)
valor = float(input("Por favor, digite o valor do produto: "))
print(valor)
total = quantidade * valor
desconto = total * 0.15
totalComDesc = total - desconto
print(f"O valor total da compra de {produto} é R$ {total}")
print(f"Paganto à vista, o valor fica R$ {totalComDesc} ,tendo um desconto de R$ {desconto}")
