# Subproblema 1: Contar la cantidad total de dígitos en una cadena
def contar_digitos(cadena):
    # Retorna la cantidad total de caracteres en la cadena numérica.
    return len(cadena)

# Subproblema 2 (Versión 1): Contar repeticiones usando bucles (estructura for)
def contar_repetidos_bucle(cadena, digito):
    # Cuenta cuántas veces aparece un dígito en la cadena usando un bucle forself.
    contador = 0
    for caracter in cadena:
        if caracter == str(digito):
            contador += 1
    return contador

# Subproblema 2 (Versión 2): Contar repeticiones usando método .count()
def contar_repetidos_count(cadena, digito):
    # Cuenta cuántas veces aparece un dígito en la cadena usando .count()
    return cadena.count(str(digito))

# Ejemplo de uso
numero = "45776574367321367112"
digito_a_contar = "7"

# Mostrar resultados
print("Número analizado:", numero)
print("Dígito a contar:", digito_a_contar)
print("Cantidad total de dígitos:", contar_digitos(numero))
print("Repeticiones con bucle for:", contar_repetidos_bucle(numero, digito_a_contar))
print("Repeticiones con .count():", contar_repetidos_count(numero, digito_a_contar))
