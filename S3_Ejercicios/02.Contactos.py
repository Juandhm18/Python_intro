contactos = [{"nombre":"Jesus","numero":3125468520},
             {"nombre":"Juan","numero":3264658945},
             {"nombre":"Santiago","numero":3654258963}
]
def agregar():
    nombre = input("Ingresa el nombre del nuevo contacto: ")
    numero = int(input(f"Ingresa el número de {nombre}: "))
    nuevo_contacto = {'nombre': nombre, 'numero': numero}
    contactos.append(nuevo_contacto)

def mostrar():
    for idx, i in enumerate(contactos):
        print(f"{idx}->",i['nombre'],"#",i['numero'])
        
def buscar():
    buscar = input("Ingrese el nombre del contacto: ")
    if buscar in contactos['nombre']:
            i = contactos.index(buscar)
            print(contactos[i]['nombre']['numero'])
    else:
        print("El nombre de ese contacto no existe")
        
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