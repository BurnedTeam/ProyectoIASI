
from estado import Estado

#Posicion de la meta
global metax
global metay

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
                return i, j, len(linea)
    return -1,-1,-1

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




def main():
    n, laberinto = lectura_fichero("LABECOIN1.txt")
    print("n:", n)
    print("laberinto:")
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

if __name__ == '__main__':
    main()

#Usar un vector para guardar los estados en los que hemos ido pasando y cuando lleguemos al objetivo el vector sera la solucion
#Escalada simple: en cuanto encuntre un estado mejor pasa a ese estado y si llega a un punto que no hay estados mejores vuelve uno atras (se relaja)
#Maxima pendiente: va mirando posibles estados y nos quedamos con el que este mas cerca de la salida. Si no hay mejores hace lo mismo que en escalada simple