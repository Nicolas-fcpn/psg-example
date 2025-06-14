# Las notas de un estudiante durante un semestre son:
# 10, 61, 00, 21, 22, 0, 32, 30, 41, 51, 5, 23, 100
# Genera una tupla con los resultados y calcula el promedio

notas = (10, 61, 00, 21, 22, 0, 32, 30, 41, 51, 5, 23, 100)
n = len(notas)
suma = sum(notas)
promedio = suma / n
aprueba = promedio >= 51
print(f"Promedio de notas : {promedio}. Aprobado: {aprueba}")