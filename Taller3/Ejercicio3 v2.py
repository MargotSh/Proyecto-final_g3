def indicar_si_son_multiplos(numero_A, numero_B):
    if numero_A % numero_B == 0 :
        return 1
    elif numero_A % numero_B == 1 :
        return 2
    elif numero_A % numero_B == 2 :
        return 3
    elif numero_A % numero_B == 3 :
        return 4
    #...
    elif numero_A % numero_B == 100 :
        return 1
    
    return 0
        
#1 = SI = V = True
#0 = NO = F = False

def main():
    numero_A = int(input("Ingresar numero A: "))
    numero_B = int(input("Ingresar numero B: "))
    
    resultado = indicar_si_son_multiplos(numero_A, numero_B)
    if resultado == 1 :
        print("Son multiplos")
    elif resultado == 0:
        print("No son multiplos")
    
    
main()
