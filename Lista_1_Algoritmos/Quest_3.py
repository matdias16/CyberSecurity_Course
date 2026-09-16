# Elaborar um algoritmo que solicita ao usuário o nome de uma disciplina e suas
# 4 notas bimestrais. O algoritmo deve calcular a média destas notas, e uma
# mensagem informando que a média da disciplina nome é média.

# início
# texto: disciplina;
# real: nota1, nota2, nota3, nota4, media;
# escreva(“Por favor, digite a nota da disciplina: ”);
# leia(disciplina);
# escreva(“Por favor, digite a nota do primeiro bimestre: ”);
# leia(nota1);
# escreva(“Por favor, digite a nota do segundo bimestre: ”);
# leia(nota2);
# escreva(“Por favor, digite a nota do terceiro bimestre: ”);
# leia(nota3);
# escreva(“Por favor, digite a nota do quarto bimestre: ”);
# leia(nota4);
# media ¬ (nota1 + nota2 + nota3 + nota4) / 4;
# escreva(“A média da disciplina”, disciplina, ” é”, media);
# fim

disciplina = input(" Por favor, digite o nome da Disciplina: ")
print(disciplina)
nota1 = int(input("Por favor, a nota do primeiro bimestre: "))
print(nota1)
nota2 = int(input("Por favor, a nota do segundo bimestre: "))
print(nota2)
nota3 = int(input("Por favor, a nota do terceiro bimestre: "))
print(nota3)
nota4 = int(input("Por favor, a nota do quarto bimestre: "))
print(nota4)
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A média da disciplina {disciplina} é: {media}")
