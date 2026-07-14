# Subproblema 1: Calcular el sueldo después de N años
def calcular_sueldo_final(sueldo_inicial, tipo_trabajador, años):
    """
    Calcula el sueldo acumulado de un trabajador después de N años
    considerando los aumentos anuales según el tipo de trabajador:
    - Gerente (g): 14% anual, 18% cada 4 años
    - Empleado (e): 8% anual, 12% cada 4 años
    """
    sueldo = sueldo_inicial

    for año in range(1, años + 1):
        # Determinar el porcentaje según tipo y si es múltiplo de 4
        if tipo_trabajador == 'g':
            if año % 4 == 0:
                porcentaje = 0.18
            else:
                porcentaje = 0.14
        elif tipo_trabajador == 'e':
            if año % 4 == 0:
                porcentaje = 0.12
            else:
                porcentaje = 0.08

        # Aumentar el sueldo acumulativo
        sueldo *= (1 + porcentaje)

    return sueldo

# Subproblema 2: Calcular el porcentaje total de aumento respecto al sueldo original
def calcular_porcentaje_aumento(sueldo_inicial, sueldo_final):
    """
    Calcula el porcentaje de aumento total en relación al sueldo inicial.
    """
    aumento = sueldo_final - sueldo_inicial
    porcentaje_aumento = (aumento / sueldo_inicial) * 100
    return porcentaje_aumento

# Ejemplo de uso
sueldo_inicial = 3000
tipo = 'e'  # 'g' para gerente, 'e' para empleado
años = 6

sueldo_final = calcular_sueldo_final(sueldo_inicial, tipo, años)
porcentaje = calcular_porcentaje_aumento(sueldo_inicial, sueldo_final)

# Mostrar resultados
print("\n--- Cálculo de sueldo ---")
print("Sueldo inicial:", sueldo_inicial)
print("Años:", años)
print("Tipo de trabajador:", "Gerente" if tipo == 'g' else "Empleado")
print("Sueldo final:", round(sueldo_final, 2))
print("Porcentaje de aumento:", round(porcentaje, 2), "%")
