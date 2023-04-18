# estado.py
# Clase estado donde esta el estado del tablero, el movimiento que hemos hecho para llegar en el 
# estado anterior a este y las monedas que lleva el robot
import math 

class Estado:
    estadoPadre=None
    coin=0
    x=0
    y=0
    tablero = None
    movimientoRealizado=''
    totalMovs=0
    heuristica=0.00
    def __init__(self, x, y, coin, tablero, movimientoRealizado, totalMovs, estadoPadre,heuristica):              
        self.x = x                                  
        self.y = y                                  
        self.coin = coin               
        self.tablero = tablero
        self.movimientoRealizado = movimientoRealizado
        self.totalMovs = totalMovs
        self.estadoPadre = estadoPadre
        self.heuristica=heuristica

    def getposicion(self):
        return(self.x, self.y)
    
    def getestado(self):
        return (self.tablero, self.x, self.y, self.coin, self.movimientoRealizado)
    
    def setHeuristica(self,totalMonedas, metax, metay):
        self.heuristica=self.getHeuristica(totalMonedas, metax, metay)
        
    def getHeuristica(self, totalMonedas, metax, metay):
        meta=[metax, metay]
        robot=[self.x, self.y]
        if(totalMonedas<=self.coin):
            return float((math.dist(meta, robot)/2)+(self.totalMovs/2)-totalMonedas*2)
        else:
            return float(math.dist(self.getMonedaCercana(),robot)/2+(self.totalMovs)-(self.coin*2.5))
        
    def getMonedaCercana(self):
        fila = 0
        robot = [self.x, self.y]
        mejorMoneda = [-1, -1]
        mejorDistancia = float('inf')
        for linea in self.tablero:
            columna = 0
            for valor in linea:
                if 1 <= valor <= 6:
                    moneda = [fila, columna]
                    distancia = math.dist(robot, moneda)
                    if distancia < mejorDistancia:
                        mejorDistancia = distancia
                        mejorMoneda = moneda
                columna += 1
            fila += 1
        return mejorMoneda
    
    def __lt__(self, otro):
        if self.heuristica is None:
            raise ValueError("La heurística del estado no ha sido calculada")
        if otro.heuristica is None:
            raise ValueError("La heurística del otro estado no ha sido calculada")
        return self.heuristica < otro.heuristica

    def __eq__(self, other):
            if isinstance(other, Estado):
                # Verifica si el tablero y las coins son iguales en ambos estados
                return self.tablero == other.tablero and self.coin == other.coin
            return False