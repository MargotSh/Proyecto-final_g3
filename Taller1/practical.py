def main():
    
    # datos de entrada
    preciox_rosa = 3.5
    cantidad = 20
    porcentaje_descuento = 10
    
    
    # a. Importe total sin descuento
    importe_total = preciox_rosa * cantidad
    
    # b. Importe final con descuento 
    monto_descuento = importe_total * (porcentaje_descuento / 100)
    importe_final = importe_total - monto_descuento
    
    
    # datos de salida
    print("Importe total sin descuento: S/", round(importe_total, 2))
    print("Importe final con descuento: S/", round(importe_final, 2))
    
main()