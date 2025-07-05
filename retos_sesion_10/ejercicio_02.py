# El dueño de una tienda de ropa deportiva ha comprado ropa formal y 
# quiere abrir una nueva tienda que combine ambos estilos. 
# Crea un conjunto con las prendas de ambos tipos con las listas de prendas

ropa_deportiva = ["Short", "Playera", "Sudadera", "Tenis", "Short", "Calcetines"]
ropa_formal = ["Saco", "Corbata", "Pantalón de vestir", "Zapatos", "Calcetines"]
print("Ropa deportiva:", ropa_deportiva)
print("Ropa formal:", ropa_formal)
conjunto = set(ropa_deportiva)
conjunto.update(ropa_formal)
print("Conjunto de prendas de ambos tipos:", conjunto)