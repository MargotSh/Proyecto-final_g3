def suma():
    print("\nse va a realizar la SUMA")

def resta():
    print("\nse va a realizar la RESTA")

def division():
    print("\nse va a realizar la DEVISION")

def validarContrasena():
    contrasena = input("\nIngrese una contraseña de solo numeros: ")
    if contrasena.isdigit():
        print("Si es numero, realizar siguientres operaciones")
    else:
        print("No es numero, contraseña incorrecta")
        
def calcular_bonos():
    #calcular el bono total que ha ganado el trabajador en la empresa en todos sus años de trabajo
    
    anios_trabajando = int(input("Ingrear cuantos años viene trabajando: "))
    bonificacion = 0
    
    iterador = 1
    while iterador<=anios_trabajando :
        sueldo_inicial = float(input(f"Ingrear sueldo del año {iterador}: "))
        nivel_desempeno = int(input(f"Ingrese el nivel de desempeño del año {iterador}:"))
        
        bono_multiplicador = 0
        
        if nivel_desempeno == 0:
            bono_multiplicador == 0
        elif nivel_desempeno == 1:
            bono_multiplicador = 0.10
        elif nivel_desempeno == 2:
            bono_multiplicador = 0.25
        elif nivel_desempeno == 3:
            bono_multiplicador = 0.50
            
        #año 1 = 0
        #año 2 = 500
        #año 3 = 100
        #600
        
        bonificacion = bonificacion + (sueldo_inicial * bono_multiplicador)
        
        iterador += 1
        #iterador = iterador + 1
        
    print(f"En todos estos {anios_trabajando} años de trabajo, ha recibido S/.{bonificacion} de bonificacion")
    


def main():
    #while se ejecuta hasta que la expresion sea falsa
    #while infinito a proposito
    #1 = SI = True
    #0 = NO = False
    while True:
        print("\n\nEscoja una opcion")
        print("1. Realizar suma")
        print("2. Realizar resta")
        print("3. Realizar division")
        print("4. Realizar multiplicacion")
        print("5. Contraseña")
        print("6. Calcular Bono")
        print("7. SALIR")
        
        opcion_elegida = input()
        
        if opcion_elegida == "1":
            suma()
        elif opcion_elegida == "2":
            resta()
        elif opcion_elegida == "3":
            division()
        elif opcion_elegida == "4":
            print("\nse va a realizar la MULTIPLICACION")
        elif opcion_elegida == "5":
            validarContrasena()
        elif opcion_elegida == "6":
            calcular_bonos()
        elif opcion_elegida == "7":
            print("\nSALIENDO....")
            break
    
main()

