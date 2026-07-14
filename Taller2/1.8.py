import math

def distancia_y_angulo(x1, y1, x2, y2):
    # Distancia: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
    dx = x2 - x1
    dy = y2 - y1
    distancia = math.sqrt(dx ** 2 + dy ** 2)
    
    # Ángulo con la horizontal en grados
    angulo = math.degrees(math.atan2(dy, dx))
    
    print(f"Distancia: {distancia}")
    print(f"Ángulo con la horizontal: {angulo}°")

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
distancia_y_angulo(x1, y1, x2, y2)