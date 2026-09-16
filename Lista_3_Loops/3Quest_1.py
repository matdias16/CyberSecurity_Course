# Um determinado material radioativo perde metade de sua massa a cada 50 segundos.
# Dada a massa inicial, em gramas, fazer um algoritmo que determine o tempo necessário
# para que a massa se torne menor do que 0,5 grama. 
# Imprima como dado de saída a massa final e o tempo calculado em segundos

Massa = float(input("Qual a quantidade de massa do material radioativo ? "))
Tempo = 0
while Massa >= 0.5:
    Massa = Massa/2
    Tempo += 50

Tempo2 = Tempo // 60

print(f"Massa final {Massa:.4f}g")
print(f"tempo necessário {Tempo} segundos")
print("Ou")
print(f"{Tempo2} minutos")
