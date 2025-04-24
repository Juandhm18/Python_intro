# Pide la edad y el género del usuario ("M" para mujer, "H" para hombre).

#     Mujer se jubila a los 60 años
#     Hombre se jubila a los 65 años

# Si ya se puede jubilar, muestra un mensaje celebratorio.
# Si no, indica cuántos años faltan para la jubilación.

edad = int(input("Cual es tu edad?: "))
genero = input("Cual es tu genero?\nSi eres hombre dijita H, si eres mujer usa M: ")
genero.upper()

while genero == 'H' or genero == 'M':
    if genero == 'H':
        if edad >= 65:
            print("Ya te puede jubilar\nFELICIDADES!")
        else:
            print("lo siento para jubilarte aun te faltan ",(65-edad)," años")
        break
    elif genero== 'M':
        if edad >= 60:
            print("Ya te puede jubilar\nFELICIDADES!")
        else:
            print("lo siento para jubilarte aun te faltan ",(60-edad)," años")
        break
else:
    print("ERROR!!!\nEl dato ingresado no concuerda")