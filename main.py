from colorama import Style, init, Fore
import os
import MazeEscaladaSimple as MES
import MazeAEstrella as AE
import MazeMaximaPendiente as MP
import MazeMaker as MM
import MazePlayer as MPy
import msvcrt as ms
import config


# Definir el ASCII art del logo
logo = """
██████╗ ██╗   ██╗██████╗ ███╗   ██╗███████╗██████╗     ███████╗ ██████╗ ██╗    ██╗   ██╗███████╗██████╗ 
██╔══██╗██║   ██║██╔══██╗████╗  ██║██╔════╝██╔══██╗    ██╔════╝██╔═══██╗██║    ██║   ██║██╔════╝██╔══██╗
██████╔╝██║   ██║██████╔╝██╔██╗ ██║█████╗  ██║  ██║    ███████╗██║   ██║██║    ██║   ██║█████╗  ██████╔╝
██╔══██╗██║   ██║██╔══██╗██║╚██╗██║██╔══╝  ██║  ██║    ╚════██║██║   ██║██║    ╚██╗ ██╔╝██╔══╝  ██╔══██╗
██████╔╝╚██████╔╝██║  ██║██║ ╚████║███████╗██████╔╝    ███████║╚██████╔╝███████╗╚████╔╝ ███████╗██║  ██║
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝ ╚═══╝  ╚══════╝╚═╝  ╚═╝
"""

def modoSel():
        if config.modo == 0:
            return "Resolucion por A*"
        elif config.modo == 1:
            return "Resolucion por Escalada Simple"
        elif config.modo == 2:
            return "Resolucion por Maxima Pendiente*"
        elif config.modo == 3:
            return "Jugar Laberintos"
        elif config.modo== 4:
            return "Crea tu propio laberinto"
def graficos():
        if config.safegraphic == 0:
            return "ULTRA"+Fore.RESET+" (Solo si puede ver esto 🟫 🤖 🚩 💲)"
        elif config.safegraphic==True:
            return "Modo Seguro"

def menu(op):
    if op==0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.RED + logo + Fore.RESET)
        print(Fore.CYAN+"-> "+Fore.YELLOW+"ENTRAR EN BURNED SOLVER")
        print(Fore.GREEN+"   Modo seleccionado: "+Fore.MAGENTA+modoSel())
        print(Fore.GREEN+"   Graficos: "+Fore.MAGENTA+graficos())
    elif op==1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.RED + logo + Fore.RESET)
        print(Fore.GREEN+"   ENTRAR EN BURNED SOLVER")
        print(Fore.CYAN+"-> "+Fore.YELLOW+"Modo seleccionado: "+Fore.MAGENTA+modoSel())
        print(Fore.GREEN+"   Graficos: "+Fore.MAGENTA+graficos())
    elif op==2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.RED + logo + Fore.RESET)
        print(Fore.GREEN+"   ENTRAR EN BURNED SOLVER")
        print(Fore.GREEN+"   Modo seleccionado: "+Fore.MAGENTA+modoSel())
        print(Fore.CYAN+"-> "+Fore.YELLOW+"Graficos: "+Fore.MAGENTA+graficos())
    
    print(Fore.RESET+"\n                      ⬆")
    print("             Pulse ⬅  ⬇ ➡  para moverse por el menú")
    print("             Pulse ENTER. Para accionar")
    print("                                                               Proyecto realizado por       Pablo Natera Muñoz")
    print("                                                                                      Alejandro Barrena Millán")
    print("                                                                                      Raúl Martín-Romo Sánchez")
    
def launchPy():
    if(config.modo==0):
        AE.AEstrella()
    elif(config.modo==1):
        MES.EscaladaSimple()
    elif(config.modo==2):
        MP.MaximaPendiente()
    elif(config.modo==3):
        MPy.MazePlayer()
    elif(config.modo==4):
        MM.MazeMaker()

def main():
    
    config.read_config()
    op=0
    key='a'
    menu(op)
    while((key != b'\r' or op!=0) and key != b'\x1b'):
        if(key==b'\xe0'):
            key= ms.getch()
            if(key==b'P'):
                if(op<2):
                    op+=1
                else:
                    op=0
            if(key==b'H'):
                if(op>0):
                    op-=1
                else:
                    op=2
            if(key==b'M'):
                if(op==1):
                    if(config.modo<4):
                        config.modo+=1
                    else:
                        config.modo=0
                    config.write_config()
                if(op==2):
                    config.safegraphic=not(config.safegraphic)
                    config.write_config()
            if(key==b'K'):
                if(op==1):
                    if(config.modo>0):
                        config.modo-=1
                    else:
                        config.modo=4
                    config.write_config()
                if(op==2):
                    config.safegraphic=not(config.safegraphic)
                    config.write_config()
        menu(op)
        key= ms.getch()
    if(key == b'\r'):
        launchPy()
        
    
    

    
if __name__ == '__main__':
    main()
