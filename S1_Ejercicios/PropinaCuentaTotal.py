#Pide el costo de una comida y calcula el 10%, 15% y 20% de propina. Muestra el total a pagar en cada caso.

CostoTotal = int(input("Ingrese el costo de la comida: "))

Propina10 = int(CostoTotal*0.10)
Propina15 = int(CostoTotal*0.15)
Propina20 = int(CostoTotal*0.20)

Propina10 = CostoTotal + Propina10
Propina15 = CostoTotal + Propina15
Propina20 = CostoTotal + Propina20

print("El total a pagar con el 10% de propina es de: ", Propina10)
print("El total a pagar con el 15% de propina es de: ", Propina15)
print("El total a pagar con el 20% de propina es de: ", Propina20)

    
