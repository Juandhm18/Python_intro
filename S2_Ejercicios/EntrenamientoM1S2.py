#El programa que vas a desarrollar en este entrenamiento debe:
    #     Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
    #     Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación ingresada
    #     Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
    #     Calcular y mostrar el promedio de las calificaciones en la lista
    #     Preguntar al usuario por un valor específico
    #     Contar cuántas calificaciones en la lista son mayores que este valor
    #   Verificar y contar calificaciones específicas:
    #         Preguntar al usuario por una calificación específica. 
    #       Verificar si esta calificación está en la lista y contar cuántas veces aparece, utilizando break y continue para controlar el flujo del programa.

# Determinar el estado de aprobación:
nota = int(input("Ingresa una calificacion numerica valida entre 0 - 100\n"))
while True:
        if not nota:
            print("La calificacion no puede quedar vacia\nIngresa un numero de nuevo.")
            nota = input()
        elif nota < 0 or nota > 100:
            print("La calificacion debe estar dentro del rango de 0 a 100")
            nota = input()
        else:    
            break
if nota >= 60:
    print("El estudiante Aprobo.\n")
elif nota > 50 and nota <60:
    print("Necesitas tomar un taller de recuperacion\n")
else:
    print("El estudiante Reprobo.\n")

#Calcular el promedio:
print("\nVamos a calcular el promedio\n")
calificaciones = input("Ingrese las calificaciones separadas por (,)\n")
Lista_Calific = [float(Lista_Calific.strip()) for Lista_Calific in calificaciones.split(',')]
sum = 0
j = 0
x = 0
may = 0
cont = 0
valor = float(input("Ingrese el valor especifico a comparar\n"))
while True:
    notaEspec = float(input("Ingrese la nota: "))
    for i in range(len(Lista_Calific)):
        sum += Lista_Calific[i]
        x += 1
        # Contar calificaciones mayores:
        if Lista_Calific[i] > valor:
            may += 1
        if notaEspec == Lista_Calific[i]:
            j = 1
    if j == 1:
        for i in Lista_Calific:
            if notaEspec == i:
                cont += 1
    else:
        print("La nota no se encuentra repetida. ")
    prom = sum / x
    break
print("El promedio de sus notas es de",prom)
print("En la lista hay",may,"notas mayores que",valor)
print("En la lista hay",cont,"notas iguales a",notaEspec)



