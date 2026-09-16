n1 = int(input("Digite o Numero 1"))
n2 = int(input("Digite o Numero 2"))
n3 = int(input("Digite o Numero 3"))

#Se o n1 for menor que o n2 e o n2 for menor que o n3, entao o n1 é o menor.
if n1 < n2 and n2 < n3:
    print("n1 é o menor")

if n1 < n3 and n3 < n2:
    print("n1 é o menor")