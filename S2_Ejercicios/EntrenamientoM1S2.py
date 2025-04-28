#El programa que vas a desarrollar en este entrenamiento debe:
    #     Solicitar al usuario ingresar una calificación numérica (de 0 a 100)
    #     Evaluar si el estudiante ha aprobado o reprobado basándose en la calificación ingresada
    #     Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
    #     Calcular y mostrar el promedio de las calificaciones en la lista
    #     Preguntar al usuario por un valor específico
    #     Contar cuántas calificaciones en la lista son mayores que este valor
    # Verificar y contar calificaciones específicas:
    #     Permitir al usuario ingresar una lista de calificaciones (separadas por comas)
    #     Calcular y mostrar el promedio de las calificaciones en la lista

# Determinar el estado de aprobación:
nota = int(input("Ingresa una calificacion numerica valida entre 0 - 100\n"))
while True:
        if not nota:
            print("La calificacion no puede quedar vacia\nIngresa un numero de nuevo.")
            nota = input()
        else:    
            break
if nota >= 60:
    print("El estudiante Aprobo.\n")
else:
    print("El estudiante Reprobo.\n")

#Calcular el promedio:
print("\nVamos a calcular el promedio\n")
calificaciones = input("Ingrese las calificaciones separadas por (,)\n")
Lista_Calific = [float(Lista_Calific.strip()) for Lista_Calific in calificaciones.split(',')]
sum = 0
x = 0
may = 0
valor = float(input("Ingrese el valor especifico a comparar\n"))
for i in range(len(Lista_Calific)):
    sum += Lista_Calific[i]
    x += 1
    # Contar calificaciones mayores:
    if Lista_Calific[i] > valor:
        may += 1
prom = sum / x
print("El promedio de sus notas es de",prom)
print("En la lista hay",may,"notas mayores que",valor)



