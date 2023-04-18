import os
import queue
import IASIKit as IASI
from colorama import Style, init, Fore

# Crear variable global
movsR = queue.Queue()

playerL="""
███╗   ███╗ █████╗ ███████╗███████╗██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗       _____
████╗ ████║██╔══██╗╚══███╔╝██╔════╝██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗     |.---.|
██╔████╔██║███████║  ███╔╝ █████╗  ██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝     ||___||
██║╚██╔╝██║██╔══██║ ███╔╝  ██╔══╝  ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗     |+  .'|
██║ ╚═╝ ██║██║  ██║███████╗███████╗██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║     | _ _ |
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝     |_____/
                                                                                    
"""

def mover(laberinto, movimiento, puntos, win, i, j, lengLine, n):
    # Obtener las coordenadas actuales de la posición del robot (8)
    x, y = i, j
    movimiento = movimiento.upper() # Convertir a mayúsculas
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
    if 0 <= x < len(laberinto) and 0 <= y < lengLine and laberinto[x][y] != 9 and (laberinto[x][y]!=7 and puntos<n):
        # Actualizar la posición del robot en el laberinto
        if laberinto[x][y]==7:
            laberinto[i][j] = 0
            i,j,lengLine=IASI.locateBot(laberinto)
            if i==-1:
                win=True
                laberinto[x][y] = 8
            else:
                x,y=i,j
        elif laberinto[x][y]==0:
            laberinto[x][y] = 8
            laberinto[i][j] = 0
        else:
            puntos+=laberinto[x][y]
            laberinto[x][y] = 8
            laberinto[i][j] = 0
        # Retornar el laberinto actualizado
        movsR.put(movimiento)
        return laberinto, puntos, win, x, y
            
    # Retornar el laberinto sin cambios (en caso de no ser posible el movimiento)
    return laberinto, puntos, win, i, j
    
def jugar(laberinto, n):
    puntos=0
    win=False
    i, j = IASI.locateBot(laberinto)
    LengLine=len(laberinto)
    while win==False:
        
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.MAGENTA+"Necesitas "+Fore.RED+str(n-puntos)+Fore.MAGENTA+" monedas para salir"+Fore.RESET)
        IASI.printLaberinto(laberinto)
        print(Fore.GREEN+"Tienes "+ Fore.YELLOW+str(puntos)+Fore.GREEN+" puntos"+Fore.RESET)
        print("   W      ⬆")
        print(" A S D  ⬅ ⬇ ➡")
        boton=input("Pulsa una tecla para moverte: ")
        if boton.lower() in ('a','w','s','d', 'aw','wa', 'as','sa','ds', 'sd', 'dw','wd'):

            laberinto,puntos,win,i,j=mover(laberinto,boton,puntos,win,i,j,LengLine, n)
    
    
    IASI.printLaberinto(laberinto)
    print("¡FELICIDADES HAS GANADO CON "+ str(puntos)+ " MONEDAS!")
        

def MazePlayer():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.RED + playerL + Fore.RESET)
    game=input(Fore.CYAN+"Que laberinto deseas jugar: "+Fore.RESET)
    n, laberinto = IASI.lectura_fichero("Laberintos/LABECOIN"+game+".txt")
    jugar(laberinto,n)
    with open("Soluciones/SOLUCION"+game+".txt", "w") as file:
        while not movsR.empty():
            file.write(movsR.get() + "\n")
