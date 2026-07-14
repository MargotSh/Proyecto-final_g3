def main():
    altura = 3.5
    largo = 4.0
    ancho = 5.5
    costo_x_metro_cubico = 3.2

    volumen = altura * largo * ancho
    a_pagar = volumen * costo_x_metro_cubico

    print("El resultado es:", round(a_pagar, 2))

main()