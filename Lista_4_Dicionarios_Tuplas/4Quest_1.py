# - Imprimir o cardápio do restaurante com as opções de produtos ofertados;
# - Logo abaixo do cardápio, exibir a mensagem “O que deseja pedir (0 para sair)?”;
# - Digitando “0” deve sair do programa;
# - Digitando o nome do produto pode ter uma das seguintes possibilidades:
# - Se o item não consta no cardápio exibir a mensagem “Item não localizado no cardápio”;
# - Se não tiver os ingredientes para o preparo do produto em estoque mostrar uma mensagem para cada ingrediente faltante “Infelizmente acabou o {ingrediente}”;
# - Se for possível produzir o produto, reduzir as quantidades de estoque e mostrar a mensagem “um {produto} saindo no capricho!!!”;
# - O programa deve continuar fazendo os pedidos até que o usuário decida sair do mesmo.

estoque = {'pao': 10, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 5}
cardapio = {
'x-burguer': ['pao', 'hamburguer'],
'x-salada': ['pao', 'hamburguer', 'tomate'],
'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
'x-egg': ['pao', 'hamburguer', 'ovo'],
'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
}

while True:
    print("Restaurante Boca Feliz")

    for opcoes in cardapio:
        print(opcoes)

    pedido = input("O que deseja pedir (0 para sair)?")

    if pedido == "0":
            print("Obrigado!")
            break
    
    if pedido not in cardapio:
        print("Item não localizado no cardápio")
        continue

    ingredientes = cardapio[pedido]

    faltando = []

    for ingrediente in ingredientes:
        if estoque[ingrediente] <= 0:
            faltando.append(ingrediente)

    if len(faltando) > 0:

        for ingrediente in faltando:
            print(f"Infelizmente acabou o {ingrediente}")

    else:
        for ingrediente in ingredientes:
            estoque[ingrediente] -= 1


        print(f"Um {pedido} saindo no capricho!!!")