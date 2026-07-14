def obtener_costo_residencial(m_cubico):
    costo = 0.0
    for i in range(1, m_cubico + 1):
        if i >= 1 and i <= 28:
            costo += 0
        elif i >= 29 and i <= 150:
            costo += 2.1
        else:
            costo += 1.5
    return costo


def obtener_costo_comercial(m_cubico):
    costo = 0.0
    for i in range(1, m_cubico + 1):
        if i >= 1 and i <= 400:
            costo += 1.8
        else:
            costo += 2.5
    return costo


def obtener_costo_segun_contrato(m_cubico, contrato):
    if contrato == "residencial":
        return obtener_costo_residencial(m_cubico)
    if contrato == "comercial":
        return obtener_costo_comercial(m_cubico)
    return 0.0


def main():
    # Datos de prueba
    m_cubico = 67
    contrato = "residencial"

    costo_residencial = obtener_costo_residencial(m_cubico)
    print("El costo residencial es:", round(costo_residencial, 2))

    costo_comercial = obtener_costo_comercial(m_cubico)
    print("El costo comercial es:", round(costo_comercial, 2))

    costo_segun_contrato = obtener_costo_segun_contrato(m_cubico, contrato)
    print("El costo según contrato es:", round(costo_segun_contrato, 2))


main()
