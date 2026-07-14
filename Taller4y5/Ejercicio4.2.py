#Una reconocida empresa de venta de gas natural desea una aplicación que permita
#calcular el total a pagar por una persona u empresa dependiendo de los metros cúbicos (m3) consumidos y su tipo de contrato.

#Existen dos tipos de contrato:
#El contrato "residencial" (r) permite que los 28 primeros m3 sean gratis,
#los siguientes 122 se paguen a tarifa de 2.1 soles y a partir del m3 123 en adelante se paguen a 1.5 soles.

#Por otro lado, el contrato "comercial" (c) permite que los 400 primeros m3 se paguen a 1.8 soles y a partir del 401 se pague a 2.5 soles.

#a.	Desarrollar un subprograma que permita a un usuario con contrato residencial calcular el total a pagar
#b.	Desarrollar un subprograma que permita a un usuario con contrato comercial calcular el total a pagar
#c.	Desarrollar un subprograma que, recibiendo la cantidad de m3 y el tipo de contrato pueda retornar el total a pagar.
def calcular_total_a_pagar(metros_cubicos, tipo_contrato):
  if(tipo_contrato == "r"):
    if(metros_cubicos <= 28):
      return 0 #aca devuelvo y se acaba todo
    elif(metros_cubicos <= 122):
      return (metros_cubicos - 28) * 2.1
    elif(metros_cubicos > 122):
      return (122 - 28) * 2.1 + (metros_cubicos - 122) * 1.5
  elif(tipo_contrato == "c"):
    if(metros_cubicos <= 400):
      return metros_cubicos * 1.8
    elif(metros_cubicos > 400):
      return 400 * 1.8 + (metros_cubicos - 400) * 2.5

tipo_contrato = input("Ingrese el tipo de contrato (r: residencial | c: comercial): ")
metros_cubicos = int(input("Ingrese la cantidad de metros cubicos consumidos: "))

total_a_pagar = calcular_total_a_pagar(metros_cubicos, tipo_contrato)
print(f"El total a pagar es: {total_a_pagar}")

