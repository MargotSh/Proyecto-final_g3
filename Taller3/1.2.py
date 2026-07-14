def par_o_impar(numero):
    if numero % 2 == 0:
        print(f"{numero} es par")
    else:
        print(f"{numero} es impar")

# Programa principal
numero = int(input("Ingrese un número: "))
par_o_impar(numero)
