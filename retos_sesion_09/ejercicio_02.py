# De la siguiente lista [5,4,3,2,2,2,0,0,1,2] obtener una sub lista inversa utilizando saltos de 3 en 3

lista_2 = [5,4,3,2,2,2,0,0,1,2]
longitud = len(lista_2)
print(lista_2[-1:-longitud-1:-3])
