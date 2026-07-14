def billetes_de_20(cantidad):
    # Se calcula la cantidad de billetes de 20 soles, redondeando hacia abajo
    billetes = cantidad // 20
    print(f"Se necesitan {billetes} billetes de 20 soles.")

cantidad = int(input("Ingrese la cantidad de dinero en soles: "))
billetes_de_20(cantidad)