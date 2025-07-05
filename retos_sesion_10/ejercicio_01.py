# Elimina los elementos de oficina repetidos de la cadena

cadena = "📎📐📏✏️🖊️🖋️📎📌📏📇🗂️📁📌🗃️✏️📂🖇️"

print("Cadena original:", cadena)
conjunto = set(cadena)
print("Cadena a conjunto")
print(conjunto)
cadena_sin_repetidos = ''.join(conjunto)
print("Cadena sin repetidos:", cadena_sin_repetidos)