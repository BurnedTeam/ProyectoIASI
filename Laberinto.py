from estado import Estado
import copy

    
#Posicion de la meta
global metax
global metay
global totalMonedas

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
        
# def ordenarAbiertos(): 
#     n=len(abiertos)
    
#     for i in range(n-1):
#         for j in range(n-1-i):
#             if abiertos[j].getHeuristica(totalMonedas, metax, metay) + abiertos[j].totalMovs > abiertos[j+1].getHeuristica(totalMonedas, metax, metay) + abiertos[j+1].totalMovs:
#                 abiertos[j], abiertos[j+1]=abiertos[j+1], abiertos[j]

def movimiento(node, parent):
    if node.x < parent.x and node.y < parent.y:
        return 'Izquierda Arriba'
    elif node.x < parent.x and node.y > parent.y:
        return 'Izquierda Abajo'
    elif node.x > parent.x and node.y < parent.y:
        return 'Derecha Arriba'
    elif node.x > parent.x and node.y > parent.y:
        return 'Derecha Abajo'
    elif node.x < parent.x:
        return 'Iquierda'
    elif node.x > parent.x:
        return 'Derecha'
    elif node.y < parent.y:
        return 'Arriba'
    elif node.y > parent.y:
        return 'Abajo'

def expansionesDeEstado(padre):
    global metax
    global metay
    global totalMonedas
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
                    aux.movimientoRealizado = movimiento(aux, padre)
                    if aux.tablero[x][y] in range(1, 6):
                        aux.coin = padre.coin + aux.tablero[x][y]
                    else:
                        aux.coin = padre.coin
                    aux.tablero = copy.deepcopy(padre.tablero)
                    aux.tablero[x][y] = 8
                    aux.tablero[i][j] = 0
                    if(round(aux.getHeuristica(totalMonedas,metax,metay),3)< round(padre.getHeuristica(totalMonedas,metax,metay),3)):
                        encontrado=True
                        print("El nuevo estado actual es :",aux.x,aux.y)
                        printLaberinto(aux.tablero)
                        return aux
        encontrado=True            
                    

    return None 
                
def expandir():
    global metax
    global metay
    global totalMonedas
    while True:
        estadoact= solucion[-1]
        print("Nuevo estado a desarollar",estadoact.x,estadoact.y,"que tiene las siguientes monedas",estadoact.coin)
        monedax,moneday=estadoact.getMonedaCercana()
        print("la moneda mas cercana ahora mismo es ", monedax, moneday)
        if estadoact.x == metax and estadoact.y == metay and estadoact.coin >= totalMonedas:
            print("resuelto por escalada")
            return solucion
        elif estadoact.x == metax and estadoact.y == metay:
            print("llegado a la solucion pero con :", estadoact.coin," monedas necesitando :",totalMonedas)
            return 0
        else:
            hijo=expansionesDeEstado(estadoact)
            if hijo != None:
                solucion.append(hijo)
            else:
                print("no se puede resolver  por escalada")
                return 0

        

def mostrarsolucion():
    while solucion:
        estadoMostrar=solucion.pop()
        print (estadoMostrar.movimientoRealizado)
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
    n, laberinto = lectura_fichero("LABECOIN1.txt")
    print("n:", n)
    print("laberinto a resolver:")
    printLaberinto(laberinto)
    
    localizarmeta(laberinto)
    x, y=locateBot(laberinto)
    EstadoBase= Estado(x, y, 0, laberinto, " ", 0, None)
    #añadir a la cola 
    solucion.append(EstadoBase)    
    print("las posicion original del robot es :", x,y, "la cual tiene una euristica inicial de :",EstadoBase.getHeuristica(totalMonedas,metax,metay) )
    monedax,moneday=EstadoBase.getMonedaCercana()
    print("la moneda mas cercana ahora mismo es ", monedax, moneday)
    print("la posicion de la meta es ",metax,metay)
    expandir()

    
if __name__ == '__main__':
    main()

#Usar un vector para guardar los estados en los que hemos ido pasando y cuando lleguemos al objetivo el vector sera la solucion
#Escalada simple: en cuanto encuntre un estado mejor pasa a ese estado y si llega a un punto que no hay estados mejores vuelve uno atras (se relaja)
#Maxima pendiente: va mirando posibles estados y nos quedamos con el que este mas cerca de la salida. Si no hay mejores hace lo mismo que en escalada simple

#Colas
#nombre.put(heuristica, estado)
#nombre.get()[1]
