import msvcrt as ms
import os
import config
from colorama import Style, init, Fore
import IASIKit as IASI
 
 
logoM = """

███╗   ███╗ █████╗ ███████╗███████╗    ███╗   ███╗ █████╗ ██╗  ██╗███████╗██████╗        ,
████╗ ████║██╔══██╗╚══███╔╝██╔════╝    ████╗ ████║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗      /(  ___________
██╔████╔██║███████║  ███╔╝ █████╗      ██╔████╔██║███████║█████╔╝ █████╗  ██████╔╝     |  >:===========`
██║╚██╔╝██║██╔══██║ ███╔╝  ██╔══╝      ██║╚██╔╝██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗      )(
██║ ╚═╝ ██║██║  ██║███████╗███████╗    ██║ ╚═╝ ██║██║  ██║██║  ██╗███████╗██║  ██║      ""
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                  
"""

downrrow="""
  ██          ██╗      
    ██      ██╔═╝
      ██  ██╔═╝ 
        ██╔═╝ 
        ╚═╝
"""     

def pintar_estado(laberinto, x, y, n):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(Fore.CYAN+"Monedas minimas = "+n)
    
    if config.safegraphic:
        # Iterar por las filas del laberinto
        for i, fila in enumerate(laberinto):
            # Iterar por las columnas de cada fila
            for j, valor in enumerate(fila):
                # Si la casilla es la seleccionada, imprimir el emoticono
                if i == x and j == y:
                    print(Fore.GREEN+"██", end="")
                # Si no, imprimir el valor de la casilla
                elif valor==0:
                    print(" " ,end=" ")
                elif valor==9:
                    print(Fore.LIGHTRED_EX+"██",end="") 
                elif valor==8:
                    print(Fore.CYAN+"O ",end="") 
                elif valor==7:
                    print(Fore.YELLOW+"██",end="") 
                else :
                    print(Fore.RESET+str(valor)+" ",end="") 
            # Imprimir un salto de línea al final de cada fila
            print()

    
    else:
        # Iterar por las filas del laberinto
        for i, fila in enumerate(laberinto):
            # Iterar por las columnas de cada fila
            for j, valor in enumerate(fila):
                # Si la casilla es la seleccionada, imprimir el emoticono
                if i == x and j == y:
                    print("🆒", end="")
                # Si no, imprimir el valor de la casilla
                elif valor==0:
                    print(" " ,end=" ")
                elif valor==9:
                    print("🟫",end="") 
                elif valor==8:
                    print("🤖",end="") 
                elif valor==7:
                    print("🚩",end="") 
                else :
                    print(" "+str(valor),end="") 
            # Imprimir un salto de línea al final de cada fila
            print()
    print(Fore.RESET+"\n           W")
    print("  Pulse A  S  D  para moverse por el laberinto")
    print(Fore.MAGENTA+"  Pulse un número del 1 al 6. Para accionar")
    print("  Pulse ESC Para guardar"+Fore.RESET)
    print("                                                               Proyecto realizado por Pablo Natera Muñoz")
    print("                                                                                      Alejandro Barrena Millán")
    print("                                                                                      Raúl Martín-Romo Sánchez")
     
def crear(laberinto, n):
    # Obtener el tamaño del laberinto
    filas, columnas = len(laberinto), len(laberinto[0])

    # Definir la posición inicial del usuario
    x, y = 0, 0

    # Bucle principal
    while True:
        # Mostrar el estado actual del laberinto
        pintar_estado(laberinto, x, y, n)

        # Esperar a que el usuario ingrese una tecla
        key = ms.getch()

        # Si el usuario presiona "esc", salir del bucle
        if key == b'\x1b':
            break

        # Si el usuario ingresa una tecla de movimiento
        elif key in [b'w', b'a', b's', b'd']:
            # Actualizar la posición del usuario según la tecla presionada
            if key == b'w' and x > 0:
                x -= 1
            elif key == b'a' and y > 0:
                y -= 1
            elif key == b's' and x < filas - 1:
                x += 1
            elif key == b'd' and y < columnas - 1:
                y += 1

        # Si el usuario ingresa un número del 0 al 9
        elif key.isdigit() and 0 <= int(key) <= 9:
            # Convertir el carácter a un número entero
            numero = int(key)

            # Actualizar el valor de la casilla actual con el número ingresado
            laberinto[x][y] = numero

    # Si se presiona "esc", salir de la función
    return

def guardarLab(laberinto, n):
    # Crear la carpeta Laberintos si no existe
    if not os.path.exists('Laberintos'):
        os.makedirs('Laberintos')
    num=input(Fore.YELLOW+"Elige el numero: "+Fore.RESET)
    # Abrir un archivo llamado laberinto.txt en modo escritura
    with open('Laberintos/LABECOIN'+num+'.txt', 'w') as archivo:
        # Escribir el valor de n en la primera línea del archivo
        archivo.write(str(n) + '\n')
        # Iterar por las filas del laberinto
        for fila in laberinto:
            # Convertir la fila a una cadena de caracteres separados por comas
            fila_str = ','.join(map(str, fila))
            # Escribir la fila en el archivo seguida de un salto de línea
            archivo.write(fila_str + '\n')

def espejo2_matriz(in_num, out_num):
    with open(f"Laberintos/LABECOIN{in_num}.txt", "r") as fichero:
        # Leer la primera línea del archivo, convertirla a entero y almacenarlo en la variable "n"
        movs = int(fichero.readline().strip())
        # Inicializar una matriz vacía "laberinto"
        matriz = []
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
                matriz.append(linea)
        #Cierre del fichero
        fichero.close()
    IASI.printLaberinto(matriz)

    print(Fore.CYAN+downrrow+Fore.RESET)
    # Obtener la matriz volteada
    matriz_volteada = [fila[::-1] for fila in matriz]
    IASI.printLaberinto(matriz_volteada)

    with open(f"Laberintos/LABECOIN{out_num}.txt", "w") as f:
        # Escribir el número inicial y la matriz volteada en el archivo de salida
        f.write(str(movs) + "\n")
        for fila in matriz_volteada:
            f.write(",".join(str(x) for x in fila) + "\n")
            
