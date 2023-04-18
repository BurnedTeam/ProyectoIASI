from estadoA import Estado
from colorama import Style, init, Fore
import IASIKit as IASI

import copy
import time
import msvcrt as ms
import os 
import queue


logom="""""

 █████╗           
██╔══██╗   ▀▄ ██ ▄▀
███████║     ████ 
██╔══██║   ▄▀ ██ ▀▄
██║  ██║       
╚═╝  ╚═╝          
                  
"""



#Posicion de la meta
global metax
global metay
global totalMonedas
global trama
global resuelto
global nodos
movsR = queue.Queue()
#Vector de estados del que sacaremos la solucion con Estado.movimiento
solucion=[]
#Cola de estados por los que podemos seguir avanzando
abiertos=[]
#Vecator de estados de los que ya hemos desarrollado sus hijos
cerrados=[]
        


def expansionesDeEstado(padre):
    global metax
    global metay
    global totalMonedas
    global trama
    global nodos
    hijos = []
    x = padre.x
    y = padre.y
    i = padre.x
    j = padre.y 
    if (trama==2 or trama==3):
        print("Estudio de los alrededores: x,y,valor")   
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if (trama==2):
                print(x,y,padre.tablero[x][y])
            if padre.tablero[x][y] not in (8, 9):
                aux = Estado(x,y,0,padre.tablero,'',1 + padre.totalMovs, padre,0)
                nodos=nodos+1
                aux.movimientoRealizado = IASI.movimiento(aux, padre)
                if aux.tablero[x][y] in range(1, 7):
                    aux.coin = padre.coin + aux.tablero[x][y]
                else:
                    aux.coin = padre.coin
                aux.tablero = copy.deepcopy(padre.tablero)
                aux.tablero[x][y] = 8
                aux.tablero[i][j] = 0
                hijos.append(aux)
    for hijo in hijos:
        if(trama==1 or trama== 2 or trama== 3):
            print(Fore.CYAN+"los posibles estados a los que ir son: ",hijo.x,hijo.y,end=" ")
            print("con euristica: ",round(hijo.getHeuristica(totalMonedas,metax,metay),3))
        hijo.setHeuristica(totalMonedas,metax,metay)
    
        
    if len(hijos) == 0:
        if(trama==2 or trama==3):
            print("no hay mas estados posibles a los que ir")

    return hijos 
                
def expandir():
    global abiertos
    global metax
    global metay
    global totalMonedas
    global trama
    global resuelto
    i=0
    while len(abiertos)>0:
        estadoact=abiertos.pop(0)
        
        if(trama==1 or trama==2 or trama==3):
            print(Fore.YELLOW+"Desarollando estado",estadoact.x,estadoact.y)
            print(Fore.YELLOW+"La meta esta en ",metax,metay)
            print("El estado tiene la siguiente euristica:")
            print(round(estadoact.getHeuristica(totalMonedas, metax, metay)))
        if(trama==2 or trama==3):       
            print("El estado tiene el siguiente laberitno")
            IASI.printLaberinto(estadoact.tablero)
    
        cerrados.append(estadoact)
        if estadoact.x == metax and estadoact.y == metay and estadoact.coin >= totalMonedas:
            print(Fore.RED+"LABERINTO RESUELTO")
            solucion.append(estadoact)
            while estadoact.estadoPadre :
                solucion.append(estadoact.estadoPadre)
                estadoact=estadoact.estadoPadre
                resuelto=True
            return solucion
        else:
            if(estadoact.x == metax and estadoact.y == metay):
                if(trama==2 or trama==3):
                    print(Fore.RED+"LLEGADA A META SIN SER CORRECTO")
            else:
                hijos = expansionesDeEstado(estadoact)
                i=i+1
                for hijo in hijos:
                    if hijo not in abiertos and hijo not in cerrados:
                        abiertos.append(hijo)
                        if(trama==3):
                            print(Fore.BLUE+"Nuevo estado agregado con el siguiente laberinto")   
                            IASI.printLaberinto(hijo.tablero)
                            time.sleep(0.5)

                abiertos = sorted(abiertos, key=lambda Estado: Estado.heuristica)

        if(trama==3):
            print(Fore.RED+"Bucle abierto otra iteraccion")
    if(trama==1 or trama==2 or trama==3):
        print(Fore.RED+"Final Expandir")    
    print(Fore.RED+"ESTE LABERINTO NO TIENE SOLUCION POSIBLE")
    resuelto=False
    
def AEstrella():
    global trama
    global metax
    global metay
    global abiertos
    global resuelto
    global nodos
    global resuelto
    nodos=0
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + logom + Fore.RESET)
    

    game=input(Fore.MAGENTA+"Que laberinto deseas jugar: ")
    n, laberinto = IASI.lectura_fichero("Laberintos/LABECOIN"+game+".txt")    
    global totalMonedas
    totalMonedas=n
    print("n:", n)
    print("laberinto a resolver:")
    IASI.printLaberinto(laberinto)
    print("")
    print("")

    
    print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"0:Debug Desactivado")
    print(Style.NORMAL+"1:Debug Basico")
    print("2:Debug Avanzado")
    print("3:Debug Todo")


    trama = int(input(Fore.CYAN+Style.BRIGHT+"Indica el nivel de la trama: "))
    print(Style.NORMAL+"")
    inicio_tiempo = time.time()
    os.system('cls' if os.name == 'nt' else 'clear')
    monedaslaberinto=IASI.sumamonedas(laberinto)
    metax, metay = IASI.localizarmeta(laberinto)
    if(trama==1 or trama==2 or trama==3):
        print(Fore.CYAN+"LA Posicion de la meta",metax,metay)
    x, y=IASI.locateBot(laberinto)
    EstadoBase= Estado(x, y, 0, laberinto, " ", 0, None,0.0)
    #añadir a la cola 
    EstadoBase.setHeuristica(totalMonedas,metax,metay)

    abiertos.append(EstadoBase)

    abiertos = sorted(abiertos, key=lambda Estado: Estado.heuristica)
    if(monedaslaberinto>=n):
        expandir()
        if(resuelto):
            IASI.mostrarsolucionALT(solucion)
        tiempo_transcurrido = time.time() - inicio_tiempo
        print(Fore.RED+"Tiempo transcurrido:", tiempo_transcurrido)
        print(Fore.RED+"Nodos generados:", nodos)
        print("")
        if(resuelto):
            print(Fore.YELLOW+"¿Quieres una visualizacion grafica de la solucion? (S/N): ")
            key=ms.getch()
            if key == b'S' or key== b's':
                IASI.mostrassoluciongraficaALT(solucion, movsR)
                print("")
                print("GoodGame wp")
                # Crear la carpeta Laberintos si no existe
                if not os.path.exists('Soluciones'):
                    os.makedirs('Soluciones')
                with open("Soluciones/SOLUCION"+game+".txt", "w") as file:
                    while not movsR.empty():
                        file.write(movsR.get() + "\n")   
    else:   
        print(Fore.RED+"NO HAY MONEDAS EN EL LABERINTO SUFICIENTES PARA PASARLO")
        tiempo_transcurrido = time.time() - inicio_tiempo
        print(Fore.RED+"Tiempo transcurrido:", tiempo_transcurrido)
        print(Fore.RED+"Nodos generados:", nodos)
    print(Fore.WHITE+Style.NORMAL+"")
    
