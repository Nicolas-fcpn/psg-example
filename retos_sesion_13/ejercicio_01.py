# Imprimir los 20 primeros números de la sucesión de Lucas.

suc_lucas = [2, 1]
for i in range(2, 20):
    suc_lucas.append(suc_lucas[i-1] + suc_lucas[i-2])
print("Los 20 primeros números de la sucesión de Lucas son:")
for i in range(20):
        print(suc_lucas[i], end=' ')