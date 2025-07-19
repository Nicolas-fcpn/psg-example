# Tienes una app para gestionar tareas de 4 usuarios, 
# para acceder los usuarios deben iniciar sesión con un nombre de usuario y 
# una contraseña introducidos por teclado.
# Define los siguientes usuarios y contraseñas utilizando la estructura de datos mas adecuada.
# Usuario: admin, Contraseña: admin123
# Usuario: user1, Contraseña: user123
# Usuario: user2, Contraseña: user123
# Usuario: user3, Contraseña: user123
# Verifica si el usuario inició sesión para acceder a la app y 
# muestra el mensaje Acceso Aprobado, caso contrario muestra el mensaje de error Acceso Denegado.

usuarios = {"admin": "admin123","user1": "user123","user2": "user123","user3": "user123"}

usuario = input("Introduce tu nombre de usuario: ")
contrasena = input("Introduce tu contraseña: ")

if usuario in usuarios and usuarios[usuario] == contrasena:
    print("Acceso Aprobado")
else:
    print("Acceso Denegado")
