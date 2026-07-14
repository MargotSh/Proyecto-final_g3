a = 3000
b = 1500
c = 2000

# Estrategia: suma de todos - mínimo - máximo = el del medio
minimo = min(a, b, c)
maximo = max(a, b, c)
medio = a + b + c - minimo - maximo

print("El sueldo intermedio es:", medio)





a = 3000
b = 1500
c = 2000

suma_total = a + b + c
mayor = (a + b + abs(a - b)) // 2
mayor = (mayor + c + abs(mayor - c)) // 2

menor = (a + b - abs(a - b)) // 2
menor = (menor + c - abs(menor - c)) // 2

medio = suma_total - mayor - menor

print("El sueldo intermedio es:", medio)