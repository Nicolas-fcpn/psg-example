# Ingresa una pregunta por teclado y almacena el valor en una tupla

pregunta = (input('Ingrese la pregunta: '),)

# Concatena las tupla

concatenado = ('¿',) + pregunta + ('?',)

# Imprime el resultado concatenado

print(concatenado)

# Repite la tupla concatenada 2 veces e imprime el nuevo resultado

repetir = concatenado * 2

print(repetir)