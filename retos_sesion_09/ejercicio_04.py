# Parte 1: Una dulcería tiene 2 listas una con los productos y otra con los precios

lista_productos = ['Oreo', 'Chizitos', 'Bon Bon Bum', 'Powerade', 'Snickers', 'Smarties', 'TriDent']
lista_precios = [2.50, 1.50, 1.00, 7.00, 12.00, 4.50, 5.50]

print('Listas originales')
print(lista_productos)
print(lista_precios)

# i. Agregar 2 productos nuevos al final de las listas

print('Lista con productos agregados')
lista_productos.extend(['Fanta', 'Chips Ahoy'])
lista_precios.extend([6.00, 3.00])
print(lista_productos)
print(lista_precios)

# ii. Eliminar el producto con el nombre "Bon Bon Bum" de las listas

print('Listas con "Bon Bon Bum" eliminado')
lista_productos.remove('Bon Bon Bum')
lista_precios.remove(1.00)
print(lista_productos)
print(lista_precios)

# iii. ¿Cuánto cuesta el producto "Oreo" y "Chizitos"?

print('Precios de "Oreo" y "Chizitos"')
producto_1 = 'Oreo'
producto_2 = 'Chizitos'
indice_prod_1 = lista_productos.index(producto_1)
indice_prod_2 = lista_productos.index(producto_2)
precio_prod_1 = lista_precios[indice_prod_1]
precio_prod_2 = lista_precios[indice_prod_2]
print('Precio de', producto_1, "=", precio_prod_1)
print('Precio de', producto_2, "=", precio_prod_2)

# iv. ¿Cuál es el producto más caro y el más barato?

print('Producto más caro y más barato')
precio_max = max(lista_precios)
precio_min = min(lista_precios)
indice_precio_max = lista_precios.index(precio_max)
indice_precio_min = lista_precios.index(precio_min)
producto_precio_max = lista_productos[indice_precio_max]
producto_precio_min = lista_productos[indice_precio_min]
print('Producto más caro:', producto_precio_max, "precio =", precio_max)
print('Producto más barato:', producto_precio_min, "precio =", precio_min)

# 5. ¿Cuántos productos tienes en total?

print('Cantidad total de productos')
print(len(lista_productos), 'productos')

# 6. ¿Cuanto cuestan todos los productos?

print('Valor total de los producto')
print(sum(lista_precios), "Bs.")

# 7. Ordena los productos y precios del más barato al más caro

# 8. Eliminar todos los productos de las listas

print('Eliminar todos los productos de las listas')
lista_productos.clear()
print('Lista de productos vacía:', lista_productos)
lista_precios.clear()
print('Lista de precios vacía:', lista_precios)