
# Pide dos valores al usuario e imprime los valores intercambiados.
# Ejemplo: Entrada → a = 3, b = 5 → Salida → a = 5, b = 3

a = input("Ingresa el primer valor a guardar: ")
b = input("Ingresa el segundo valor a guardar: ")

print("La entrada fue -> a =",a, ", b =",b)
a, b = b, a
print ("la salida es -> a = ",a, ", b = ",b)