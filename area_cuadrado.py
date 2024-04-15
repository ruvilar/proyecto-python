# RETO PYTHON 1

def calculate_square(side_1, side_2):
    side_1 = float(input("Introduce la longitud para el lado del cuadrado en cm"))
    area = side_1 * side_1
    print("El área de %i de un cuadrado es de %.2f centímetros"%(side_1, area))

    side_2 = float(input("Introduce la longitud para el perímetro del cuadrado en cm"))
    perimeter = side_2 * 4
    print("El perímetro de %i de un cuadrado es de %.2f centímetros"%(side_2, perimeter))

calculate_square(1, 1)
