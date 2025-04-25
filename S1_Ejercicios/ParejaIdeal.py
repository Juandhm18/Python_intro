puntaje = 0
print("\n       <-------CUPIDO------->\n")
print("Veamos si eres una persona compatible")
print("Puedes usar las siguientes opciones de respuesta")
print("Si   -   No    -     Tal vez\n")

preguntas = [
    str(input("Consideras que eres una persona aseada? ")),
    str(input("Tienes una proyeccion sobre tu futuro en la que podria encajar una pareja? ")),
    str(input("Te ves en una relacion estable? ")),
    str(input("Te gusta el anime? ")),
    str(input("Te gustan los deportes? ")),
    str(input("Te gustaria conocer lugares nuevos con tu pareja? ")),
    str(input("Consideras que incluir a tu pareja con tu circulo social es importante? ")),
    str(input("Consideras que los detalles van mas de solo gastar dinero? ")),
    str(input("Consideras importante que en ciertas ocasiones tu pareja sea tu confidente? ")),
    str(input("Consideras que el amor cursi es bonito? "))
]

for i in range(9):
    while type(preguntas[i])==str:
        if preguntas[i].lower() == 'si':
            puntaje += 10
        elif preguntas[i].lower() == 'tal vez':
            if preguntas[2].lower() == 'tal vez':
                preguntas[i] = str(input("Eres honesta con lo que sientes cuando lo sientes? "))
                if preguntas[i].lower() == 'si':
                    puntaje += 10
                elif preguntas[i].lower == 'tal vez': 
                    puntaje += 5
                elif preguntas[i].lower == 'no':
                    puntaje -= 10
            else:
                puntaje += 5   
        elif preguntas[i].lower() == 'no':
            puntaje -= 10
        else:
            print("Lo siento la respuesta es invalida")
        break
if puntaje >= 80:
    print("\nEres ideal")
elif puntaje > 50 and puntaje < 80:
    print("\nQuiza pueda funcionar")
else:
    print("\nLo siento, no eres tu, soy yo")