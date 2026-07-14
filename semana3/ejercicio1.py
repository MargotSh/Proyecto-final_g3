def ejercicio1():
    #datos de entrada
    sueldoMensual = 5000
    utilidad = 6000
    
    #proceso
    sueldoAnual = sueldoMensual * 14 + utilidad
    sueldoNeto = sueldoAnual - 7 * 3600
    
    if sueldoNeto > 0:
        impuesto = 0.21 * sueldoNeto
    else:
        impuesto = 0
        
    #salida
    print("el impuesto a cobrar es", impuesto)
    
ejercicio1()