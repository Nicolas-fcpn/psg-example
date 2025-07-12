# Crea un diccionario de alimentos y que animales domésticos lo consumen, por ejemplo
# {"carne" : ["gato", "perro"], "zanahoria" : ["conejo"] }
# Añade al diccionario 4 alimentos más, usando update(clave=valor)

alimentos = {"carne": ["gato", "perro"], "zanahoria": ["conejo"]}
print("Diccionario inicial, alimentos:", alimentos)

alimentos.update({"pescado": ["gato"], "maíz": ["loro", "conejo", "hamster"], 
                  "manzana": ["loro", "hamster"], "trigo": ["hamster", "conejo"]})
print("Diccionario actualizado:", alimentos)

# Existe en el diccionario de alimentos la comida 'trigo'?
prueba_logica = "trigo" in alimentos
print("¿Existe la comida 'trigo' en el diccionario de alimentos?", prueba_logica)

# Elimina la comida 'zanahoria' del diccionario de alimentos
del alimentos["zanahoria"]
print("Diccionario después de eliminar 'zanahoria':", alimentos)    