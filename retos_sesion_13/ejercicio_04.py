# Crea un ciclo infinito que reciba una frase por teclado y verifique si la frase es palíndromo. 
# La ejecución termina si la frase ingresada contiene la palabra salir

while True:
    frase = input("Ingresa una frase  para verificar si es palindromo (o 'salir' para terminar): ")
    if "salir" in frase.lower():
        break
    frase_limpia = frase.replace(" ", "").lower()
    if frase_limpia == frase_limpia[::-1]:
        print("La frase es un palíndromo.")
    else:
        print("La frase no es un palíndromo.")
