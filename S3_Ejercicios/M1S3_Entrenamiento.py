productos = {"papa":{"precio":2500,"cantidad":50},
             "zanahoria":{"precio":500,"cantidad":10}}

def agregar(articulo, precio, cantidad):
    productos[articulo] = {"precio": precio, "cantidad":cantidad}
    
def buscar(consul):
        if consul in productos:
            print(f"\n{consul}: ${productos[consul]['precio']} | cantidad {productos[consul]['cantidad']}")
        else:
            print("Este articulo no existe")

def editar(consul, precio):
    if consul in productos:
        productos[consul]["precio"] = precio
        print(f"precio actualizado para {consul}: {productos[consul]['precio']}")
    else:
        print("El producto no existe.")

def eliminar(consul):
    if consul in productos:
        del productos[consul]
    else:
        print("El producto no existe, por lo cual no se puede eliminar")
        
def total():
    totalInventario = sum(map(lambda x: x['precio']*x['cantidad'], productos.values()))
    print(totalInventario)
        
while True:
        print("\n     -----DIRECTORIO-----\n")
        print("1. Agregar un nuevo producto")
        print("2. Consultar productos")
        print("3. Actualizar precios")
        print("4. Eliminar productos")
        print("5. Total productos")
        print("6. Cerrar\n")
        opcion = input("Ingresa la opcion: ")
        match opcion:
            case "1":
                articulo = input("Ingrese el nombre del articulo: ")
                precio = float(input("Ingrese el valor PU de el articulo: "))
                cantidad = int(input("Cantidad disponible "))
                agregar(articulo, precio, cantidad)
            case "2":
                consul = input("Ingrese el nombre del producto: ").strip().lower()
                buscar(consul)
            case "3":
                consul = input("Ingrese el articulo a editar: ")
                precio = float(input("Ingrese el nuevo precio: "))
                editar(consul, precio)
            case "4":
                consul = input("Ingrese el articulo a eliminar: ")
                eliminar(consul)
            case "5":
                total()
            case "6":
                print("Saliendo...")
                break
            case _:
                print("Esta opcion no existe, intentalo de nuevo\n")            
