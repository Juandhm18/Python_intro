# Pide:
#     Sueldo bruto
#     Porcentaje de descuento (por ejemplo: 13)
# Calcula el sueldo neto usando la fórmula:
#     sueldo_neto = sueldo_bruto - (sueldo_bruto * descuento / 100)
# Ejemplo de salida:
#     Sueldo bruto: 1000 Descuento: 13 Sueldo neto: 870.0

sueldo_bruto = float(input("\nDe cuanto es el monto de tu salario bruto?: "))
descuento = int(input("Cual es el porcentaje de descuento que se te retira: "))

sueldo_neto = sueldo_bruto - (sueldo_bruto * descuento / 100)

print("Tu sueldo bruto es de: ",sueldo_bruto," se te descuenta: ",descuento," y tu sueldo neto es de: ",sueldo_neto)