#Pide edad, país y número de documento. 
#Muestra si cumple condiciones: edad entre 18 y 30 inclusive, país distinto de "Antártida" y documento diferente de 0.

edad = int(input("Cuantos años tienes? "))
pais = input("De que pais eres? ").lower()
documento = input("Cual es el numero de tu documento? ")

if edad > 18 and edad < 30 and pais != 'antartida' and documento != 0:
    print("Cumples con las condiciones!")
else:
    print("Lo siento en esta ocasion no cumples con las condiciones")