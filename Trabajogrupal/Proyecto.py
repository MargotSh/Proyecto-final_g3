from datetime import datetime

inventario = {}
movimientos = []

print("========================================")
print(" SISTEMA DE CONTROL DE INVENTARIO VIRCATEX")
print("========================================")

while True:

    print("\n1. Registrar producto")
    print("2. Registrar movimiento")
    print("3. Consultar inventario")
    print("4. Reporte de movimientos")
    print("5. Salir")

    opcion = input("\nSeleccione una opción: ")

    # HU01
    if opcion == "1":

        codigo = input("Código del producto: ").strip()

        if codigo == "":
            print("\nEl código no puede estar vacío.")
            continue

        if codigo in inventario:
            print("\nEl producto ya existe.")
            continue

        descripcion = input("Descripción: ").strip()

        if descripcion == "":
            print("\nLa descripción no puede estar vacía.")
            continue

        inventario[codigo] = {
            "descripcion": descripcion,
            "stock": 0
        }

        print("\nProducto registrado correctamente.")

    # HU02 + HU03
    elif opcion == "2":

        print("\nTipo de movimiento")
        print("1. Ingreso")
        print("2. Salida")

        tipo = input("Seleccione: ")

        codigo = input("Código del producto: ").strip()

        if codigo not in inventario:
            print("\nProducto no encontrado.")
            continue

        cantidad = int(input("Cantidad: "))

        if cantidad <= 0:
            print("\nLa cantidad debe ser mayor que cero.")
            continue

        fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        if tipo == "1":

            inventario[codigo]["stock"] += cantidad

            movimientos.append({
                "tipo": "Ingreso",
                "codigo": codigo,
                "cantidad": cantidad,
                "fecha": fecha
            })

            print("\nIngreso registrado correctamente.")

        elif tipo == "2":

            if inventario[codigo]["stock"] < cantidad:
                print("\nStock insuficiente.")
                continue

            inventario[codigo]["stock"] -= cantidad

            movimientos.append({
                "tipo": "Salida",
                "codigo": codigo,
                "cantidad": cantidad,
                "fecha": fecha
            })

            print("\nSalida registrada correctamente.")

        else:
            print("\nTipo de movimiento inválido.")

    # HU04
    elif opcion == "3":

        print("\n========== INVENTARIO ==========")

        if len(inventario) == 0:
            print("No existen productos registrados.")
        else:
            print("{:<10} {:<25} {:>10}".format(
                "Código", "Descripción", "Stock"))
            print("-" * 50)

            for codigo, datos in inventario.items():
                print("{:<10} {:<25} {:>10}".format(
                    codigo,
                    datos["descripcion"],
                    datos["stock"]
                ))

    # HU05
    elif opcion == "4":

        print("\n====== REPORTE DE MOVIMIENTOS ======")

        if len(movimientos) == 0:
            print("No existen movimientos registrados.")
        else:

            print("{:<10} {:<10} {:>10} {:<20}".format(
                "Código", "Tipo", "Cantidad", "Fecha"))

            print("-" * 70)

            for mov in movimientos:
                print("{:<10} {:<10} {:>10} {:<20}".format(
                    mov["codigo"],
                    mov["tipo"],
                    mov["cantidad"],
                    mov["fecha"]
                ))

    elif opcion == "5":
        print("\nPrograma finalizado.")
        break

    else:
        print("\nOpción inválida.")
