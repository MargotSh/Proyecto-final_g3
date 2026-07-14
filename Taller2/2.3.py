import math

def area_circulo(radio):
    # Fórmula: A = π * r^2
    area = math.pi * (radio ** 2)
    print(f"El área del círculo es: {area:.2f}")

radio = float(input("Ingrese el radio del círculo: "))
area_circulo(radio)