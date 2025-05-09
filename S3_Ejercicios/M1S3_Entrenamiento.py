# Lista de productos con información básica: nombre, precio y cantidad
productos = [{"producto":"papa","precio":25,"cantidad":50},
             {"producto":"zanahoria","precio":50,"cantidad":10}]
# Función que verifica si un artículo ya existe en la lista de productos
def articulo_existente():
    while True:
        articulo = input("Ingrese el nombre del articulo: ").lower()
        found = False
        for i in productos:
            #Si el articulo existe se retorna true al codigo
            if i["producto"] == articulo:
                found = True
                print("""El articulo ya existe por lo cual no se puede agregar de nuevo,
pero se puede editar su cantidad""")
                return found
        #SI el articulo no existe retorna el nombre del articulo ingresado
        if not found:
            return articulo 
# Función para agregar un nuevo producto al inventario
def agregar(articulo, precio, cantidad):
    productos.append({"producto":articulo,"precio":precio,"cantidad":cantidad})
#Solicita y valida que el precio sea un número flotante válido.
def solicitar_precio():
    while True:
            precio = input("Ingrese el valor unitario del artículo: ")
            if precio.isdigit(): # Verifica que el input sea numérico
                precio = float(precio)
                if precio <= 0:
                    print("El precio debe ser mayor que 0. Intente nuevamente.")
                else:
                    return precio
            else:
                print("Entrada inválida. Por favor, ingrese un número válido para el precio.")
# Función para solicitar un número entero válido
def solicitar_cantidad():
    #Solicita y valida que la cantidad sea un número entero válido.
    while True: 
        cantidad = input("Ingrese la cantidad disponible: ")
        if cantidad.isdigit():
            cantidad = int(cantidad)
            if cantidad < 0:
                print("La cantidad no puede ser negativa. Intente nuevamente.")
            else:
                return cantidad
        else:
            print("Entrada inválida. Por favor, ingrese un número válido para la cantidad.\n")
# Función para buscar un producto en el inventario
def buscar(consul):
    found = False
    for i in productos:
        if i["producto"] == consul:
            found = True
            print(f"El articulo fue encontrado y esta es su informacion \n{i["producto"]} | {i["precio"]} | {i["cantidad"]}")
    # Si el producto no está en la lista, se informa al usuario
    if not found:
        print(f"Este articulo no existe\n")
# Función para actualizar el precio de un producto existente
def editar(consul, precio):
    found = False    
    for i in productos:
        if i["producto"] == consul:
            found = True
            i["precio"] = precio
            print(f"El precio de este articulo fue editacon con exito\n")
    if not found:
        print(f"El articulo que estas tratando de editar no existe\n") 
# Función para eliminar un producto del inventario
def eliminar(consul):
    found = False
    for i in productos:
        if consul == i["producto"]:
            found = True
            productos.remove(i) # Se usa remove() para eliminar el diccionario correcto
            return
    if not found:
        print("El producto no existe, por lo cual no se puede eliminar")
# Función que muestra el inventario y calcula el valor total       
def total():
    if not productos: 
        print("El inventario está vacío.")
        return# Verifica si la lista está vacía
    for i in productos:
        print(f"{i["producto"]} | {i["precio"]} | {i["cantidad"]}")
    # Calcula el valor total del inventario multiplicando precio * cantidad
    totalInventario = sum(map(lambda x: x['precio']*x['cantidad'], productos))
    print(f"\n\033[32mTOTAL\033[0m:  {totalInventario:.2f}")
    
# Menú interactivo principal
while True:
        print("\n     -----\033[33mDIRECTORIO\033[0m-----\n")
        print("1. Agregar un nuevo producto")
        print("2. Consultar productos")
        print("3. Actualizar precios")
        print("4. Eliminar productos")
        print("5. Total productos")
        print("6. Cerrar\n")
        opcion = input("Ingresa la opcion: ")
        match opcion:
            case "1":
                articulo = articulo_existente()
                if articulo != True: # Si el artículo no existe, se agregará
                    cantidad = solicitar_cantidad()
                    precio = solicitar_precio()
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
                print("\033[35mSaliendo...\033[0m")
                break
            case _:
                print("Esta opcion no existe, intentalo de nuevo\n")            

    