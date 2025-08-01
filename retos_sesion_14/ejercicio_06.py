def separar_pares_impares(numeros):
    pares = []
    impares = []
    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return pares, impares

print ("Separar pares e impares")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Lista original:", lista)
pares, impares = separar_pares_impares(lista)
print("Números pares:", pares)
print("Números impares:", impares)
