def determinarCosto(examenEscrito,examenOral):
    costo = 0
    nivel = determinarNivel(examenEscrito,examenOral)
    if nivel == 3:
        costo = 400
    elif nivel == 2:
        costo = 250
    elif nivel == 1:
        costo = 150
    return costo

def determinarNivel(examenEscrito,examenOral):
    n = 0
    if examenEscrito > 95 and examenOral > 75:
        n = 3
    elif examenEscrito > 95 and examenOral <= 75:
        n = 2
    elif examenEscrito <= 95:
        n = 1
    return n

def ejercicio2():
    #datos de entrada
    examenEscrito = 98
    examenOral = 74
    
    #Preguna A
    nivel = determinarNivel(examenEscrito,examenOral)
    print("El nivel es",nivel)
    
    #Pregunta B
    costo = determinarCosto(examenEscrito,examenOral)
    print("El costo es",costo)
ejercicio2()