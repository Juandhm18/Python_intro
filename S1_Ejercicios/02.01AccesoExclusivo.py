#Pide la edad y el número de invitación. Muestra directamente si puede ingresar (edad > 21 y invitación == 777).
edad = int(input("Cuantos años tienes? "))
inv = int(input("Cual es el numero de invitacion? "))

if edad > 21 and inv == 777:
    print("\nFELICIDADES puedes ingresar\n")
else:
    print("\nLo siento no fuiste invitado")