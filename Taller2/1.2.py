import math

def area_circulo(radio):
    # Fórmula del área de un círculo: A = π * r^2
    area = math.pi * (radio ** 2)
    print(f"Área del círculo: {area}")

radio = float(input("Ingrese el radio del círculo: "))
area_circulo(radio)
