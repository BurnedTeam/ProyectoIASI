from estado import Estado
#Importar la biblioteca heapq para la implementación de la cola de prioridad
import queue
    

#Posicion de la meta
global metax
global metay
global totalMonedas

#Vector de estados del que sacaremos la solucion con Estado.movimiento
solucion=[]

#Cola de estados por los que podemos seguir avanzando
abiertos=queue.PriorityQueue()

#Vecator de estados de los que ya hemos desarrollado sus hijos
cerrados=[]

def comparaHijos(hijos):
    abiertosFinal=queue.PriorityQueue()
    cerradosFinal
    for hijo in hijos:
        for cases in cerrados:
            if cases.tablero==hijo.tablero:
                if(cases.totalMovs>hijo.totalMovs):
                    abiertosFinal.put(hijo, hijo.getHeuristica(totalMonedas,metax,metay))
                else:
                    abiertosFinal.put(cases, cases.getHeuristica(totalMonedas,metax,metay))
            else:
                abiertosFinal.put(cases, cases.getHeuristica(totalMonedas,metax,metay))
        
        for cases in abiertos:
            if cases.tablero==hijo.tablero:
                if(cases.totalMovs>hijo.totalMovs):
                    abiertosFinal.put(hijo, hijo.getHeuristica(totalMonedas,metax,metay))
                else:
                    abiertosFinal.put(cases, cases.getHeuristica(totalMonedas,metax,metay))
            else:
                abiertosFinal.put(cases, cases.getHeuristica(totalMonedas,metax,metay))
    abiertos=abiertosFinal

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


def mover(laberinto, movimiento, puntos, win, i, j, lengLine):
    # Obtener las coordenadas actuales de la posición del robot (8)
    x, y = i, j
    # Verificar el movimiento y actualizar las coordenadas según sea necesario
    if movimiento == 'W':
        x = x - 1
    elif movimiento == 'A':
        y = y - 1
    elif movimiento == 'S':
        x = x + 1
    elif movimiento == 'D':
        y = y + 1
    elif movimiento == 'DS' or movimiento == 'SD':
        y = y + 1
        x = x + 1
    elif movimiento == 'AS' or movimiento == 'SA':
        y = y - 1
        x = x + 1
    elif movimiento == 'AW' or movimiento == 'WA':
        y = y - 1
        x = x - 1
    elif movimiento == 'WD' or movimiento == 'DW':
        y = y + 1
        x = x - 1
    
    # Verificar si el nuevo movimiento es posible (no fuera de los límites del laberinto ni colisión con un obstáculo)
    if 0 <= x < len(laberinto) and 0 <= y < lengLine and laberinto[x][y] != 9:
        # Actualizar la posición del robot en el laberinto
        if laberinto[x][y]==7:
            laberinto[i][j] = 0
            i,j,lengLine=locateBot(laberinto)
            if i==-1:
                win=True
                laberinto[x][y] = 8
            else:
                x,y=i,j
        elif laberinto[x][y]==0:
            laberinto[x][y] = 8
            laberinto[i][j] = 0
        else:
            puntos=puntos+1
            laberinto[x][y] = 8
            laberinto[i][j] = 0
        # Retornar el laberinto actualizado
        return laberinto, puntos, win, x, y
            
    # Retornar el laberinto sin cambios (en caso de no ser posible el movimiento)
    return laberinto, puntos, win, i, j
           
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
                metay=fila
                metax=columna
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
    hijos = []
    x = padre.x
    y = padre.y
    i = padre.x
    j = padre.y
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if padre.tablero[x][y] not in (8, 9):
                aux = Estado(x,y,0,padre.tablero,'',1 + padre.totalMovs, padre)
                #no se como guardamos que moviemiento por que creo que no lo hacemos 
                aux.movimientoRealizado = movimiento(aux, padre)
                if aux.tablero[x][y] in range(1, 6):
                    aux.coin = padre.coin + aux.tablero[x][y]
                else:
                    aux.coin = padre.coin
                aux.tablero[x][y] = 8
                hijos.append(aux)
     
    return hijos 
                
def expandir():
    global metax
    global metay
    global totalMonedas
    while abiertos:
        estadoact=abiertos.get()
        cerrados.append(estadoact)
        #print(estadoact.x,estadoact.y)
        if estadoact.x == metax and estadoact.y == metay and estadoact.coin >= totalMonedas:
            solucion.append(estadoact)
            while estadoact.estadoPadre :
                solucion.append(estadoact.estadoPadre)
                estadoact=estadoact.estadoPadre
            return solucion
        hijos = expansionesDeEstado(estadoact)
        for hijo in hijos:
            if hijo not in abiertos and hijo not in cerrados:
                abiertos.put(hijo, hijo.getHeuristica(totalMonedas,metax,metay))        

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
    n, laberinto = lectura_fichero("LABECOIN1.txt")
    print("n:", n)
    print("laberinto a resolver:")
    printLaberinto(laberinto)
    
    localizarmeta(laberinto)
    x, y=locateBot(laberinto)
    EstadoBase= Estado(x, y, 0, laberinto, " ", 0, None)
    #añadir a la cola 
    abiertos.put(EstadoBase, EstadoBase.getHeuristica(totalMonedas,metax,metay))

    while x!=-1:
        expandir()
        mostrarsolucion()
        x, y=locateBot()
    
if __name__ == '__main__':
    main()

#Usar un vector para guardar los estados en los que hemos ido pasando y cuando lleguemos al objetivo el vector sera la solucion
#Escalada simple: en cuanto encuntre un estado mejor pasa a ese estado y si llega a un punto que no hay estados mejores vuelve uno atras (se relaja)
#Maxima pendiente: va mirando posibles estados y nos quedamos con el que este mas cerca de la salida. Si no hay mejores hace lo mismo que en escalada simple

#Colas
#nombre.put(heuristica, estado)
#nombre.get()[1]
