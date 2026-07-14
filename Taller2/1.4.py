def fuerza_gravitacional(m1, m2, r):
    # Fórmula: F = G * (m1 * m2) / r^2
    G = 6.67e-11  # Constante gravitacional
    fuerza = G * (m1 * m2) / (r ** 2)
    print(f"La fuerza gravitacional es: {fuerza} N")

m1 = float(input("Ingrese masa 1 (kg): "))
m2 = float(input("Ingrese masa 2 (kg): "))
r = float(input("Ingrese distancia entre masas (m): "))
fuerza_gravitacional(m1, m2, r)