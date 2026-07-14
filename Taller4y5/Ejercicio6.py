def medicina_en_el_cuerpo(medicina, dias):
    cont_dias = 0
    medicina_res = medicina

    while cont_dias < dias:
        medicina_res = medicina_res - (medicina_res * 0.20)
        cont_dias = cont_dias + 1

    return medicina_res


def dias_en_eliminar_medicina(medicina, porcentaje):
    medicina_a_eliminar = medicina * porcentaje / 100
    suma_medicina_a_eliminar = 0.0
    cont_dias = 0

    while suma_medicina_a_eliminar < medicina_a_eliminar:
        a_eliminar = medicina * 0.20
        medicina = medicina - a_eliminar
        suma_medicina_a_eliminar = suma_medicina_a_eliminar + a_eliminar
        cont_dias = cont_dias + 1

    return cont_dias


def main():
    # Datos de prueba
    medicina = 100.0
    dias = 5
    porcentaje = 20.5

    # Probar método medicina_en_el_cuerpo
    medicina_rest = medicina_en_el_cuerpo(medicina, dias)
    print("Después de", dias, "días se eliminará", round(medicina_rest, 2), "de medicina")

    # Probar método dias_en_eliminar_medicina
    dias_elim = dias_en_eliminar_medicina(medicina, porcentaje)
    print("Tardará", dias_elim, "días en eliminar la medicina")

main()
