from estado import Estado
import copy
from colorama import Style, init, Fore
from termcolor import colored
    
#Posicion de la meta
global metax
global metay
global totalMonedas
global trama
#Vector de estados del que sacaremos la solucion con Estado.movimiento
solucion=[]



def lectura_fichero(nom_fichero):
    # Abrir el archivo con nombre especificado en el parámetro "nom_fichero" en modo lectura ('r')
    with open(nom_fichero, 'r') as fichero: 
        # Leer la primera línea del archivo, convertirla a entero y almacenarlo en la variable "n"
        n = int(fichero.readline().strip())
        # Inicializar una matriz vacía "laberinto"
        laberinto = []
        # Procesar el archivo línea por línea
        for line in fichero:
            # Inicializar una lista vacía "linea"
            linea = []
            # Procesar cada valor en la línea actual y agregarlo a la lista "linea" como un entero
            for value in line.strip().split(','):
                try:                     
                    linea.append(int(value))
                except ValueError:
                    # Si el valor no puede ser convertido a entero, se omite
                    pass
            # Agregar la lista "linea" al final de la matriz "laberinto"
            if linea:
                laberinto.append(linea)
        #Cierre del fichero
        fichero.close()
        # Retornar los valores de "n" y "laberinto"
        global totalMonedas
        totalMonedas=n

        return n, laberinto



           
#Localiza la posicion del robot
def locateBot(laberinto):
    for i, linea in enumerate(laberinto):
        for j, valor in enumerate(linea):
            if valor == 8:
                return i, j
    return -1,-1

#Localizar la posicion de la meta   
def localizarmeta(laberinto):    
    fila=0
    for linea in laberinto:
        columna=0
        for valor in linea: 
            if valor==7:
                global metax
                global metay
                metay=columna
                metax=fila
            columna=columna+1            
        fila=fila+1 
        


def movimiento(node, parent):
    if node.x < parent.x and node.y < parent.y:
        return 'Izquierda Arriba'
    elif node.x < parent.x and node.y > parent.y:
        return 'Derecha Arriba'
    elif node.x > parent.x and node.y < parent.y:
        return 'Izquierda Abajo '
    elif node.x > parent.x and node.y > parent.y:
        return 'Derecha Abajo'
    elif node.x < parent.x:
        return 'Arriba'
    elif node.x > parent.x:
        return 'Abajo'
    elif node.y < parent.y:
        return 'Iquierda'
    elif node.y > parent.y:
        return 'Derecha'

def expansionesDeEstado(padre):
    global metax
    global metay
    global totalMonedas
    global trama

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
                aux = Estado(x,y,0,padre.tablero,'',1 + padre.totalMovs, padre)
                aux.movimientoRealizado = movimiento(aux, padre)
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
            print("Nuevo estado a desarollar",estadoact.x,estadoact.y,"que tiene las siguientes monedas",estadoact.coin)
        monedax,moneday=estadoact.getMonedaCercana()
        if(trama==1 or trama ==2):
            print("la moneda mas cercana ahora mismo es ", monedax, moneday)
        EstadoMejor= Estado
        if estadoact.x == metax and estadoact.y == metay and estadoact.coin >= totalMonedas:
            print("")
            print("")
            print("")            
            print(Fore.RED+"RESUELTO POR ESCALADA MAXIMA PENDIENTE")
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
                    printLaberinto(EstadoMejor.tablero)
                solucion.append(EstadoMejor)
            else:
                print("")
                print("")
                print("")
                print(Fore.RED+Style.BRIGHT +"NO HAY ESTADO CON MEJOR EURISTICA QUE EL ACTUAL")
                print(Fore.RED+"IMPOSIBLE RESOLVER POR ESCALADA MAXIMA PENDIENTE")
                print(Fore.RED+"NOS QUEDARIA EL SIGUIENTE LABERINTO")
                printLaberinto(estadoact.tablero)
                
                return 0

        

def mostrarsolucion():
    print(Style.NORMAL+Fore.WHITE+"")

    print(Style.NORMAL+Fore.GREEN+"Los movientos realizados son:")
    while solucion:
        estadoMostrar=solucion.pop(0)
        print(Fore.GREEN+estadoMostrar.movimientoRealizado)
    print(Style.NORMAL+Fore.WHITE+"")
def printLaberinto(laberinto):
    print()
    for linea in laberinto:
        for valor in linea:
            if valor==0:
                print(" " ,end=" ")
            elif valor==9:
                print("🟫",end="") 
            elif valor==8:
                print("🤖",end="") 
            elif valor==7:
                print("🚩",end="") 
            else :
                print("💲",end="") 
        print() 
    
def main():
    global metax
    global metay
    global trama

    n, laberinto = lectura_fichero("LABECOIN3.txt")
    print("n:", n)
    print("laberinto a resolver:")
    printLaberinto(laberinto)
    
    print(Fore.MAGENTA+"0 sin Trama")
    print("1 Trama basica")
    print("2 Trama Avanzada")

    trama = int(input("Indica el nivel de la trama: "))
    print("")
    
    localizarmeta(laberinto)
    x, y=locateBot(laberinto)
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
    mostrarsolucion()

    
if __name__ == '__main__':
    main()

