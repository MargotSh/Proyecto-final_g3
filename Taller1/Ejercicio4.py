import math

def main():
    horas = 3.5
    importex_hora = 4.2

    # Alternativa1
    """ 
    horas = horas + 0.49
    importe_a_cobrar = round(horas) * importex_hora
    """



    # Alternativa2
    importe_a_cobrar = math.ceil(horas) * importex_hora

    print("El importe a recibir es:", round(importe_a_cobrar, 2))

main()