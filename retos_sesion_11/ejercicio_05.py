# Eres NOE y tienes que guardar dos animales de cada especie en un arca, crea un diccionario con las especies
# {"🐶" : 2, "🐱" : 2, "🐯" : 2, "🐵" : 2, "🦄" : 0, "🦒" : 1}

especies_animales = {
    '🐶': 2,
    '🐱': 2,
    '🐯': 2,
    '🐵': 2,
    '🦄': 0,
    '🦒': 1
}
print("Diccionario de especies animales de Noé:")
print(especies_animales)

# Añade al arca 3 especies más usando update()
especies_animales.update({
    '🐮': 2,
    '🐰': 2,
    '🐍': 2
})
print("Diccionario actualizado de especies animales de Noé:")
print(especies_animales)

# Toma lista de los animales en el arca iterando el diccionario
items = especies_animales.items()
items = list(items) # Convertir a lista
print("Lista de los animales:")
print(items, type(items))

# Existe en el arca la especie 'dragon' 🐲?
existe_dragon = '🐲' in especies_animales
print("¿Existe la especie dragón?", existe_dragon)

# Elimina la especie unicornio del arca
del especies_animales['🦄']
print("Diccionario actualizado de especies animales de Noé:")
print(especies_animales)

# Modifica el valor de la especie jirafa por 2
especies_animales['🦒'] = 2
print("Diccionario actualizado de especies animales de Noé:")
print(especies_animales)

# Vacía el arca después del diluvio
especies_animales.clear()
print("Arca vacía después del diluvio:")
print(especies_animales)
