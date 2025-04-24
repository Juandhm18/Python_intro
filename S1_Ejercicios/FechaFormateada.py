#Pide al usuario el día, mes y año por separado e imprime la fecha en formato: "DD/MM/AAAA" y también "AAAA-MM-DD"

Dia = input("Digite el dia: ")
mes = input("Digite el mes: ")
año = input("Digite el año: ")

print(f"La fecha en formato DD/MM/AAAA es: {Dia}/{mes}/{año}")
print(f"La fecha en formato AAAA-MM-DD es: {año}-{mes}-{Dia}")