produto = input("Digite o nome do produto: ")
valor = float(input("Digite o valor do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))

total = valor*quantidade

print("=============================")
print ("Produto: ", produto)
print ("Quantidade: ", quantidade)
print (f"Preço: R$ {valor:.2f}")
print(f"Total: R$ {total:.2f}")
print("=============================")