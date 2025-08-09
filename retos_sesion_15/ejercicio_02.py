class FrutaNoValidaError(Exception):
    pass
def construir_canasta():
    frutas_permitidas = ["🍅", "🍇", "🍈", "🍉", "🍊", "🍌", "🍍", "🍑"]
    canasta = []
    while True:
        fruta = input("Ingrese una fruta (o 'salir' para terminar): ")
        if fruta.lower() == "salir":
            print("Finalizando el programa.")
            break
        if fruta not in frutas_permitidas:
            raise FrutaNoValidaError(f"La fruta '{fruta}' no está permitida.")
        canasta.append(fruta)
    print("Canasta de frutas:", canasta)
try:
    construir_canasta()
except FrutaNoValidaError as e:
    print("Error:", e)