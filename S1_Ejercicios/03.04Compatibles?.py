#Pide:
#     Nombre y edad de dos personas
# Verifica si:
#     Ambos tienen al menos 18 años
#     Se llaman distinto
#     La diferencia de edad no supera los 10 años
# Si cumplen todo, imprime un mensaje gracioso diciendo que son compatibles 💞
# Si no, di por qué no lo son.

usuario = str(input("Como te llamas? ")).lower()
usuario2 = str(input("Como se llama la segunda persona? ")).lower()

edad = int(input("Cuantos años tienes? "))
edad2 = int(input("Cuantos años tiene la segunda persona? "))

if edad > 18 and edad2 > 18 and usuario != usuario2 and (edad - edad2) <= 10:
    print("Uy tortolos, son una pareja compatible")
elif edad < 18 or edad2 < 18:
    print("Todo bien en casa? Uno de los dos es menor de edad")
elif usuario == usuario2:
    print("De verdad es alguien que se llama como vos, no son compatibles")
else:
    print("Pero si uno de los dos le lleva mas de 10 años al otro")