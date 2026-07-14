def calcular_nota_final(pc01, pc02, ep, ef):
    # Fórmula: Promedio Final = PC01 * 0.2 + PC02 * 0.2 + EP * 0.2 + EF * 0.4
    promedio_final = pc01 * 0.2 + pc02 * 0.2 + ep * 0.2 + ef * 0.4
    print(f"La nota final es: {promedio_final:.2f}")

pc01 = float(input("Ingrese la nota de PC01: "))
pc02 = float(input("Ingrese la nota de PC02: "))
ep = float(input("Ingrese la nota de EP: "))
ef = float(input("Ingrese la nota de EF: "))
calcular_nota_final(pc01, pc02, ep, ef)