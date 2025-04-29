import datetime
respuesta = input("Desea ingresa la hora actual por su cuenta? (S/N) ")
if respuesta.upper() == 'N':
    hora_actual = datetime.time.now()
else:
    hora_actual = input("Ingrese la hora actual en formato (AAAA-MM-DD HH:MM:SS): ")
    formato_str = "%Y-%m-%d %H:%M:%S"
    hora_actual = datetime.datetime.strptime(hora_actual, formato_str)
print(hora_actual)
