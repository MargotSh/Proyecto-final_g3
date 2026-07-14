def segundos_a_hms(t):
    horas = t // 3600
    t = t % 3600
    minutos = t // 60
    segundos = t % 60
    print(f"{horas}h {minutos}m {segundos}s")

t = int(input("Ingrese el tiempo en segundos: "))
segundos_a_hms(t)