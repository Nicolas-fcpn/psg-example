def contar_vocales(cadena):
    contador = 0
    for letra in cadena:
        if letra.lower() in "aeiou":
            contador += 1
    return contador

print ("Contar vocales")
texto = "Python Study Group es un grupo de estudio"
resultado = contar_vocales(texto)
print("La cantidad de vocales en '", texto, "' es:", resultado)