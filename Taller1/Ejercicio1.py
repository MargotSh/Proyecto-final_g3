def main():
    a = 90.5
    b = 40.1
    c = 59.6

    area1 = (a - c) * b / 2
    area2 = b * c
    area_total = area1 + area2

    print("El resultado es:", round(area_total, 2))

main()