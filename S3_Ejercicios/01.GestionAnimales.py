nombre = []
edad = []
enfermo = []

def agregar():
    nombre.append(input("Ingrese el nombre de la mascota: "))
    edad.append(input("Cuantos años tiene? "))
    salud = input("Esta enfermo? Si/No ").upper()
    if salud == "SI":
        enfermo.append("Enfermo") 
    else:
        enfermo.append("Sano")
    
def eliminar():
    mascota = input("Ingrese el nombre de la mascota que deseas eliminar: ")
    if mascota in nombre:
            i = nombre.index(mascota)
            del nombre[i]
            del edad[i]
            del enfermo[i]
    else:
        print("El nombre de esa mascota no existe")
                
def mostrar():
    for i in range (len(nombre)):
        print(i,". Nombre:",nombre[i],"- edad:",edad[i]," - estado de salud:",enfermo[i])
    
while True:
    try:
        print("\n-----GESTION DE ANIMALES-----")
        print("         1. Agregar un animal nuevo")
        print("         2. Eliminar un animal por su nombre")
        print("         3. Mostrar lista de animales")
        print("         4. Finalizar")
        opcion = int(input("Que opcion deseas seleccionar?\n"))
        match opcion:
            case 1:
                agregar()
            case 2:
                eliminar()
            case 3:
                mostrar()
            case 4:
                print("Saliendo...")
                break
            case _:
                print("Esta opcion no existe, intentalo de nuevo\n")
    except ValueError:
        print("Debes ingresar un número válido.")            
