estudiantes = {"juan":{"edad":22,"nota":2.5},"jose":{"edad":18,"nota":3.5}}

def agregar(nombre, edadUser, notaEstu):
    estudiantes[nombre] = {"edad": edadUser, "nota":notaEstu}

def editar(nombre, nueva_nota):
    if nombre in estudiantes:
        estudiantes[nombre]["nota"] = nueva_nota
        print(f"Nota actualizada para {nombre}: {estudiantes[nombre]['nota']}")
    else:
        print("El estudiante no existe.")

def eliminar(nombre):
    if nombre in estudiantes:
        del estudiantes[nombre]
    else:
        print("El estudiante no existe.")
        
def mostrar():
    for nombre, datos in estudiantes.items():
        print(f"{nombre}: Edad {datos['edad']} | Nota {datos['nota']}")
        
while True:
    try:
        print("\n     -----DIRECTORIO-----\n")
        print("1. Agregar un nuevo estudiante")
        print("2. Modificar calificacion estudiante")
        print("3. Mostrar informacion estudiantes")
        print("4. Eliminar un estudiante por su nombre.")
        print("5. Cerrar\n")
        opcion = int(input("Ingresa la opcion: "))
        match opcion:
            case 1:
                nombre = input("Ingresa el nombre del estudiante: ")
                edadUSer = int(input("Cuantos años tiene? "))
                notaEstu = float(input(f"Ingrese la nota de {nombre}: "))
                agregar(nombre, edadUSer, notaEstu)
            case 2:
                nombre = input("Ingresa el nombre del estudiante al que se le editara la calificacion: ")
                nueva_nota = float(input(f"Ingrese la nueva nota para {nombre}: "))
                editar(nombre, nueva_nota)
            case 3:
                mostrar()
            case 4:
                nombre = input("Ingresa el nombre del estudiante que deseas eliminar: ")
                eliminar(nombre)
            case 5:
                print("Saliendo...")
                break
            case _:
                print("Esta opcion no existe, intentalo de nuevo\n")            
    except ValueError:
        print("Debes ingresar un número válido.")