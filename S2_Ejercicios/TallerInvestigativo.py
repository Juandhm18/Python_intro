#1.Crea una lista llamada mi_lista con los números del 1 al 5.
mi_Lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#2.Crea una lista [10, 20, 30, 40] y muestra el primer y el último elemento.
lista = [10,20,30,40,50]
print(lista[0],"El ultimo elemento de la lista es",lista[-1])
#3. A partir de [10, 20, 30, 40, 50], obtén:
#     Los elementos del índice 1 al 3.
#     Los primeros 3 elementos.
#     Los elementos desde el índice 2 hasta el final.
print(lista[1:3])
print(lista[:3])
print(lista[2:])
#4. Cambia el tercer elemento de [10, 20, 30, 40] por 99.
lista[2] = 99
print(lista[::-1])
#5. A una lista [10, 20, 30] agrega:
#     El número 40 al final.
#     El número 15 en la posición 1.
#     Los números 50 y 60 al final de la lista.
lista = [10,20,30]
lista.append(40)
lista.insert(1,15)
lista.extend([50,60])
print(lista)
#6. De la lista [10, 20, 30, 40, 50], realiza las siguientes acciones:
#     Elimina el número 30.
#     Elimina el último elemento.
#     Elimina el segundo elemento (índice 1).
lista.remove(30)
print(lista)
lista.pop()
print(lista)
del lista[1]
print(lista)
#7. Con la lista [10, 20, 30, 40, 50]:
#     Verifica si el número 20 está en la lista.
#     Encuentra el índice del número 30.
#     Cuenta cuántas veces aparece el número 20.
lista = [10,20,30,40,50]
if 20 in lista:
    print("found")
print("el indice del numero 30 es:",lista.index(30))
print("El numero 20 aparece:",lista.count(20))
#8. Ordena la lista [40, 10, 30, 20]:
#     Primero en orden ascendente.
#     Luego en orden descendente.
#     Crea una nueva lista ordenada sin modificar la original.
lista = [40,10,30,20]
nueva_lista = sorted(lista)
print(nueva_lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
#9. Ejemplo práctico:
#     Invierte el orden de [10, 20, 30, 40] utilizando ambas técnicas.
lista = [10, 20, 30, 40]
print(lista[::-1])
lista.reverse()
print(lista)
#10. Copia la lista [10, 20, 30] de tres maneras diferentes.
lista = [10, 20, 30]
copia = lista[:]
mylist = list(lista)
newlist = lista.copy()
print(mylist)
print(newlist)
print(copia)
#11. Crea una lista vacía y escribe un código que imprima "La lista está vacía" si no contiene datos.
lista = []
if not lista:
    print("La lista esta vacia")
#12. Escribe un programa que:
#     Pregunte al usuario cuántos elementos quiere ingresar.
#     Luego pida esos elementos uno por uno.
#     Finalmente, muestre la lista completa.
listadatos = []
cant = int(input("Ingrese la cantidad de datos que desea ingresar: "))
for i in range(cant):
    dato = input(f"ingrese el dato en la posicion {i+1} ")
    listadatos.append(dato)
print(listadatos)