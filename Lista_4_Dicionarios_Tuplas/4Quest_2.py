# - Imprimir a lista de unidades de conversão
# - Solicitar o valor que se deseja converter usando a frase “Valor a ser convertido: ”
# - Solicitar a unidade origem do valor usando a frase “Converter de: ”
# - Solicitar a unidade destino de conversão usando a franse “Converter para: ”
# - Exibir o valor convertido com a frase “Conversão: {valor} {unidade origem} = {valor} {unidade destino}”


ano_luz = {
"pc": 0.31,
"al": 1,
"ae": 63241.09,
"ml": 525960.23,
"sl": 31557609.92
}
unidades = [
"Parsec (pc)",
"Ano-Luz (al)", 
"Unidade Astronômica (ae)",
"Minuto-Luz (ml)", 
"Segundo-Luz (sl)"
]

print("---Unidades de conversão---")

for unidade in unidades:
    print(unidade) 

print("---------------------------")


solicitar_valor = float(input("Valor a ser convertido: "))
unidade_inicial = input("Converter de (Inserir somente a abreviação): ")
unidade_final = input("Converter para (Inserir somente a abreviação): ")

valorinicial_luz = solicitar_valor * ano_luz[unidade_inicial]

valor_convertido = valorinicial_luz / ano_luz[unidade_final]

print("---------------------------")


print(f"Conversão: {solicitar_valor} {unidade_inicial} = {valor_convertido} {unidade_final}")