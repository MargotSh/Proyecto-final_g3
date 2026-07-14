def obtener_precio_app(tipo_producto, tipo_celular):
    tipo_producto = tipo_producto.upper()
    tipo_celular = tipo_celular.lower()
    
    if tipo_producto == 'O':
        if tipo_celular == 'i':
            return 50.60
        elif tipo_celular == 'a':
            return 20.30
    elif tipo_producto == 'J':
        if tipo_celular == 'i':
            return 90.80
        elif tipo_celular == 'a':
            return 40.50
    elif tipo_producto == 'U':
        if tipo_celular == 'i':
            return 60.80
        elif tipo_celular == 'a':
            return 30.20
    
    return None  # Si no se encuentra una combinación válida

def calcular_monto_total(tipo_producto, tipo_celular, cantidad):
    precio = obtener_precio_app(tipo_producto, tipo_celular)
    if precio is None:
        print("Datos inválidos: tipo de producto o tipo de celular incorrecto.")
        return None
    total = precio * cantidad
    return total

# Programa principal
def main():
    tipo_producto = input("Ingrese el tipo de producto (O: Oficina, J: Juegos, U: Utilitarios): ")
    tipo_celular = input("Ingrese el tipo de celular (i: iPhone, a: Android): ")
    cantidad = int(input("Ingrese la cantidad de aplicaciones: "))
    
    monto = calcular_monto_total(tipo_producto, tipo_celular, cantidad)
    if monto is not None:
        print(f"El monto total a pagar es: {monto:.2f} soles")

main()
