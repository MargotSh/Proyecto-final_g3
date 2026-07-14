from datetime import datetime

# Diccionario para almacenar el inventario
inventario = {}

print("========================================")
print(" SISTEMA DE CONTROL DE INVENTARIO")
print("========================================")

while True:

    print("\n1. Ingreso de productos")
    print("2. Salida de productos")
    print("3. Reporte de Inventario")
    print("4. Salir")

    opcion = input("\nSeleccione una opción: ")

    # INGRESO
    if opcion == "1":

        codigo = input("Código del producto: ")
        descripcion = input("Descripción: ")
        cantidad = int(input("Cantidad a ingresar: "))

        if codigo in inventario:
            inventario[codigo]["stock"] += cantidad
        else:
            inventario[codigo] = {
                "descripcion": descripcion,
                "stock": cantidad
            }

        fecha = datetime.now()

        print("\nIngreso registrado correctamente.")
        print("Fecha y hora:", fecha.strftime("%d/%m/%Y %H:%M:%S"))

    # SALIDA
    elif opcion == "2":

        codigo = input("Código del producto: ")

        if codigo in inventario:

            cantidad = int(input("Cantidad a retirar: "))

            if inventario[codigo]["stock"] >= cantidad:

                inventario[codigo]["stock"] -= cantidad

                fecha = datetime.now()

                print("\nSalida registrada correctamente.")
                print("Fecha y hora:",
                      fecha.strftime("%d/%m/%Y %H:%M:%S"))

            else:
                print("\nStock insuficiente.")

        else:
            print("\nProducto no encontrado.")

    # REPORTE
    elif opcion == "3":

        print("\n========= REPORTE DE INVENTARIO =========")

        if len(inventario) == 0:
            print("No existen productos registrados.")
        else:

            print("{:<10} {:<25} {:>10}".format(
                "Código", "Descripción", "Stock"))

            print("-"*50)

            for codigo, datos in inventario.items():
                print("{:<10} {:<25} {:>10}".format(
                    codigo,
                    datos["descripcion"],
                    datos["stock"]
                ))

        print("=========================================")

    # SALIR
    elif opcion == "4":

        print("\nREPORTE FINAL")

        print("{:<10} {:<25} {:>10}".format(
            "Código", "Descripción", "Stock"))

        print("-"*50)

        for codigo, datos in inventario.items():
            print("{:<10} {:<25} {:>10}".format(
                codigo,
                datos["descripcion"],
                datos["stock"]
            ))

        print("\nPrograma finalizado.")
        break

    else:
        print("\nOpción inválida.")
        #prueba