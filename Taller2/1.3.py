def celsius_a_fahrenheit(celsius):
    # Fórmula: F = C * 9/5 + 32
    fahrenheit = celsius * 9/5 + 32
    print(f"{celsius}°C equivalen a {fahrenheit}°F")

c = float(input("Ingrese la temperatura en Celsius: "))
celsius_a_fahrenheit(c)
