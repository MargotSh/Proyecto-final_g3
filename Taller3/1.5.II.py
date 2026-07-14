def obtener_precio_producto(tipo_producto):
    tipo_producto = tipo_producto.upper()
    
    if tipo_producto == 'P':
        return 20.5
    elif tipo_producto == 'C':
        return 19.4
    elif tipo_producto == 'L':
        return 32.3
    elif tipo_producto == 'A':
        return 16.5
    elif tipo_producto == 'M':
        return 19.8
    else:
        return None

def calcular_monto_total(tipo_producto, cantidad_sacos):
    precio = obtener_precio_producto(tipo_producto)
    if precio is None:
        print("Tipo de producto inválido")
        return None
    total = precio * cantidad_sacos
    return total

# Programa principal
def main():
    tipo_producto = input("Ingrese el tipo de producto (P: Papa, C: Cebolla, L: Limón, A: Ají, M: Maíz): ")
    cantidad_sacos = int(input("Ingrese la cantidad de sacos: "))
    monto = calcular_monto_total(tipo_producto, cantidad_sacos)
    if monto is not None:
        print(f"El monto a pagar es: {monto:.2f} soles")

main()
