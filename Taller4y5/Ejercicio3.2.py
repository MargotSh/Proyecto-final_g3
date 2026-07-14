#Un banco establece que la clave secreta para acceso a sus cajeros automáticos
#debe ser un número de cuatro o más dígitos
#y que la suma de los dos dígitos que se encuentran en la 3 y 4 posición (posición de centena y millar) sea par.
#Determinar si una clave cumple con la condición
def validar_es_4_digitos_version_1(clave):
    if len(clave) != 4:
        print("V1. La clave NO es de 4 digitos")
    else:
        print("V1. La clave SI es de 4 digitos")
        
def validar_es_4_digitos_version_2(clave):
    contador_de_caracteres = 0
    
    for letra in clave:
        contador_de_caracteres += 1

    
    if contador_de_caracteres != 4:
        print("V2. La clave NO es de 4 digitos")
    else:
        contador_auxiliar = 0
        numero_posicion_3 = 0
        numero_posicion_4 = 0
        
        for letra in clave:
            if contador_auxiliar == 0:
                numero_posicion_4 = letra
            elif contador_auxiliar == 1:
                numero_posicion_3 = letra
            contador_auxiliar += 1
            
        suma = int(numero_posicion_4) + int(numero_posicion_3)
        print(f"La suma de {numero_posicion_4} y {numero_posicion_3} es: {suma}")
        
        if suma % 2 == 0:
            print("CLAVE VALIDA")
        else:
            print("CLAVE INVALIDA")
            

clave_ingresada = input("Ingrese la clave para el ATM:")

#validar_es_4_digitos_version_1(clave_ingresada)
validar_es_4_digitos_version_2(clave_ingresada)

