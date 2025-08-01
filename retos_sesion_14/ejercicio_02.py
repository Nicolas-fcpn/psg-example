def calcular(num1, num2, operacion):
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        return num1 / num2
    else:
        return "Operación no válida"

print ("Calculadora")
argumento_1 = 10
print("Argumento 1:", argumento_1)
argumento_2 = 5
print("Argumento 2:", argumento_2)
operador = "+"
print("Operador:", operador)
resultado = calcular(argumento_1, argumento_2, operador)
print("El resultado es:", resultado)
