#Pide el monto total de la compra y la edad del cliente. Muestra si obtiene descuento (monto > 100 o edad > 60).

edad = int(input("Cuantos años tienes? "))
Monto = int(input("De cuanto es el monto? "))

if edad > 60 and Monto > 100:
    print("\nFELICIDADES tienes descuento\n")
else:
    print("\nLo siento no tienes descuento")