# Pide un número de tres cifras (ej. 123) y muestra sus cifras en orden inverso (321). 
# Usa operaciones matemáticas para extraer centenas, decenas y unidades.

num = int(input("Digite un numero de 3 cifras: "))
if num >99 and num <= 999:  
    centenas = num//100
    decenas = (num%100)//10
    unidades = num%10
    print (f"El numero invertido es: {unidades}{decenas}{centenas}")
else:
    print("El numero tiene mas de 3 dijitos.")
#print ("El numero invertido es: ", int(str(num)[::-1]))

