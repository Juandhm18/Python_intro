# Pide al usuario un número de segundos y muestra cuántas horas, minutos y segundos son.
#  Ejemplo: 3665 segundos → 1 hora, 1 minuto, 5 segundos.

tiempoSec = int (input("Introduce numero de segundos: "))
minutos = tiempoSec // 60
hora = tiempoSec // 3600
minutos = minutos%60
segundos = tiempoSec%60

print (tiempoSec, " segundos es igual a ->", hora, " hora, ", minutos, " minutos, ", segundos, " segundos.")