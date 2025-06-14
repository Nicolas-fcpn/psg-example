# Crea una tupla con los siguientes elementos:

tupla = ('a','b','c','d','e','f','g','h','i','j')

print(f"tupla: {tupla}")

# Imprime el primer elemento

print(f"Primer elemento: {tupla[0]}")

# Imprime el último elemento

print(f"Ultimo elemento: {tupla[len(tupla) - 1]}")

# Imprime un slice del índice 3 al 5

print(f"Slice del índice 3 al 5: {tupla[3:6]}")

# Imprime un slice del 5 al 9 con pasos de 3

print(f"Slice de elementos 5 al 9 con pasos de 3: {tupla[4:9:3]}")

# Imprime un slice del 9 al 0 con pasos de -2

print(f"Slice del 9 al 0 con pasos de -2: {tupla[9:0:-2]}")