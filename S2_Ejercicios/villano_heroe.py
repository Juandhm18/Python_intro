#ecenrio 1 el heroe esta solo y escoge la mejor opcion para ganar\n
# ten en cuenta que puede haber civiles y estan en riesgo 
vulnerable = 100
vidaVil = 100
print("---Ciudad Gotica---\n---Abril 18/1999---")
print("--Manicomio Arkham-\n")
print("Parece que Bane esta atacando Arkham...")

villano = input("con tu nivel atual crees que Bane es fuerte o debil:\n")
civiles = input("¿hay civiles cerca?:\n")

if civiles == "si":
    repuesta = input("¿hay civiles en peligro?:\n")
    if repuesta == "si":
        print("Veo que hay personas en peligro, debes tomar una decision")
        repuesta = input("Consideras que tienes lo necesario para salvar a las personas?:\n")
        if repuesta == 'si':
            print("entonces vamos a actuar.")
            repuesta = input("Vas a atacar al villano? ")
            if repuesta == 'si':
                if villano == 'fuerte':
                    print("Te sientes confiado! Ten cuidado con la seguridad del civil")
                    repuesta = input ("Acertaste el golpe? ")
                    if repuesta == 'si':
                        print("Gran golpe vaquero, lograste poner a salvo al civil!")
                    else:
                        print("Fallar te pudo haber costado caro, pero lograste salvar al civil.")
                        vulnerable -= 10
                else:
                    print("Hora de atacar, acertaste un gran ataque y salvaste al civil")
            else:
                print("movimiento veloz y salvamos al civil sin recibir mucho daño")
                vulnerable -= 5
    else:
        print("Evalua la situacion")
else:
    print("Evalua la situacion")
    
if villano == "fuerte":
        repuesta = input("¿Quieres pedir refuerzos?:\n")
        if repuesta == "si":
            refuerzos = 'si'
            print("Estas esperando refuerzos (15 a 20 minutos)")
            repuesta = input("los refuerzos llegaron a tiempo:\n")
            if repuesta == "si":
                print("puedes entrar a la batalla")
            else:
                print("consigue tiempo hasta que lleguen los refuerzos")
                vulnerable -= 10
        else:
            refuerzos = 'no'
            repuesta = input("¿te sintes confiado para tener una batalla?:\n")
            if repuesta == "si":
                print("Estas en la batalla\n")
                vulnerable -= 20
            else:
                print("evalua la situacion\n")
else:
    print("como eres tan fuerte ya estas en la batalla\n")
    refuerzos = 'no'

if refuerzos == 'si':
    print("Robin y BatMan han llegado la pelea se hace mas sencilla.")
    print("Aunque Bane opone resistencia logran vencer con exito.")
    vidaVil -= 80
else:
    repuesta = input("Bane te ataca como un salvaje. Esquivas a la derecha o la izquierda?\n")
    if repuesta == 'izquierda':
        print("Bane te alcanzo, fallaste en esquivar y te acerto un golpe critico")
        vulnerable -= 20
    else:
        print("Esquivaste con exito, y has logrado derribar a Bane")
        vidaVil -= 25
    repuesta = input("Y vuelve al ataque pero esta vez por tu espalda.\ngolpear o esquivar?\n")
    if repuesta == 'golpear':
        print("Bane detiene tu golpe y te rompe la mano. xc")
        vulnerable -= 25
    else:
        print("Gran esquivada, su brazo se atoro en una reja")
        repuesta = input("tienes la opcion de golpear su abdomen o desconectar sus valvulas de liquido.\n")
        if repuesta == 'golpear':
            print("Rompiste sus costillas pero esto lo enfurece y te manda a volar luego de liberarse")
            vulnerable -= 20
        else:
            print("Ha perdido fuerza luego de desconectar el liquido que lo hace fuerte")
            vidaVil -= 40
        
if vulnerable <= vidaVil:
    print("estas muy vulnerable que quieres hacer?")
    repuesta = input("quieres recuperarte o seguir luchando:\n")
    if repuesta == "recuperarte":
        print("La ciudad esta en riesgo, mejorate pronto para que no nos muramos")
    elif repuesta == "luchar":
        print("Estas en peligro!! te estas muriendo")
else:
    print("Felicidades vencieron al villano.")
