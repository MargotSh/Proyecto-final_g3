import math

def radianes_a_gms(radianes):
    # Fórmula: grados = radianes * (180 / π)
    grados = math.degrees(radianes)
    g = int(grados)
    minutos = (grados - g) * 60
    m = int(minutos)
    s = (minutos - m) * 60
    print(f"{g}° {m}' {s}\"")

rad = float(input("Ingrese el ángulo en radianes: "))
radianes_a_gms(rad)