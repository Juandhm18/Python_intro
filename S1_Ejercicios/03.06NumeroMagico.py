# Pide un número al usuario.

#     Si es divisible por 3 y 5, imprime: "FizzBuzz"
#     Si solo por 3, imprime: "Fizz"
#     Si solo por 5, imprime: "Buzz"
#     Si no es divisible por ninguno, imprime: "Nada mágico"

Num = int (input("Ingresa un numero: "))
if Num % 3 == 0 and Num % 5 == 0:
    print("FizzBuzz")
elif (Num % 3 == 0):
    print("Fizz")
elif (Num % 5 == 0):
    print("Buzz")
else:
    print("Nada mágico")