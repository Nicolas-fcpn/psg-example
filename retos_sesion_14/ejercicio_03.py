def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)

print ("Llamar función")
n = 10
resultado = lucas(n)
print("El número de Lucas", n, "es:", resultado)