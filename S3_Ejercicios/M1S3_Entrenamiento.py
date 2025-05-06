productos = {"papa":{"precio":2500,"cantidad":50}}

def agregar(articulo, precio, cantidad):
    productos[articulo] = {"precio": precio, "cantidad":cantidad}

# def editar(nombre, nueva_nota):
#     if nombre in estudiantes:
#         estudiantes[nombre]["nota"] = nueva_nota
#         print(f"Nota actualizada para {nombre}: {estudiantes[nombre]['nota']}")
#     else:
#         print("El estudiante no existe.")

# def eliminar(nombre):
#     if nombre in estudiantes:
#         del estudiantes[nombre]
#     else:
#         print("El estudiante no existe.")
        
# def mostrar():
#     for nombre, datos in estudiantes.items():
#         print(f"{nombre}: Edad {datos['edad']} | Nota {datos['nota']}")
        
while True:
    try:
        print("\n     -----DIRECTORIO-----\n")
        print("1. Agregar un nuevo producto")
        print("2. Consultar productos")
        print("3. Actualizar precios")
        print("4. Eliminar productos")
        print("5. Total productos")
        print("6. Cerrar\n")
        opcion = int(input("Ingresa la opcion: "))
        match opcion:
            case 1:
                articulo = input("Ingrese el nombre del articulo: ")
                precio = float(input("Ingrese el valor PU de el articulo: "))
                cantidad = int(input("Cuantos lleva? "))
                agregar(articulo, precio, cantidad)
            case 2:
                
                editar(nombre, nueva_nota)
            case 3:
                mostrar()
            case 4:
                eliminar(nombre)
            case 5:
                total()
            case 6:
                print("Saliendo...")
                break
            case _:
                print("Esta opcion no existe, intentalo de nuevo\n")            
    except ValueError:
        print("Debes ingresar un número válido.")