#Pide dos notas. Muestra si el estudiante aprobó: ambas notas ≥ 6 y ninguna < 4.
print("\nVerifiquemos si aprobaste")
nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))

if nota1 >= 6 and nota2 >= 6:
    print("Has approbado!")
elif nota1 >= 6 or nota2 >= 6:
    print("Necesitas reforzar, debes hacer una examen adicional")
else:
    print("Has reprobado, mejor suerte la proxima")