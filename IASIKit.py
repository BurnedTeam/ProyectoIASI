from colorama import Style, init, Fore
import config
import time
import os 



def printLaberinto(laberinto):
    
    if config.safegraphic:
        print()
        for linea in laberinto:
            for valor in linea:
                if valor==0:
                    print(" " ,end=" ")
                elif valor==9:
                    print(Fore.LIGHTRED_EX+"██",end="") 
                elif valor==8:
                    print(Fore.CYAN+"O ",end="") 
                elif valor==7:
                    print(Fore.YELLOW+"██",end="") 
                else :
                    print(Fore.RESET+str(valor)+" ",end="") 
            print() 
        print(Fore.RESET)
    else:
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
    
def mostrarsolucion(solucion):
    for estadoMostrar in solucion:
        print(Fore.GREEN + estadoMostrar.movimientoRealizado)
    print(Fore.WHITE+"")
    #IASI.printLaberinto(estadoMostrar.tablero)
    print("")   
    
def mostrassoluciongrafica(solucion):
    for estadoMostrar in solucion:
        os.system('cls' if os.name == 'nt' else 'clear')
        printLaberinto(estadoMostrar.tablero)
        time.sleep(0.5)
    
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
    
#Localizar la posicion de la meta   
def localizarmeta(laberinto):    
    fila=0
    for linea in laberinto:
        columna=0
        for valor in linea: 
            if valor==7:
                return fila, columna
            columna=columna+1            
        fila=fila+1 
        
#Localiza la posicion del robot
def locateBot(laberinto):
    for i, linea in enumerate(laberinto):
        for j, valor in enumerate(linea):
            if valor == 8:
                return i, j
    return -1,-1

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

        return n, laberinto

def mostrassoluciongraficaALT(solucion, movsR):
    for estadoMostrar in reversed(solucion):
        os.system('cls' if os.name == 'nt' else 'clear')
        printLaberinto(estadoMostrar.tablero)
        movsR.put(estadoMostrar.movimientoRealizado)
        time.sleep(0.5)


def mostrarsolucionALT(solucion):
    for estadoMostrar in reversed(solucion):
        print(Fore.GREEN + estadoMostrar.movimientoRealizado)
    print(Fore.WHITE+"")
    #IASI.printLaberinto(estadoMostrar.tablero)
    print("")
def sumamonedas(tablero):
    suma = 0
    for fila in tablero:
        for valor in fila:
            if valor >= 1 and valor <= 6:
                suma += valor
    return suma