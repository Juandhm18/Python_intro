# Pide al usuario 3 notas (entre 0 y 10).
#     Si alguna nota está fuera del rango, muestra un mensaje de error.
#     Si todas son válidas, calcula el promedio y muestra si el estudiante aprueba (≥ 6) o reprueba.
prom = 0
NotasExam = []*3
print("\nSISTEMA QUE CALCULA PROMEDIOS\n")
for i in range(3):
    nota = float(input("Ingrese la nota del examen: "))
    while nota < 0 or nota > 10:
        print("ERROR La nota esta fuera del rango de calificacion")
        nota = float(input("Ingrese la nota nuevamente: "))
    NotasExam.append(nota)

for i in range(3):
    prom += NotasExam[i]/3
    
if prom >= 6:
    print("\nEl estudiante APROBO!")
    print(f"Con un promedio de {prom:.2f}")
else:
    print("\nAL estudiante NO le dieron las tajadas!\n")
    print(f"Con un promedio de {prom:.2f} no paso")