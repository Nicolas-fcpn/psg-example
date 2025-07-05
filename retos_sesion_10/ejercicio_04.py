# Jane y Jhon llevan saliendo juntos por 4 semanas, 
# cada vez que salen van a comer a un candy bar. 
# Quieren saber que tan compatibles son viendo cuantos platos de comida tienen en común. 
# A continuación tienes los postres que han ido pidiendo en cada salida:
# Jane: Lemon Pie, Brownie, Tarta de Manzana,
#       Helado de Chocolate, Flan
# Jhon: Carrot Cake, Croissant de Chocolate,
#       Lemon Pie, Tarta de Manzana, Pudding
# Si la cantidad de postres que tienen en común es mayor al 50% 
# entonces son compatibles, de lo contrario quieren replantear su relación

postres_jane = {"Lemon Pie", "Brownie", "Tarta de Manzana", "Helado de Chocolate", "Flan"}
print("Postres de Jane:", postres_jane)
postres_jhon = {"Carrot Cake", "Croissant de Chocolate", "Lemon Pie",
                 "Tarta de Manzana", "Pudding"}
print("Postres de Jhon:", postres_jhon)
postres_comunes = postres_jane.intersection(postres_jhon)
print("Postres en común:", postres_comunes)
todos_postres = postres_jane.union(postres_jhon)
print("Todos los postres:", todos_postres)
porcentaje_comun = (len(postres_comunes) / len(todos_postres)) * 100
print("Porcentaje de postres en común:", porcentaje_comun, "%")
prueba = porcentaje_comun > 50
print("¿Son compatibles?", prueba)