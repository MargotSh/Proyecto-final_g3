def es_multiplo(a, b):
    if b == 0:
        print("No se puede dividir entre cero.")
        return
    if a % b == 0:
        print("Verdadero (V): A es múltiplo de B")
    else:
        print("Falso (F): A no es múltiplo de B")

# Programa principal
a = int(input("Ingrese el primer número (A): "))
b = int(input("Ingrese el segundo número (B): "))
es_multiplo(a, b)
