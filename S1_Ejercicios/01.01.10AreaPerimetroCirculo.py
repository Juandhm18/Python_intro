#Pide el radio de un círculo y muestra el área y el perímetro (circunferencia).
pi = 3.1416
radio = float(input("Ingresa el radio del circulo: "))

area = pi*(radio*radio)
perimetro = 2*pi*radio

print(f"El area del circulo es de {area:.2f}")
print(f"El perimetro del circulo es de {perimetro:.2f}")