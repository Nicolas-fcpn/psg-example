# Crea un diccionario con la siguiente tupla de especies animales
# (('canino', '🐶') , ('felino','🐱') , ('aves',['🐦','🦅']))

especies_animales = {
    'canino': '🐶',
    'felino': '🐱',
    'aves': ['🐦', '🦅']
}
print("Diccionario de especies animales:")
print(especies_animales, type(especies_animales))

# Del diccionario obtén y elimina el valor de la clave 'aves'
aves = especies_animales.pop('aves')
print(aves, type(aves))

# Modifica el valor de la clave 'felino' por '🐈'
especies_animales['felino'] = '🐈'
print("Diccionario modificado:")
print(especies_animales)

# Cambia la clave canino por caninos y su valor por ['🐶','🐕']
especies_animales['caninos'] = ['🐶', '🐕']
del especies_animales['canino']
print("Diccionario modificado:")
print(especies_animales)
