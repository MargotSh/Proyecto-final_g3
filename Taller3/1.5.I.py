def obtener_bono_extranjero(nacionalidad):
    if nacionalidad.upper() == 'E':
        return 500
    else:
        return 0

def obtener_incremento_por_edad(edad):
    if 15 <= edad <= 20:
        return 1400
    elif 21 <= edad <= 25:
        return 1500
    elif 26 <= edad <= 30:
        return 1200
    else:
        return 800

def calcular_sueldo_final(edad, nacionalidad):
    sueldo_base = 2500
    bono = obtener_bono_extranjero(nacionalidad)
    incremento = obtener_incremento_por_edad(edad)
    sueldo_final = sueldo_base + bono + incremento
    return sueldo_final

# Programa principal
def main():
    edad = int(input("Ingrese la edad del jugador: "))
    nacionalidad = input("Ingrese la nacionalidad del jugador (E: Extranjero, N: Nacional): ")
    sueldo = calcular_sueldo_final(edad, nacionalidad)
    print(f"El sueldo final del jugador es: {sueldo:.2f} soles")

main()
