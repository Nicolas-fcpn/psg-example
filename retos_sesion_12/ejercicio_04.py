# Una tienda ofrece descuentos a sus clientes, si el cliente tiene una edad mayor a 60 años y 
# tiene una compra mayor a 1000, se le aplica un descuento del 20%, 
# si el cliente tiene una edad entre 18 y 60 años y tiene una compra mayor a 500 se le aplica un descuento del 10%, 
# si no cumple ninguna condición se le aplica un descuento del 2%

edad = int(input("Introduce tu edad: "))
compra = int(input("Introduce el monto de tu compra: "))

if edad > 60 and compra > 1000:
    descuento = 0.2
elif edad >= 18 and edad <= 60 and compra > 500:
    descuento = 0.1
else:
    descuento = 0.02

descuento_porcentual = int(descuento * 100)
print(f"Tu descuento es del {descuento_porcentual}%")
monto_descuento = compra * descuento
print("El monto de tu descuento es:", monto_descuento)
print("El monto final a pagar es:", compra - monto_descuento)