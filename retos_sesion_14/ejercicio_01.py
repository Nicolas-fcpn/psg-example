def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

print ("Calcular promedio")
promedio = calcular_promedio([50, 75, 80, 91, 70])
print ("El promedio es:", promedio)

