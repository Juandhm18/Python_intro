import random
print("     1. Usa un while para imprimir los números del 1 al 10.")
print("     2. Usa un while para imprimir los números del 10 al 1 en orden descendente.")
print("     3. Usa un while para sumar los números del 1 al 10 e imprimir el resultado.")
print("     4. Pide al usuario un número y usa un while para seguir pidiendo hasta que ingrese un número positivo.")
print("     5. Crea un menú con while que permita al usuario elegir entre opciones \n       ",
      "(por ejemplo, '1. Saludar', '2. Despedirse', '3. Salir') y solo termine cuando elija la opción de salir.")
print("     6. Genera un número secreto (puedes usar una variable fija)  \n       "
      "usa un while para pedirle al usuario que lo adivine. Da pistas si el número es mayor o menor.")
print("     7. Pide al usuario una palabra y usa un while para contar cuántas vocales tiene.")
print("     8. Pide al usuario una contraseña y usa un while para seguir pidiendo hasta que ingrese 'python123'")
print("     9. Pide números al usuario y súmalos hasta que ingrese '0', momento en el que se imprimirá el total.")
print("     10. Pide al usuario que ingrese un número entre 1 y 10. Si no lo hace, sigue pidiéndolo hasta que lo haga correctamente.")
opcion = int(input("Elige el ejercicio que deseas realizar 1-10\n"))
num = 0
match opcion:
    #1. Contar del 1 al 10:
    case 1:
        while True:
            num += 1
            if num <= 10:
                print(num)
            else:
                break
    #2. Contar hacia atrás:
    case 2:
        num = 11
        while True:
            num -= 1
            if num >= 1:
                print(num)
            else:
                break
    #3. Suma de los primeros 10 números:        
    case 3:
        sum = 0 
        while True:
            num += 1
            if num <= 10:
                sum += num
            else:
                break
        print("La suma de los numeros del 1 al 10 es:",sum)
    #4. Solicitar número positivo:
    case 4:
        num = int(input("Ingresa un numero positivo: "))
        while True:    
            if num <= 0:
                print("El numero no puede ser negativo o un cero")
                num = int(input("Ingresa un numero positivo: "))
            else:
                break
    #5. Menú interactivo:
    case 5: 
        while True:
            print("-----MENU INTERACTIVO-----")
            print("         1. Saludar")
            print("         2. Despedirse")
            print("         3. Salir")
            menu = int(input("Elige una opcion para ejecutar: "))
            match menu:
                case 1:
                    print("Bienvenido a este ambiente amigable")
                    break
                case 2:
                    print("Es un placer haberte conocido, vuelve pronto")
                    break
                case 3:
                    print("Saliendo...")
                    break
                case _:
                    print("La opcion no es valida")
    #6. Adivina el número:
    case 6:
        num = random.randint(1,20)
        opcion = int(input("Adivina un numero entre 1 y 20: "))
        while True:
            if opcion < num:
                opcion = int(input("El numero que elegiste es menor que el numero aleatorio, prueba de nuevo: "))
            elif opcion > num:
                opcion = int(input("El numero que elegiste es mayor que el numero aleatorio, prueba de nuevo: "))
            else:
                print("Adivinaste el numero secreto", num)
                break
    #7. Contar vocales en una palabra:
    case 7:
        vocales = ['a','e','i','o','u']
        palabra = input("Ingresa una palabra: ")
        cont = 0
        while True:
            for i in palabra:
                for j in vocales:
                    if i == j:
                        cont += 1
            break
        print(f"La palabra tiene {cont} vocales")
    #8. Validar contraseña:
    case 8:
        intentos = 5
        while True:
            contraseña = input("Ingrese la contraseña: ")
            contraseña = contraseña.lower()
            if contraseña == "python123":
                print("Has iniciado sesion.")
                break
            else:
                intentos -= 1
                print(f"Contraseña incorrecta, te quedan {intentos} intentos")
                if intentos == 0:
                    print("Has agotado los intentos. Sesion bloqueada")
                    break
    # Sumar hasta detenerse:
    case 9:
        print("Ingresa los numeros a sumar, recuerda podras parar una digites 0")
        sum = 0
        while True:
            num = int(input("Ingresa un numero: "))
            sum += num
            if num == 0:
                break
        print(f"La suma da {sum}")
    # Número de intentos:
    case 10:
        num = int(input("Ingresa un numero entre 1 y 10"))
        while True:
            if num < 1 or num > 10:
                print("El numero debe estar en el rango de 1 a 10")
                num = int(input("Ingresa otro numero: "))
            else:
                break
    case _:
        print("No jodas esta opcion no existe")

