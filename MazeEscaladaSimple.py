import sys
from estadoEscaladas import Estado
from colorama import Style, init, Fore


#from termcolor import colored

import IASIKit as IASI
import os 
import copy
import time
import msvcrt as ms


    
#Posicion de la meta
global metax
global metay
global trama
global totalMonedas
global resuelto
global nodos

logo="""
███████╗███████╗ ██████╗ █████╗ ██╗      █████╗ ██████╗  █████╗     ███████╗██╗███╗   ███╗██████╗ ██╗     ███████╗
██╔════╝██╔════╝██╔════╝██╔══██╗██║     ██╔══██╗██╔══██╗██╔══██╗    ██╔════╝██║████╗ ████║██╔══██╗██║     ██╔════╝
█████╗  ███████╗██║     ███████║██║     ███████║██║  ██║███████║    ███████╗██║██╔████╔██║██████╔╝██║     █████╗  
██╔══╝  ╚════██║██║     ██╔══██║██║     ██╔══██║██║  ██║██╔══██║    ╚════██║██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  
███████╗███████║╚██████╗██║  ██║███████╗██║  ██║██████╔╝██║  ██║    ███████║██║██║ ╚═╝ ██║██║     ███████╗███████╗
╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝
"""
#Vector de estados del que sacaremos la solucion con Estado.movimiento
solucion=[]

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
    encontrado=False
    while encontrado==False:    
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if padre.tablero[x][y] not in (8, 9):
                    aux = Estado(x,y,0,padre.tablero,'',1 + padre.totalMovs, padre)
                    nodos=nodos+1
                    aux.movimientoRealizado = IASI.movimiento(aux, padre)
                    if padre.tablero[x][y] in range(1, 7): #esta jocoso el python el 1 es cerrado pero el 7 es abierto jaja saludos
                        aux.coin = padre.coin + padre.tablero[x][y]
                    else:
                        aux.coin = padre.coin
                    aux.tablero = copy.deepcopy(padre.tablero)
                    aux.tablero[x][y] = 8
                    aux.tablero[i][j] = 0
                    if(round(aux.getHeuristica(totalMonedas,metax,metay),3)< round(padre.getHeuristica(totalMonedas,metax,metay),3) or aux.coin > padre.coin ):
                        encontrado=True
                        if trama==1:
                            print("El nuevo estado a desarollares :",aux.x,aux.y)
                            IASI.printLaberinto(aux.tablero)
                        return aux
        encontrado=True            
                

    return None 
                
def expandir():
    global metax
    global metay
    global totalMonedas
    global trama
    global resuelto
    while True:
        estadoact= solucion[-1]
        if trama==1:
            print("")
            print("")
            print(Fore.LIGHTBLUE_EX+"_________________________________________________")
            print("")
            print("")
            print(Fore.GREEN+"Nuevo estado a desarollar",estadoact.x,estadoact.y,"que tiene las siguientes 💲",estadoact.coin)
            print("")
        monedax,moneday=estadoact.getMonedaCercana()
        if trama==1:
            print(Fore.CYAN+"la moneda mas cercana ahora mismo es ", monedax, moneday)
        if estadoact.x == metax and estadoact.y == metay and estadoact.coin >= totalMonedas:
            if trama==1:
                print("")
                print(Fore.GREEN+"Llegada al estado meta")
                print("")
                print(Fore.LIGHTBLUE_EX+"_________________________________________________")

            print("")            
            print(Fore.RED + Style.BRIGHT + "RESUELTO POR ESCALADA")
            print(Style.NORMAL+"")            

            resuelto=True
            
            return solucion

        elif estadoact.x == metax and estadoact.y == metay:
            print("")
            print("")
            print(Fore.RED +"LLEGADO A LA SOLUCION PERO CON  :", estadoact.coin," 💲 Y NECESITAVA :",totalMonedas)
            resuelto=False
            return 0
        else:
            hijo=expansionesDeEstado(estadoact)
            if hijo != None:
                solucion.append(hijo)
            else:
                if trama==1:
                    print("Llegada al estado final")
                    print("")
                    print(Fore.LIGHTBLUE_EX+"_________________________________________________")

                print("")
                print(Fore.RED +Style.BRIGHT +"NO SE PUEDE RESOLVER POR ESCALADA")
                resuelto=False
                print("NO HAY UN ESTADO CON MEJOR EURISTICA QUE EL ACTUAL")
                print(Style.NORMAL+"")

                #IASI.printLaberinto(estadoact.tablero)
                return 0

def EscaladaSimple(debug):
    global metax
    global metay
    global trama
    global nodos
    global totalMonedas
    nodos=0
    
    
    key='a'
    while((key != b'\r') and key != b'\x1b'):
        while ms.kbhit():
            ms.getch()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.RED + logo + Fore.RESET)
        game=input(Fore.MAGENTA+"Que laberinto deseas jugar: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        n, laberinto = IASI.lectura_fichero("Laberintos/LABECOIN"+game+".txt")   
        totalMonedas=n
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Monedas necesarias: "+Fore.YELLOW+ str(n)+ Fore.RESET)
        print(Fore.GREEN+"Laberinto a resolver:")
        IASI.printLaberinto(laberinto)
        print("")
        print(Fore.LIGHTBLUE_EX+Style.BRIGHT+"Pulse:    Enter para resolver")
        print(Style.NORMAL+Fore.BLUE+"          Cualquier otro botón para seleccionar otro laberinto")
        print(Style.NORMAL+Fore.BLUE+"          ESC Para cerrar la aplicación"+ Fore.RESET)
        key= ms.getch()
    if(key == b'\x1b'):
        sys.exit()
    #"0:Debug Desactivado"
    #"1:Debug Basico"
    if(debug>0):
        trama = 1
    else:
        trama=0

    print(Style.NORMAL+"")
    inicio_tiempo = time.time()

    os.system('cls' if os.name == 'nt' else 'clear')

    metax, metay = IASI.localizarmeta(laberinto)
    x, y=IASI.locateBot(laberinto)
    EstadoBase= Estado(x, y, 0, laberinto, " ", 0, None)
    #añadir a la cola 
    solucion.append(EstadoBase)
    if(trama==1):    
        print(Fore.CYAN+"las posicion original del robot es :", x,y, "la cual tiene una euristica inicial de :",EstadoBase.getHeuristica(totalMonedas,metax,metay) )
    monedax,moneday=EstadoBase.getMonedaCercana()
    if(trama==1):
        print("la 💲💲💲 mas cercana ahora mismo es ", monedax, moneday)
        print("la posicion de la meta es ",metax,metay)      
        print("")
        print("")
        print("")

    expandir()

    tiempo_transcurrido = time.time() - inicio_tiempo
    print(Fore.RED+"Tiempo transcurrido:", tiempo_transcurrido)
    print(Fore.RED+"Nodos generados:",   nodos)
    print("")
    if(resuelto):
        IASI.mostrarsolucion(solucion)
        print(Fore.YELLOW+"¿Quieres una visualizacion grafica de la solucion? (S/N): ")
    else:
        print(Fore.YELLOW+"¿Quieres una visualizacion grafica del intento? (S/N): ")
    
    key=ms.getch()
    if key == b'S' or key== b's':
        IASI.mostrassoluciongrafica(solucion) 
    if(resuelto):
        print("")
        print("GoodGame wp")       
    print(Style.NORMAL+Fore.WHITE+"")
    
        
