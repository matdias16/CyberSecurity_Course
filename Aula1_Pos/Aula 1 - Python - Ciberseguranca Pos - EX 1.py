produto = "Pipoqueira, Pop Time, Branco, 127V, Britânia"

detalhes = "Prepara 100g de pipoca com ar quente em aproximadamente 3,5 minutos; " \
"Prática e fácil de usar; Não precisa usar óleo; " \
"Faz até 5 ciclos sem precisar deixar o produto esfriar; " \
"Bocal direcionador da pipoca; Dosador para pipoca e manteiga; " \
"Chave liga/desliga; Pés antiderrapantes; Material: Plástico e metal.";

valor = 130.00

quantidade = 3

garantia = True

produto = input("Digite o nome do produto: ")
valor = float(input("Digite o valor do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))


total = valor*quantidade

print("=============================")
print ("Produto: ", produto)
print ("Detalhes: ", detalhes)
print (f"Preço: R$ {valor:.2f}")
print ("Quantidade: ", quantidade)
print ("Garantia: ", garantia)
print("Total: R$ {total:.2f}")
print("=============================")