def crear_mensaje(nombre, nota):
    # Generamos el mensaje exacto como se requiere
    print(f"Soy {nombre} y mi nota es {nota}")

nombre = input("Ingrese su nombre: ")
nota = float(input("Ingrese su nota: "))
crear_mensaje(nombre, nota)