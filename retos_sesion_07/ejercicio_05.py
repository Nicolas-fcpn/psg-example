# Escribe un programa que reciba una cadena y retorna verdadero o 
# falso si es palindrome sin importar los espacios, mayúsculas o minúsculas

cadena = input("Ingrese la cadena de prueba: ")
cadena_prueba = cadena.replace(" ", "").lower()
cadena_inv = cadena_prueba[len(cadena_prueba)::-1]
prueba = cadena_prueba == cadena_inv
print(f'"{cadena}" es {prueba}')
print(f"{cadena_prueba} -> {cadena_inv}")