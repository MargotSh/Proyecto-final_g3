def mensaje_por_edad(nombre, edad):
    if 0 <= edad <= 2:
        print(f"{nombre} es un infante")
    elif 3 <= edad <= 10:
        print(f"{nombre} es un niño")
    elif 11 <= edad <= 13:
        print(f"{nombre} es púber")
    elif 14 <= edad <= 18:
        print(f"{nombre} es adolescente")
    elif 19 <= edad <= 59:
        print(f"{nombre} es adulto")
    elif edad >= 60:
        print(f"{nombre} es anciano")
    else:
        print("Edad inválida")

# Programa principal
nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))
mensaje_por_edad(nombre, edad)
