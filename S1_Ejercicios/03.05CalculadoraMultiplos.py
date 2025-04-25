# Pide dos números y verifica si el primero es múltiplo del segundo usando %.
# Ejemplo:
#     12 es múltiplo de 4 → True 15 es múltiplo de 6 → False

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

if num1 % num2 == 0:
    print(num1, "Es multiplo de",num2,"-> True")
else:
    print(num1, "Es multiplo de",num2,"-> False")