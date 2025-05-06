contactos = {
    "jesus": 3125468520,
    "juan": 3264658945,
    "santiago": 3654258963
}
def agregar():
    nombre = input("Ingresa el nombre del nuevo contacto: ")
    while True:
        numero = input(f"Ingresa el número de {nombre}: ").strip()
        if numero.isdigit():
            contactos[nombre] = numero
            print("Contacto agregado exitosamente.")
            break
        else:
            print("Número inválido. Inténtalo de nuevo.")
            
def mostrar():
    print("\nLista de contactos:")
    for idx, (nombre, numero) in enumerate(contactos.items(), 1):
        print(f"{idx}-> {nombre.capitalize()} #{numero}")
        
def buscar():
    buscar = input("Ingrese el nombre del contacto: ").strip().lower()
    if buscar in contactos:
        print(f"Número de {buscar.capitalize()}: {contactos[buscar]}")
    else:
        print("El nombre de ese contacto no existe.")
            
       
while True:
    try:
        print("\n     -----DIRECTORIO-----\n")
        print("1. Agregar un nuevo contacto")
        print("2. Mostrar todos los contactos")
        print("3. Buscar contacto")
        print("4. Cerrar\n")
        opcion = int(input("Ingresa la opcion: "))
        match opcion:
            case 1:
                agregar()
            case 2:
                mostrar()
            case 3:
                buscar()
            case 4:
                print("Saliendo...")
                break
            case _:
                print("Esta opcion no existe, intentalo de nuevo\n")            
    except ValueError:
        print("Debes ingresar un número válido.")    