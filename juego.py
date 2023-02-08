global posx
global posy
global metax
global metay
import time
import os
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

def moverizquierda(laberinto):
    global posx
    global posy
    if posx > 0 and laberinto[posy][posx-1] != 9:
        laberinto[posy][posx] = 0
        posx = posx - 1
        laberinto[posy][posx] = 8
    return laberinto


def moverderecha(laberinto):
    global posx
    global posy
    if posx > 0 and laberinto[posy][posx+1] != 9:
        laberinto[posy][posx] = 0
        posx = posx + 1
        laberinto[posy][posx] = 8
    return laberinto
    
    
def moverabajo(laberinto):
    global posx
    global posy
    if posx > 0 and laberinto[posy+1][posx] != 9:
        laberinto[posy][posx] = 0
        posy = posy + 1
        laberinto[posy][posx] = 8
    return laberinto 
 
def moverarriba(laberinto):
    global posx
    global posy
    if posx > 0 and laberinto[posy-1][posx] != 9:
        laberinto[posy][posx] = 0
        posy = posy - 1
        laberinto[posy][posx] = 8
    return laberinto
      
def pintarlaberinto(laberinto):
    os.system('cls' if os.name == 'nt' else 'clear')
    for linea in laberinto:
        columna=0
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
    print()
    
    
    
    
def localizarrobot(laberinto):
    fila=0
    for linea in laberinto:
        columna=0
        for valor in linea: 
            if valor==8:
                global posx
                global posy
                posy=fila
                posx=columna
            columna=columna+1            
        fila=fila+1
   
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
        
        
def control_robot(laberinto, direccion):
    if direccion == 'w':
        laberinto = moverarriba(laberinto)
    elif direccion == 's':
        laberinto = moverabajo(laberinto)
    elif direccion == 'a':
        laberinto = moverizquierda(laberinto)
    elif direccion == 'd':
        laberinto = moverderecha(laberinto)
    pintarlaberinto(laberinto)
    return laberinto
                       
def main_loop(laberinto):
    global posx
    global posy
    global metax
    global metay
    while True:
        pintarlaberinto(laberinto)
        direccion = input("Introduce z para salir o una dirección  (w/a/s/d): ")
        if direccion == 'z':
            break
        laberinto = control_robot(laberinto, direccion)
        if posy==metay and posx == metax:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("¡Has ganado!")
            break
        #time.sleep(0.5)
if __name__ == '__main__':
    n, laberinto = lectura_fichero("LABECOIN3.txt")
    localizarrobot(laberinto)
    localizarmeta(laberinto)
    print(posx,posy)
    print(metax,metay)
    main_loop(laberinto)
