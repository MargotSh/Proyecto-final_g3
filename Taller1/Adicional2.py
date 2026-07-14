def main():
    producto1 = 45.50
    producto2 = 32.25
    producto3 = 18.75

    subtotal = producto1 + producto2 + producto3
    igv = subtotal * 0.18
    total = subtotal + igv

    print("Total a pagar:", round(total, 2))

main()