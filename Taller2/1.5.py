def desglose_monedas(c):
    m5 = c // 5
    resto = c % 5
    m2 = resto // 2
    m1 = resto % 2
    print(f"Monedas de 5: {m5}, de 2: {m2}, de 1: {m1}")

cantidad = int(input("Ingrese la cantidad en soles: "))
desglose_monedas(cantidad)