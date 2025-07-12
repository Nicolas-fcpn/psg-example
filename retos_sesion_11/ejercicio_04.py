# Gestión de hábitats en peligro: Crea un diccionario que asocie especies animales 
# en peligro de extinción con información sobre sus hábitats amenazados, 
# lo que permite priorizar la protección de áreas críticas para la supervivencia de estas especies

habitats_y_especies = {"polo norte" : {
    "especies": {"oso polar", "morsa", "ballena"}
  }, "amazonas" : {
    "especies": {"tigre", "mono", "guacamayo"}
  }
}

print("Diccionario de hábitats y especies en peligro:")
print(habitats_y_especies)

# Añade al diccionario 2 habitats más usando update() con 2 especies cada uno
habitats_y_especies.update({
    "sabana africana": {
        "especies": {"león", "rinoceronte"}
    },
    "bosques asiáticos": {
        "especies": {"tigre", "panda"}
    }
})

print("Diccionario de hábitats y especies en peligro actualizado:")
print(habitats_y_especies)

# Existe en el diccionario el habitat 'amazonas'?
existe_amazonas = 'amazonas' in habitats_y_especies
print("¿Existe el hábitat 'amazonas'?", existe_amazonas)

# Añade al amazonas la especie 'anaconda'
habitats_y_especies['amazonas']['especies'].add('anaconda')
print("Diccionario de hábitats y especies en peligro actualizado:")
print(habitats_y_especies)
