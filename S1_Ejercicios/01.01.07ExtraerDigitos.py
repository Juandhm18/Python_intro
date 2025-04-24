#Pide un número de 4 cifras e imprime cada dígito por separado, separados por coma.
#📌 Ejemplo: Entrada → 1234 → Salida → 1, 2, 3, 4

numero = input("Ingrese un numero de 4 digitos: ")
while len(numero)>4 or len(numero)<4:
    if len(numero)>4:
        numero = input("No sea bruto ingrese un numero de 4 digitos: ")
    else:
        numero = input("Le falla el celebro? Que un numero de 4 digitos: ")
print(",".join(numero))