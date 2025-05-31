print("Comparación de paridad en números")
numero_1 = 44
numero_2 = 98
ambos_pares = (numero_1 % 2 == 0) and (numero_2 % 2 == 0)
ambos_impares = (numero_1 % 2 != 0) and (numero_2 % 2 != 0)
print(f"{numero_1=} y {numero_2=}, ambos pares: {ambos_pares}")
print(f"{numero_1=} y {numero_2=}, ambos impares: {ambos_impares}")
numero_1 = 111
numero_2 = 333
ambos_pares = (numero_1 % 2 == 0) and (numero_2 % 2 == 0)
ambos_impares = (numero_1 % 2 != 0) and (numero_2 % 2 != 0)
print(f"{numero_1=} y {numero_2=}, ambos pares: {ambos_pares}")
print(f"{numero_1=} y {numero_2=}, ambos impares: {ambos_impares}")