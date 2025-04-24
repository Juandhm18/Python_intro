#Pedimos datos del producto
tieneNumeros = True
while tieneNumeros == True:
    producto = input("Ingrese el nombre del producto: ")
    #Validar que el usuario si ingreso algun articulo
    while not producto:
        print("El nombre del producto no puede estar vacío.")
        producto = input("Ingrese el nombre del producto: ")
    else:
        tieneNumeros = any(character.isdigit() for character in producto)
        if tieneNumeros:
            print("El nombre del producto no puede contener números.")
else:
    #Una vez validado se piden precio y cantidad
    precio_unitario = float (input("Ingrese el precio por unidad: " ))
    Cantidad_prod = int (input("Ingresa la cantidad a comprar: "))
    #Se valida que los datos sean numeros positivos mayores a cero
    if precio_unitario <= 0 or Cantidad_prod <= 0:
        print("El precio y la cantidad deben ser números positivos o diferentes a cero.")
        print("Intentalo nuevamente")
    else:
        #Se pide el descuento a aplicar
        descuento = float(input("Ingrese el porcentaje de descuento: "))
        #Validar que el descuento este dentro del rango posible
        if  descuento < 0 or descuento > 100:
            print("El descuento debe estar entre 0 y 100%.")
        else:
            #Calcular el costo total teniendo en cuenta los datos ingresados
            costo_total = precio_unitario * Cantidad_prod 
            #Costo de la compra sin descuento
            print(f"El costo de la compra del {producto} sin descuento es de: {costo_total}")
            #Se aplica el descuento
            descuento_aplicado = costo_total * (descuento/100)
            #se valida el descuento para saber el mensaje que se mostrara en pantalla
            if descuento > 0:
                if descuento == 100:
                    print("Felicidades la compra del " + producto + " es gratis ")
                else:
                    costo_total = costo_total - descuento_aplicado
                    print(f"El costo total de la compra del {producto} es: {costo_total}")
            else:
                print("No se aplicó descuento, el costo total es el mismo.")
            print("Gracias por su compra!")
    