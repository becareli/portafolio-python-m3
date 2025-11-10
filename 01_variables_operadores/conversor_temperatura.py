def conversor_temperatura(temp_c):
    temp_f = temp_c * 9/5 + 32
    temp_k = temp_c + 273.15
    return temp_f, temp_k

celsius = float(input("Ingrese temperatura en Celsius: "))
fahrenheit, kelvin = conversor_temperatura(celsius)
print(f"{celsius}°C equivale a {fahrenheit}°F y {kelvin} K")
