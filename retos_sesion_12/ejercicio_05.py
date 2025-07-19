# Tienes una app para gestionar contactos, cada contacto tiene un nombre y un número de teléfono,
# si el contacto tiene un número de teléfono válido (11 dígitos incluyendo el código de país) y 
# un nombre valido se guarda en la lista de contactos y muestra el mensaje Contacto guardado, 
# caso contrario se muestra el mensaje de error Datos incorrectos.
# El nombre y el numero de teléfono se ingresan por teclado
# Verifica si el el numero de teléfono es válido
# Verifica si el nombre válido usando truthiness
# Nombre: Juan Perez
# Teléfono: +591123456789
# -------------
# Contacto guardado
# Nombre: 
# Teléfono: +123456789
# -------------
# Datos incorrectos

lista_contactos = {}
nombre_contacto = input("Introduce el nombre del contacto: ")
telefono_contacto = input("Introduce el número de teléfono del contacto: ")
if len(telefono_contacto) == 12 and telefono_contacto.startswith("+") and nombre_contacto:
    print("-------------")
    print("Contacto guardado")
    lista_contactos[telefono_contacto] = nombre_contacto
else:
    print("-------------")
    print("Datos incorrectos")
