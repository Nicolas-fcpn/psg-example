def calculadora():
    while True:
        try:
            num1 = input("Ingrese el primer número (o 'salir' para terminar): ")
            if num1.lower() == "salir":
                print("Saliendo de la calculadora.")
                break
            num1 = float(num1)
            num2 = float(input("Ingrese el segundo número: "))
            print("Seleccione la operación:")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            operacion = input("Ingrese el número de la operación: ")
            if operacion == "1":
                resultado = num1 + num2
                print(f"Resultado: {resultado}")
            elif operacion == "2":
                resultado = num1 - num2
                print(f"Resultado: {resultado}")
            elif operacion == "3":
                resultado = num1 * num2
                print(f"Resultado: {resultado}")
            elif operacion == "4":
                try:
                    resultado = num1 / num2
                    print(f"Resultado: {resultado}")
                except ZeroDivisionError:
                    print("Error: No se puede dividir entre cero.")
            else:
                print("Operación no válida.")
        except ValueError:
            print("Error: Entrada no válida. Por favor, ingrese números.")
        except Exception as e:
            print(f"Error inesperado: {e}")

calculadora()