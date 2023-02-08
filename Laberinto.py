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
    
def pintar_estado(laberinto):
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
                print("🟢",end="") 
        print() 
        

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
             
def locateBot(laberinto):
    for i, linea in enumerate(laberinto):
        for j, valor in enumerate(linea):
            if valor == 8:
                return i, j, len(linea)
    return -1,-1,-1

def jugar(laberinto):
    puntos=0
    win=False
    i, j, LengLine = locateBot(laberinto)
    while win==False:
        pintar_estado(laberinto)
        print("Tienes "+ str(puntos)+" puntos")
        print("   W      ⬆")
        print(" A S D  ⬅ ⬇ ➡")
        boton=input("Pulsa una tecla para moverte: ")
        if boton in ('A','W','S','D', 'AW','WA', 'AS','SA','DS', 'SD', 'DW','WD'):
            laberinto,puntos,win,i,j=mover(laberinto,boton,puntos,win,i,j,LengLine)
    
    
    pintar_estado(laberinto)
    print("¡FELICIDADES HAS GANADO Y ENCIMA HAS CONSEGUIDO "+ str(puntos)+ " PUNTOS!")
        

def main():
    game=input("Que laberinto deseas jugar: ")
    n, laberinto = lectura_fichero("LABECOIN"+game+".txt")
    #print("n:", n)
    #print("laberinto:")
    #pintar_estado(laberinto)
    jugar(laberinto)
if __name__ == '__main__':
    main()