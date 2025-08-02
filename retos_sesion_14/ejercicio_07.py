print("==========TRES EN RAYA==========")

def inicializar_tablero():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    print("##### JUEGO NUEVO #####")
    for fila in tablero:
        print(fila)
    print("Juega X")
    return tablero

def tres_en_raya(jugador, fila, columna):
    if tablero[fila][columna] == ' ':
        tablero[fila][columna] = jugador
        for fila in tablero:
            print(fila)
        if verificar_ganador(tablero, jugador):
            print(f"¡{jugador} ha ganado!")
            print("##### FIN DEL JUEGO #####")
            return
        elif verificar_empate(tablero):
            print("¡Es un empate!")
            print("##### FIN DEL JUEGO #####")
            return
        else:
            siguiente_jugador = "O" if jugador == "X" else "X"
            print(f"Juega {siguiente_jugador}")
    else:
        print("Casilla ocupada, elige otra.")

def verificar_ganador(tablero, jugador):
    # Verificar filas
    for fila in tablero:
        if all(casilla == jugador for casilla in fila):
            return True
    # Verificar columnas
    for columna in range(3):
        if all(tablero[fila][columna] == jugador for fila in range(3)):
            return True
    # Verificar diagonales
    if all(tablero[i][i] == jugador for i in range(3)) or \
       all(tablero[i][2 - i] == jugador for i in range(3)):
        return True
    return False

def verificar_empate(tablero):
    return all(casilla != ' ' for fila in tablero for casilla in fila)

# Ejemplo de uso - Gana X
tablero = inicializar_tablero()
tres_en_raya("X", 0, 0)
tres_en_raya("O", 1, 1)
tres_en_raya("X", 0, 1)
tres_en_raya("O", 2, 2)
tres_en_raya("X", 0, 2)

# Ejemplo de uso - Gana O
tablero = inicializar_tablero()
tres_en_raya("X", 0, 2)
tres_en_raya("O", 1, 0)
tres_en_raya("X", 1, 2)
tres_en_raya("O", 2, 2)
tres_en_raya("X", 2, 0)
tres_en_raya("O", 1, 1)
tres_en_raya("X", 2, 1)
tres_en_raya("O", 0, 0)

# Ejemplo de uso - Gana O
tablero = inicializar_tablero()
tres_en_raya("X", 0, 2)
tres_en_raya("O", 1, 0)
tres_en_raya("X", 1, 2)
tres_en_raya("O", 2, 2)
tres_en_raya("X", 2, 0)
tres_en_raya("O", 1, 1)
tres_en_raya("X", 2, 1)
tres_en_raya("O", 0, 0)

# Ejemplo de uso - Empate
tablero = inicializar_tablero()
tres_en_raya("X", 0, 0)
tres_en_raya("O", 1, 1)
tres_en_raya("X", 0, 2)
tres_en_raya("O", 0, 1)
tres_en_raya("X", 2, 0)
tres_en_raya("O", 1, 0)
tres_en_raya("X", 1, 2)
tres_en_raya("O", 2, 2)
tres_en_raya("X", 2, 1)

# Ejemplo de uso - Gana X con casillas ocupadas
tablero = inicializar_tablero()
tres_en_raya("X", 0, 0)
tres_en_raya("O", 0, 0)
tres_en_raya("O", 1, 1)
tres_en_raya("X", 1, 1)
tres_en_raya("X", 0, 1)
tres_en_raya("O", 2, 2)
tres_en_raya("X", 0, 2)