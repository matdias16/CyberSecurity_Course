# Aniversario da Matilda
presente1 = "Dark Souls III"
presente2 = "Pijama"
presente3 = "Skyrim"
presente4 = "Meias"

# List(Array, Vetor, ArrayList, Matriz unidimensional)

presentes = ["Dark Souls III", "Pijama", "Skyrim", "Meias"]
print (presentes)
print ("Quantidade de presentes", len(presentes))
print ("Quantidade de presentes", presentes[2])

presentes.append(200.0)
print(presentes)

presentes.insert(1, "O senhor dos aneis, Edição de Luxo")
print(presentes)

for presente in presentes:
    print(presente)

for i in range(len(presentes)):
    print(f"{i}: {presentes[i]}")


#slicing
# Acessar pedaços da lista
print("Toda a lista: ", presentes)
print("Do 1 ao 3: ", presentes[1:4])
print("Do 1 ao 3: ", presentes[:2])
print("Do 1 ao 3: ", presentes[4:])

presentes[2:4] = ["Lego Avengers", "Bola"]
print(presentes)

presentes[2:4] = ["Vestido"]
print(presentes)

presentes[2:4] = []
print(presentes)

presentes.remove("Dark Souls III")
print(presentes)

presentes += ["Bloodborne", "Frescobol"] #Concatenando no final da lista esses valores. Append adiciona 1 valor; += ou extend coloca um vetor.
print(presentes)

print("==========================")

#                  -4            -3        -2      -1
#                   0             1         2       3
presentes = ["Dark Souls III", "Pijama", "Skyrim","Meias"]
print("Último elemento:", presentes[-1])
print("Penúltimo elemento:", presentes[-2])


# Limpar a lista
presentes = []
presentes.clear