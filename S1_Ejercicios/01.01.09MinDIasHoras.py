#Pide una cantidad de minutos y muestra a cuántos días, horas y minutos equivale.

min = int (input("Ccuantos minutos hay?: "))
hora = min // 60
dias = hora // 24
hora = hora%24
min = min%60

print (min, " minutos es igual a ->", dias, " dias, ", hora, " horas, ", min, " minutos.")

