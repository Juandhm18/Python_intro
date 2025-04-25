# Pide una cantidad en kilómetros y convierte:
#     A metros (km × 1000)
#     A centímetros (km × 100000)
#     A milímetros (km × 1_000_000)
# Muestra todo en una sola línea usando print() y concatenación.
# Ejemplo:
#     2 km = 2000 metros, 200000 cm, 2000000 mm

km = int(input("Ingresa la cantidad en km a convertir: "))
metros = km*1000
centim = km*100000
milim = km*1000000
print(km,"km =", metros,"metros,",centim,"cm,",milim,"mm")