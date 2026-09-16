Disciplina = input("Digite o nome da disciplina: ")
Nota = int(input("Qual foi sua nota do bimestre 1 ? "))
Nota_2 = int(input("Qual foi sua nota do bimestre 2 ? "))
Nota_3 = int(input("Qual foi sua nota do bimestre 3 ?"))
Nota_4 = int(input("Qual foi sua nota do bimestre 4 ?"))
Quantidade_Bimestre = 4

Media_Disciplina = (Nota + Nota_2 + Nota_3 + Nota_4) / Quantidade_Bimestre
#Passo 3: Mostrar resultado
#Aprovado: Media > 7
#Reprovado: Media < 4
#Exame Final: Media >= 4 AND < 7

if Media_Disciplina >= 7:
    print("Aprovado")
#sugar sintax
elif Media_Disciplina < 4:
    print("Reprovado")
else:
    print("Exame Final")

print("Final do programa")
