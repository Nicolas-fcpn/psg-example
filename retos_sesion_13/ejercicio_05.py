# Imprimir un tablero de ajedrez de 8x8 con los caracteres # y *
print("Tablero de ajedrez 8x8:")
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("# ", end=" ")
        else:
            print("* ", end=" ")
    print()