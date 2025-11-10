num = int(input("Número para calcular factorial: "))
factorial = 1
contador = 1

while contador <= num:
    factorial *= contador
    contador += 1

print(f"El factorial de {num} es {factorial}")
