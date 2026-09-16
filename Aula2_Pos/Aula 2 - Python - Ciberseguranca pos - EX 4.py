# contar de 1 a 10
nota = -1
while True:
    try: #Utilizamos o try no caso que queremos que o programa tente fazer o while independente da condição
        nota = float(input("Digite uma nota de 0 a 10: "))
    except ValueError: #usamos o except para que caso de algum erro, o python ele usará como exceção e seguirá
        print("Nota inválida. Digite um número entre 0 e 10")

print("Sua nota é: ", nota)

