# Definimos la cantidad de segundos para cada magnitud de tiempo

seg_semana = 7 * 24 * 60 * 60
seg_dia = 24 * 60 * 60
seg_hora = 60 * 60
seg_min = 60

# Usando división entera, vamos almacenando las magnitudes de tiempo

total_seg = 1000000
semanas = total_seg // seg_semana
seg_restante = total_seg - seg_semana
dias = seg_restante // seg_dia
seg_restante = seg_restante - dias * seg_dia
horas = seg_restante // seg_hora
seg_restante = seg_restante - horas * seg_hora
minutos = seg_restante // seg_min
seg_restante = seg_restante - minutos * seg_min
print(total_seg, "segundos =", semanas, "semana(s)",\
      dias, "dia(s)", horas, "hora(s)", minutos, "minuto(s)",\
        seg_restante, "segundo(s)")