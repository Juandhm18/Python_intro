#Pide al usuario un precio (float) y muestra el resultado con dos decimales y símbolo de moneda (por ejemplo: $123.45).
precio = float(input("ingresa el precio del articulo: "))
print(f"${precio:.2f}")