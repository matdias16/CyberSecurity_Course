produto = "Pipoqueira, Pop Time, Branco, 127V, Britânia"

detalhes = "Prepara 100g de pipoca com ar quente em aproximadamente 3,5 minutos; " \
"Prática e fácil de usar; Não precisa usar óleo; " \
"Faz até 5 ciclos sem precisar deixar o produto esfriar; " \
"Bocal direcionador da pipoca; Dosador para pipoca e manteiga; " \
"Chave liga/desliga; Pés antiderrapantes; Material: Plástico e metal.";

valor = 130.00

frete = 30.50

quantidade = 4

garantia = True

total = valor*quantidade

if garantia == False:
    total = total + 4.55

if total < 200:
    total = total + frete

if total > 500:
    desconto = total * 0.1
    total = total - desconto

print("=============================")
print ("Produto: ", produto)
print ("Detalhes: ", detalhes)
print (f"Preço: R$ {valor:.2f}")
print ("Quantidade: ", quantidade)
print ("Garantia: ", garantia)
print(f"Total: R$ {total:.2f}")
print("=============================")