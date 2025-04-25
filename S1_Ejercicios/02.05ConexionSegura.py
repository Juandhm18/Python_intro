#Pide protocolo (http o https) y puerto (80 o 443). 
#Muestra si la conexión es segura: protocolo es "https" y puerto es "443".

protocolo = input("\nIngresa el protocolo (HTTP o HTTPS)").lower()
puerto = int(input("Ingresa el puerto (80 o 443)"))

if protocolo == 'http' and puerto == 443:
    print("\nSu conexion es segura")
else:
    print("\nLo siento no estas en una conexion segura")