def clave_es_valida_for_sin_reversed(clave):
    clave_str = str(clave)
    longitud = len(clave_str)

    if longitud < 4:
        return False

    contador = 0
    digito_3 = 0
    digito_4 = 0

    for caracter in clave_str:
        contador += 1
        posicion_derecha = longitud - contador + 1

        if posicion_derecha == 3:
            digito_3 = int(caracter)
        elif posicion_derecha == 4:
            digito_4 = int(caracter)

    suma = digito_3 + digito_4
    return suma % 2 == 0


# Ejemplo de uso
clave = 4628

print("\n--- Validación de clave usando FOR sin reversed ---")
print("Clave ingresada:", clave)
if clave_es_valida_for_sin_reversed(clave):
    print("La clave es válida.")
else:
    print("La clave NO es válida.")