def espejo_matriz(in_num, out_num):
    with open(f"Laberintos/LABECOIN{in_num}.txt", "r") as fichero:
        # Leer la primera línea del archivo, convertirla a entero y almacenarlo en la variable "n"
        movs = int(fichero.readline().strip())
        # Inicializar una matriz vacía "laberinto"
        matriz = []
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
                matriz.append(linea)
        #Cierre del fichero
        fichero.close()
    IASI.printLaberinto(matriz)

    print(Fore.CYAN+downrrow+Fore.RESET)
    # Obtener la matriz espejo
    matriz_espejo = [list(reversed(fila)) for fila in matriz[::-1]]
    IASI.printLaberinto(matriz_espejo)

    with open(f"Laberintos/LABECOIN{out_num}.txt", "w") as f:
        # Escribir el número inicial y la matriz espejo en el archivo de salida
        f.write(str(movs) + "\n")
        for fila in matriz_espejo:
            f.write(",".join(str(x) for x in fila) + "\n")


def voltear_matriz(in_num, out_num):
    with open(f"Laberintos/LABECOIN{in_num}.txt", "r") as fichero:
        # Leer la primera línea del archivo, convertirla a entero y almacenarlo en la variable "n"
        movs = int(fichero.readline().strip())
        # Inicializar una matriz vacía "laberinto"
        matriz = []
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
                matriz.append(linea)
        #Cierre del fichero
        fichero.close()
    IASI.printLaberinto(matriz)

    print(Fore.CYAN+downrrow+Fore.RESET)
    n = len(matriz)
    matriz_volteada = [[matriz[i][j] for i in range(n-1, -1, -1)] for j in range(n)]
    
    IASI.printLaberinto(matriz_volteada)

    with open(f"Laberintos/LABECOIN{out_num}.txt", "w") as f:
        # Escribir el número inicial y la matriz volteada en el archivo de salida
        f.write(str(movs) + "\n")
        for fila in matriz_volteada:
            f.write(",".join(str(x) for x in fila) + "\n")

def menu(op):
    if op==0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.RED + logoM + Fore.RESET)
        print(Fore.CYAN+"-> "+Fore.YELLOW+"Generar Laberinto")
        print(Fore.GREEN+"   Voltear matriz hacia la derecha")
        print(Fore.GREEN+"   Modo espejo")
        print(Fore.GREEN+"   Volteo + espejo")
    elif op==1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.RED + logoM + Fore.RESET)
        print(Fore.GREEN+"   Generar Laberinto")
        print(Fore.CYAN+"-> "+Fore.YELLOW+"Voltear matriz hacia la derecha")
        print(Fore.GREEN+"   Modo espejo")
        print(Fore.GREEN+"   Volteo + espejo")
    elif op==2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.RED + logoM + Fore.RESET)
        print(Fore.GREEN+"   Generar Laberinto")
        print(Fore.GREEN+"   Voltear matriz hacia la derecha")
        print(Fore.CYAN+"-> "+Fore.YELLOW+"Modo espejo")
        print(Fore.GREEN+"   Volteo + espejo")
    elif op==3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.RED + logoM + Fore.RESET)
        print(Fore.GREEN+"   Generar Laberinto")
        print(Fore.GREEN+"   Voltear matriz hacia la derecha")
        print(Fore.GREEN+"   Modo espejo")
        print(Fore.CYAN+"-> "+Fore.YELLOW+"Volteo + espejo")
    
    print(Fore.RESET+"\n                      ⬆")
    print("             Pulse ⬅  ⬇ ➡  para moverse por el menú")
    print("             Pulse ENTER. Para accionar")
    print("                                                               Proyecto realizado por       Pablo Natera Muñoz")
    print("                                                                                      Alejandro Barrena Millán")
    print("                                                                                      Raúl Martín-Romo Sánchez")

def MazeMaker():
    op=0
    key='a'
    menu(op)
    while((key != b'\r') and key != b'\x1b'):
        if(key==b'\xe0'):
            key= ms.getch()
            if(key==b'P'):
                if(op<3):
                    op+=1
                else:
                    op=0
            if(key==b'H'):
                if(op>0):
                    op-=1
                else:
                    op=3
        menu(op)
        key= ms.getch()
    if(key == b'\r'):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.RED + logoM + Fore.YELLOW)
        if op == 1:
            n=input("Elige laberinto de entrada ")
            n2=input("Elige laberinto de salida ")
            voltear_matriz(n,n2)
        # Si el usuario presiona "2", poner la matriz en modo espejo
        elif op == 3:
            n=input("Elige laberinto de entrada ")
            n2=input("Elige laberinto de salida ")
            espejo_matriz(n,n2)
        # Si el usuario presiona "3", generar un laberinto
        elif op == 0:
            n=input("Elige el número de monedas minimas: ")
            laberinto = [[9 if i == 0 or i == 9 or j == 0 or j == 9 else 0 for j in range(10)] for i in range(10)]
            print("Monedas minimas = "+ n+"\n")
            crear(laberinto, n)
            guardarLab(laberinto, n)
        # Si el usuario presiona otra tecla, volver al menú
        elif  op == 2:
            n=input("Elige laberinto de entrada ")
            n2=input("Elige laberinto de salida ")
            espejo2_matriz(n,n2)
        else:
            MazeMaker() 
