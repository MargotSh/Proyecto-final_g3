#Se requiere un programa que calcule la cantidad de billetes de
#20 soles que se necesitan para entregar una cantidad de dinero
#en billetes de esa denominación

#Por ejemplo si envío 350 soles me dirá que se necesitan 17
#billetes (la parte decimal se ignora)

def main():
  #Datos de entrada
  cifra = int( input("Ingrese un numero: ") )

  #Secuencia de pasos
  numero_de_billetes_de_20 = cifra // 20

  #Datos de salida
  #print(numero_de_billetes_de_20)
  print("El numero de billetes de 20 es:")

main()
