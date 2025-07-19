# Crea una calculadora por consola que realice las operaciones de suma, 
# resta, multiplicación y división. Las operaciones se ingresan por teclado separadas por comas en el siguiente formato:
# numero1, número2, operación
# ejemplo: 10, 5, +
# verifica si la operación solicitada es válida y muestra el resultado

cadena = input("Operación: ")
numero1, numero2, operacion = cadena.split(", ")
numero1 = float(numero1)
numero2 = float(numero2)
if operacion == "+":
    print("-------------")
    print("Resultado:", numero1 + numero2)
elif operacion == "-":
    print("-------------")
    print("Resultado:", numero1 - numero2)
elif operacion == "*":
    print("-------------")
    print("Resultado:", numero1 * numero2)
elif operacion == "/":
    print("-------------")
    print("Resultado:", numero1 / numero2)
else:
    print("-------------")
    print("Operación no válida")
