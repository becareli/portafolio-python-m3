nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
altura = float(input("Ingresa tu altura en metros: "))
es_arquitecto = input("¿Eres arquitecto? (sí/no): ").lower() == "sí"

print(f"Nombre: {nombre}, Edad: {edad}, Altura: {altura}m, Arquitecto: {es_arquitecto}")
