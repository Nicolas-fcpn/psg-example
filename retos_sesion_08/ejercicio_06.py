# De las tuplas de coordenadas
# (x1,y1)=(−20,−20) y (x2,y2)=(40,20)
# Encuentra las coordenadas del punto medio, almacena en una tupla e imprime el resultado

tupla_1 = (-20, -20)
x1, y1 = tupla_1
tupla_2 = (40, 20)
x2, y2 = tupla_2
x = (x1 + x2) / 2
y = (y1 + y2) / 2
punto_medio = (x, y)
print(f"Las coordenadas del punto medio para {tupla_1} y {tupla_2} son: {punto_medio}")