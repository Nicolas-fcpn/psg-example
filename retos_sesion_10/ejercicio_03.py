# Tienes dos listas: clientes que compraron en la 
# tienda física y clientes que compraron online.

tienda_fisica = ["Ana", "Luis", "Pedro", "María", "Juan"]
tienda_online = ["Pedro", "María", "Ana", "Carlos", "Laura"]
print("Clientes de la tienda física:", tienda_fisica)
print("Clientes de la tienda online:", tienda_online)

print("a. Quiénes compraron en ambos canales.")
conjunto_fisica = set(tienda_fisica)
conjunto_online = set(tienda_online)
conjunto_compraron_ambos = conjunto_fisica.intersection(conjunto_online)
print("Clientes que compraron en ambos canales:", conjunto_compraron_ambos)
print("b. Quiénes compraron solo en la tienda física.")
conjunto_solo_fisica = conjunto_fisica.difference(conjunto_online) 
print("Clientes que compraron solo en la tienda física:", conjunto_solo_fisica)
print("c. Quiénes compraron solo online.")
conjunto_solo_online = conjunto_online.difference(conjunto_fisica)
print("Clientes que compraron solo online:", conjunto_solo_online)