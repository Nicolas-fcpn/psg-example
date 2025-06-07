# Agregar 5 Ejemplos con otras funciones no vistas en la sesión

print ("1. Función removeprefix()")
cadena = "automático"
sin_prefijo = cadena.removeprefix("auto")
print (cadena)
print (sin_prefijo)

print ("2. Función endswith()")
cadena = "automatización"
termina_en = cadena.endswith("ción")
print (cadena)
print (termina_en)
cadena = "automatizado"
termina_en = cadena.endswith("ción")
print (cadena)
print (termina_en)

print ("3. Función encode()")
cadena = "automatización"
cad_cod = cadena.encode(encoding='utf-8')
print (cadena)
print (cad_cod)

print ("4. Función count()")
cadena = "bla bla bla bla"
print (cadena)
print (cadena.count('bla'))
cadena = "blableblebla"
print (cadena)
print (cadena.count('bla'))

print ("5. Función center()")
cadena = 'apoteósico'
print(cadena.center(30))
print(cadena.center(30, '-'))
print(cadena.center(30, '*'))