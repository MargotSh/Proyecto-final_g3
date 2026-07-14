#Caso CONCURSO DE CANTO

#datos de entrada
participantes = ["Valeria", "Sebastián", "Daniela", "Hugo", "Fernanda"]
puntajes = [86, 92, 78, 88, 95]

# a. Función para obtener el promedio de puntajes

def promedio_puntajes(puntajes):
    suma = 0
    for i in range(len(puntajes)):
        suma = suma + puntajes[i]
    return suma / len(puntajes)

# b. Función para obtener el mayor puntaje y el participante que lo obtuvo

def mayor_puntaje(participantes, puntajes):
    mayor = puntajes[0]
    nombre = participantes[0]

    for i in range(len(puntajes)):
        if puntajes[i] > mayor:
            mayor = puntajes[i]
            nombre = participantes[i]

    return nombre, mayor

#c. Función para obtener la cantidad de participantes con puntajes superiores al promedio
    
def superiores_promedio(puntajes):
    prom = promedio_puntajes(puntajes)
    contador = 0

    for i in range(len(puntajes)):
        if puntajes[i] > prom:
            contador = contador + 1

    return contador
    
promedio = promedio_puntajes(puntajes)
print("a. Promedio de puntajes:", promedio)

participante, mayor = mayor_puntaje(participantes, puntajes)
print("b. Mayor puntaje:", mayor)
print("   Participante:", participante)

cantidad = superiores_promedio(puntajes)
print("c. Participantes con puntaje superior al promedio:", cantidad)