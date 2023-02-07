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