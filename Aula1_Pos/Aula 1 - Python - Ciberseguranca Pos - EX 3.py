import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

produto = input("Digite o nome do produto: ")
valor = float(input("Digite o valor do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

total = valor * quantidade

print("=============================")
print("Produto:", produto)
print("Quantidade:", quantidade)
print("Preço:", locale.currency(valor, grouping=True))
print("Total:", locale.currency(total, grouping=True))
print("=============================")