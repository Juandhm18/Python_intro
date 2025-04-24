#Pide una temperatura en Fahrenheit y muestra el equivalente en Celsius.

TempF = float(input ("Digite la temperatura en grados Fahrenheit a convertir:"))
TempC = float((TempF - 32) * 5/9)
print("Su equivalente en Celsius es: ", TempC)