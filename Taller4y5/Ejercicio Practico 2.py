jugadores = ["Messi", "Dembélé", "Oyarzabal", "Vinícius"]
goles = [7, 4, 4, 4]

##EDAD PROMEDIO
def calcular_edad_promedio():
  suma_edades = 0
  contador = 0
  for edad in goles:
    suma_edades = suma_edades + edad
    contador = contador + 1
  promedio_edad = suma_edades / contador

  print(f"El promedio de goles es {promedio_edad}")

  return promedio_edad

##CUAL ES LA EDAD MAYOR Y QUIEN LA TIENE
def edad_mayor_y_quien_la_tiene():
  mayor_edad = 0
  contador = 0
  indice_mayor_edad = 0
  for edad in goles:
    if edad > mayor_edad:
      mayor_edad = edad
      indice_mayor_edad = contador
    contador = contador + 1

  print(f"La mayor cantidad de goles es {mayor_edad} y lo tiene {jugadores[indice_mayor_edad]}")

def mostrar_edades_mayor_al_promedio(edad_promedio):
  print("Los goles mayores al promedio son:")
  for edad in goles:
    if edad > edad_promedio:
      print(edad)

def main():
  edad_promedio = calcular_edad_promedio()
  edad_mayor_y_quien_la_tiene()
  mostrar_edades_mayor_al_promedio(edad_promedio)

main()

