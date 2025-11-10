def area_cuadrado(lado):
    return lado * lado

def area_circulo(radio):
    import math
    return math.pi * radio ** 2

print("Área cuadrado:", area_cuadrado(5))
print("Área círculo:", area_circulo(3))
