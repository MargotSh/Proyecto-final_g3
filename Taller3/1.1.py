def comparar_numeros(a, b):
    if a > b:
        print(f"{a} es mayor que {b}")
    elif a < b:
        print(f"{a} es menor que {b}")
    else:
        print(f"{a} y {b} son iguales")

# Programa principal
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
comparar_numeros(a, b)
