# Definimos la cantidad de segundos para cada magnitud de tiempo

seg_semana = 7 * 24 * 60 * 60
seg_dia = 24 * 60 * 60
seg_hora = 60 * 60
seg_min = 60

# Usando división entera, vamos almmacenando las magnitudes de tiempo

total_seg = 987654
semanas = total_seg // seg_semana
seg_restante = total_seg - seg_semana
dias = seg_restante // seg_dia
seg_restante = seg_restante - dias * seg_dia
horas = seg_restante // seg_hora
seg_restante = seg_restante - horas * seg_hora
minutos = seg_restante // seg_min
seg_restante = seg_restante - minutos * seg_min
print(f"{total_seg} segundos equivale a:")
print(f"{semanas} semanas")
print(f"{dias} dias")
print(f"{horas} horas")
print(f"{minutos} minutos")
print(f"{seg_restante} segundos")