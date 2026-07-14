def obtenerTotalComision(ventas):
    comision = obtenerTotalVentas(ventas) * 300
    return comision

def obtenerVendSupCuota(ventas,vendedores):
    miArreglo = [""] * len(ventas)
    for i in range(0, len(ventas),1):
        if ventas[i] > 5:
            miArreglo[i] = vendedores[i]
    return miArreglo

def obtenerPorcentaje(ventas):
    porc = 0
    numerador = 0
    denominador = len(ventas)
    
    for i in range(0, len(ventas),1):
        if ventas[i] > 5:
            numerador = numerador + 1
            
    porc = numerador / denominador
    return porc

def obtenerTotalVentas(ventas):
    suma = 0
    for i in range(0, len(ventas),1):
        suma = suma + ventas[i]
    return suma

def ejercicio1():
    #datos de entrada
    ventas = [15,16,1,0,4,15,13]
    vendedores = ["Hugo","Mariana","Luis","Jennifer","Jorge","Valeria","Manuel"]
    
    #Pregunta A
    totalVentas = obtenerTotalVentas(ventas)
    print("El total de ventas es",totalVentas)
    
    #Pregunta B
    porcentaje = obtenerPorcentaje(ventas)
    print("El porcentaje es",round(porcentaje,2))
    
    #Pregunta C
    vendSupCuota = obtenerVendSupCuota(ventas,vendedores)
    print("Los vendedores que superaron la cuota son",vendSupCuota)
    
    #Pregunta D
    totalComision = obtenerTotalComision(ventas)
    print("El total de comisión es",totalComision)
    
ejercicio1()