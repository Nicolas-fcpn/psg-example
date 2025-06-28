# Crear una lista de personas con 10 nombres de personas

lista_nombres = ["Juan", "María", "Pedro", "Pablo", "Paola", "Julia",\
                 "José", "Luís", "Miriam", "Daniela"]
print("Lista de nombres")
print(lista_nombres)

# Obtener una sub lista de 5 a 9 con saltos de 2 en 2
print("Sub lista de 5 a 9, salto 2")
longitud_lista = len(lista_nombres)
sub_lista = lista_nombres[4:longitud_lista:2]
print(sub_lista)

# Buscar si existe el nombre "José" en la lista original
print("Buscar palabra 'José' en la lista original")
palabra = "José"
print("¿La palabra:", palabra, "está en la lista original?")
print(palabra in lista_nombres)

# Ordenar la sub lista alfabéticamente a-z
print("Sub lista ordenada")
sub_lista.sort()
print(sub_lista)

# Ordenar la lista original alfabéticamente descendente z-a
print("Lista original en orden descendente")
lista_nombres.sort(reverse=True)
print(lista_nombres)