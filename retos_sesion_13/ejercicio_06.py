# Crea un ciclo infinito que reciba un número por teclado y verifique si el número es múltiplo de 7.
# La ejecución termina si se ingresa el número 0
while True:
    numero = int(input("Ingresa un número (0 para salir): "))
    if numero == 0:
        break
    if numero % 7 == 0:
        print(f"{numero} es múltiplo de 7.")
    else:
        print(f"{numero} no es múltiplo de 7.")
