# Pide al usuario 3 notas (entre 0 y 10).
#     Si alguna nota está fuera del rango, muestra un mensaje de error.
#     Si todas son válidas, calcula el promedio y muestra si el estudiante aprueba (≥ 6) o reprueba.

NotasExam = []*3
for i in range(3):
    nota = input("Ingrese la nota del examen: ")
    NotasExam.append(nota)
    print(NotasExam)
    