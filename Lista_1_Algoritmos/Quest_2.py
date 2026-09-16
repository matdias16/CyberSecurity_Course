#Elaborar um algoritmo que solicita ao usuário seu ano de nascimento e calcula 
# sua idade com relação ao ano de 2020, 
# sendo que o usuário já fez aniversário neste ano

# início
# inteiro: ano_nasc, idade;
# escreva(“Por favor, digite o ano do seu nascimento: ”);
# leia(ano_nasc);
# idade ¬ 2020 – ano_nasc;
# escreva(“A sua idade é”, idade);
# fim

ano_nasc = int(input("Por favor, digite o ano do seu nascimento: "))
print("Seu ano de nascimento:", ano_nasc)
idade = 2020 - ano_nasc
print("A sua idade é", idade)