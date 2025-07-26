# Imprimir los 20 primeros números que sean múltiplos de 2 y 5.
multiplos = []
numero = 10  # Comenzamos desde el primer múltiplo de 2 y 5
while len(multiplos) < 21:
    if numero % 2 == 0 and numero % 5 == 0:
        multiplos.append(numero)
    numero += 1

print("Los 20 primeros números que son múltiplos de 2 y 5 son:")

for i in range(20):
    print(multiplos[i], end=' ')