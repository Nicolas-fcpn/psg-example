print ("Operador XNOR")
A = True
B = True
C = (not ((A or B) and not (A and B)))
print(f"{A=} {B=} A XNOR B = {C}")
A = True
B = False
C = (not ((A or B) and not (A and B)))
print(f"{A=} {B=} A XNOR B = {C}")
A = False
B = True
C = (not ((A or B) and not (A and B)))
print(f"{A=} {B=} A XNOR B = {C}")
A = False
B = False
C = (not ((A or B) and not (A and B)))
print(f"{A=} {B=} A XNOR B = {C}")