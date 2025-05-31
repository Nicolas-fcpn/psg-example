print("Tabla de verdad")
print ("A = Tarjeta valida")
print ("B = Huella dactilar")
print ("C = La puerta se abre")
print ("El operador lógico es XOR")
print ("C es True cuando A es True o B es True, pero no ambos")
A = True
B = True
C = (A or B) and not (A and B)
print(f"{A=} {B=}, A XOR B = {C}")
A = True
B = False
C = (A or B) and not (A and B)
print(f"{A=} {B=}, A XOR B = {C}")
A = False
B = True
C = (A or B) and not (A and B)
print(f"{A=} {B=}, A XOR B = {C}")
A = False
B = False
C = (A or B) and not (A and B)
print(f"{A=} {B=}, A XOR B = {C}")