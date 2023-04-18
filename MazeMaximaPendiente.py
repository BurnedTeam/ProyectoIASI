import sys
from estadoEscaladas import Estado
import copy
from colorama import Style, init, Fore
import os    
import time
try:
    import msvcrt as ms
except ImportError:
    import getch as ms
import IASIKit as IASI

#Posicion de la meta
global metax
global metay
global totalMonedas
global trama
global nodos
#Vector de estados del que sacaremos la solucion con Estado.movimiento
solucion=[]

logo="""
███╗   ███╗ █████╗ ██╗  ██╗    ██████╗ ███████╗███╗   ██╗██████╗ ██╗███████╗███╗   ██╗████████╗███████╗
████╗ ████║██╔══██╗╚██╗██╔╝    ██╔══██╗██╔════╝████╗  ██║██╔══██╗██║██╔════╝████╗  ██║╚══██╔══╝██╔════╝
██╔████╔██║███████║ ╚███╔╝     ██████╔╝█████╗  ██╔██╗ ██║██║  ██║██║█████╗  ██╔██╗ ██║   ██║   █████╗  
██║╚██╔╝██║██╔══██║ ██╔██╗     ██╔═══╝ ██╔══╝  ██║╚██╗██║██║  ██║██║██╔══╝  ██║╚██╗██║   ██║   ██╔══╝  
██║ ╚═╝ ██║██║  ██║██╔╝ ██╗    ██║     ███████╗██║ ╚████║██████╔╝██║███████╗██║ ╚████║   ██║   ███████╗
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚═╝     ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝
"""
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
    if (trama==2):
        print("Estudio de los alrededores: x,y,valor")   
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if (trama==2):
                print(x,y,padre.tablero[x][y])
            if padre.tablero[x][y] not in (8, 9):
                nodos=nodos+1
                aux = Estado(x,y,0,padre.tablero,'',1 + padre.totalMovs, padre)
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
        if(trama==1 or trama ==2):
            print("los posibles estados a los que ir son: ",hijo.x,hijo.y,end=" ")
            print("con euristica: ",round(hijo.getHeuristica(totalMonedas,metax,metay),3))
    if len(hijos) == 0:
        if(trama==1 or trama ==2):
            print("no hay mas estados posibles a los que ir")

    return hijos 
                
def expandir():
    global metax
    global metay
    global totalMonedas
    global trama

    while True:
        estadoact= solucion[-1]
        if(trama==1 or trama ==2):                   
            print(Fore.LIGHTBLUE_EX+"_________________________________________________")
            print("")
            print(Fore.GREEN+"Nuevo estado a desarollar",estadoact.x,estadoact.y,"que tiene las siguientes monedas",estadoact.coin)
            print("")
        monedax,moneday=estadoact.getMonedaCercana()
        if(trama==1 or trama ==2):
            print(Fore.CYAN+"la moneda mas cercana ahora mismo es ", monedax, moneday)
        EstadoMejor= Estado
        if estadoact.x == metax and estadoact.y == metay and estadoact.coin >= totalMonedas:
            print("")
            print("")
            print("")            
            print(Fore.RED+Style.BRIGHT+"RESUELTO POR ESCALADA MAXIMA PENDIENTE")
            print(Style.NORMAL+"")
            global exito
            exito=True
            return solucion
        if estadoact.x == metax and estadoact.y == metay:
            print("")
            print("")            
            print(Fore.RED+Style.BRIGHT+"LLEGADA A LA META PERO SIN LAS MONEDAS NECESARIAS")
            print(Style.NORMAL+"")
            return solucion
        else:
            hijos=expansionesDeEstado(estadoact)
            EstadoMejor=hijos[0]
            for hijo in hijos:
                if(EstadoMejor.coin <hijo.coin and EstadoMejor.coin<totalMonedas):
                        EstadoMejor=hijo
                else:
                    if(EstadoMejor.getHeuristica(totalMonedas,metax,metay)> hijo.getHeuristica(totalMonedas,metax,metay) and hijo.coin>= EstadoMejor.coin):
                        EstadoMejor=hijo
            if(trama==2):            
                print("los estados a compara esta vez son los de euristica: ",round(EstadoMejor.getHeuristica(totalMonedas,metax,metay),2),round(estadoact.getHeuristica(totalMonedas,metax,metay),2))       
            if EstadoMejor.getHeuristica(totalMonedas,metax,metay) < estadoact.getHeuristica(totalMonedas,metax,metay) or EstadoMejor.coin >estadoact.coin:
                if(trama ==2):
                    print("El nuevo estado actual es :",EstadoMejor.x,EstadoMejor.y)
                if(trama==1 or trama ==2):
                    IASI.printLaberinto(EstadoMejor.tablero)
                solucion.append(EstadoMejor)
            else:
                print("")
                if trama==1 or trama ==2:
                    print(Fore.LIGHTBLUE_EX+"_________________________________________________")
                    print("")
                    print("")
                    print(Fore.RED+"NO HAY ESTADO CON MEJOR EURISTICA QUE EL ACTUAL")
                    print("")
                print("")
                print(Fore.RED+Style.BRIGHT+"IMPOSIBLE RESOLVER POR ESCALADA MAXIMA PENDIENTE")
                print(Style.NORMAL+"")
                print("")        
                return 0   
    
def MaximaPendiente(debug):
    global exito
    global metax
    global metay
    global trama
    global nodos
    global totalMonedas
    nodos=0
    exito=False
    
    key='a'
    while((key != b'\r') and key != b'\x1b' and key !='\n'):
        IASI.flushInputs()
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
    if(debug>1):
        trama = 2
    elif(debug==1):
        trama = 1
    else:
        trama=0
        
        
    print(Style.NORMAL+"")
    inicio_tiempo = time.time()

    metax, metay = IASI.localizarmeta(laberinto)
    x, y = IASI.locateBot(laberinto)
    EstadoBase= Estado(x, y, 0, laberinto, " ", 0, None)
    #añadir a la cola 
    solucion.append(EstadoBase)    
    if(trama==1 or trama==2):
        print(Fore.CYAN+"las posicion original del robot es :", x,y, "la cual tiene una euristica inicial de :",EstadoBase.getHeuristica(totalMonedas,metax,metay) )
    monedax,moneday=EstadoBase.getMonedaCercana()
    if(trama==1 or trama==2):
        print("la moneda mas cercana ahora mismo es ", monedax, moneday)
        print("la posicion de la meta es ",metax,metay)
        print("")
        print("")
        print("")
        
        

    expandir()
    tiempo_transcurrido = time.time() - inicio_tiempo
    print(Fore.RED+"Tiempo transcurrido:", tiempo_transcurrido)
    print(Fore.RED+"Nodos generados:",   nodos)
    if(exito):
        IASI.mostrarsolucion(solucion)
        print(Fore.YELLOW+"¿Quieres una visualizacion grafica de la solucion? (S/N): ")
    else:
        print(Fore.YELLOW+"¿Quieres una visualizacion grafica del intento? (S/N): ")
    
    key=ms.getch()
    if key == b'S' or key== b's':
        IASI.mostrassoluciongrafica(solucion) 
    if(exito):
        print("")
        print("GoodGame wp")        
    print(Style.NORMAL+Fore.WHITE+"")
    
