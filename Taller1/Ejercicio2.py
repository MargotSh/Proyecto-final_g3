def main():
    horas = 3.0
    pagox_hora = 40.5

    sueldo_bruto = horas * pagox_hora
    descuento = sueldo_bruto * 0.10
    sueldo_neto = sueldo_bruto - descuento

    print("El importe a recibir es:", round(sueldo_neto, 2))

main()
