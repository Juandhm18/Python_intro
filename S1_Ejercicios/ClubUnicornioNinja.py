edad = int(input("Cuantos años tienes?:"))

if edad < 18:
    print("No puedes entrar esperamos poder conocerte pronto")
else:
    PaseDorado = input("Tienes pase dorado S/N?:")
    PaseDorado = PaseDorado.upper()
    if PaseDorado == 'S':
        print("Puedes ingresar, Bienvenido!")
    elif PaseDorado == 'N' and edad < 25:
        print("Puedes ingresar, Bienvenido!")
    else:
        print("No puedes entrar te deseamos buena suerte!")