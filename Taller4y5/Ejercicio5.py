def obtener_descuento(importe, numero):
    descuento_local = 0.0
    contador = 0
    if importe > 800:
        while numero > 0:
            if numero % 10 == 1:
                contador += 1
            numero = numero // 10
        descuento_local = (importe * contador) / 100  # Eliminado 1.0, ya que Python maneja float automáticamente
        if contador % 2 == 0 and contador > 0:
            descuento_local += 50
    return descuento_local


def obtener_importe_final(importe, numero):
    descuento = obtener_descuento(importe, numero)
    return importe - descuento


def main():
    # Datos de prueba
    importe = 896.9  # monto consumido
    numero = 32121  # número del papel

    descuento = obtener_descuento(importe, numero)
    print("El descuento es:", round(descuento, 2))

    importe_final = obtener_importe_final(importe, numero)
    print("El importe final es:", round(importe_final, 2))


main()