# Jhon colecciona autos a escala 1:64, tiene los siguientes autos
# {'Ferrari', 'Lamborghini', 'Porsche', 'Bugatti', 'McLaren'}
# Jess tambien colecciona autos a escala 1:64, tiene los siguientes autos
# {'Ferrari', 'Lamborghini', 'Tesla', 'Ford', 'Chevrolet'}
# ¿Que autos tienen en común ambos coleccionistas?, ¿Cuáles son los autos en común?

autos_jhon = {'Ferrari', 'Lamborghini', 'Porsche', 'Bugatti', 'McLaren'}
autos_jess = {'Ferrari', 'Lamborghini', 'Tesla', 'Ford', 'Chevrolet'}

autos_comunes = autos_jhon.intersection(autos_jess)
print("Los autos en común son:", autos_comunes)
