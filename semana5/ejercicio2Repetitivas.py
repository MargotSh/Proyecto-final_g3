def calcularPorcentaje(anho,sueldo,tipoTrabajador):
    sueldoFinal = calcularSueldoFinal(anho,sueldo,tipoTrabajador)
    porc = (sueldoFinal / sueldo - 1) * 100
    
    return porc
    

def calcularSueldoFinal(anho,sueldo,tipoTrabajador):
    sueldoNuevo = sueldo
    
    if tipoTrabajador == "G":
        for i in range(1, anho+1,1):
            if i % 4 == 0:
                sueldoNuevo = sueldoNuevo + sueldoNuevo * 0.18 #años 4,8,12,16.....
            else:
                sueldoNuevo = sueldoNuevo + sueldoNuevo * 0.14 #años 1,2,3,5,6,7,9.....
    else:
        for i in range(1, anho+1,1):
            if i % 4 == 0:
                sueldoNuevo = sueldoNuevo + sueldoNuevo * 0.12 #años 4,8,12,16.....
            else:
                sueldoNuevo = sueldoNuevo + sueldoNuevo * 0.08 #años 1,2,3,5,6,7,9.....    
    
    return sueldoNuevo

def ejercicio2():
    #datos de entrada
    anho = 5
    sueldo = 6000
    tipoTrabajador = "G"
    
    #Pregunta A
    sueldoFinal = calcularSueldoFinal(anho,sueldo,tipoTrabajador)
    print("El sueldo final es",round(sueldoFinal,2), "soles")
    
    #Pregunta B
    porcentaje = calcularPorcentaje(anho,sueldo,tipoTrabajador)
    print("El porcentaje de aumento es",round(porcentaje,2))
    
ejercicio2()