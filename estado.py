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
    
    def __init__(self, x, y, coin, tablero, movimientoRealizado, totalMovs, estadoPadre):              
        self.x = x                                  
        self.y = y                                  
        self.coin = coin               
        self.tablero = tablero
        self.movimientoRealizado = movimientoRealizado
        self.totalMovs = totalMovs
        self.estadoPadre = estadoPadre
    
    def getposicion(self):
        return(self.x, self.y)
    
    def getestado(self):
        return (self.tablero, self.x, self.y, self.coin, self.movimientoRealizado)
    
    def getHeuristica(self, totalMonedas, metax, metay):
        meta=[metax, metay]
        robot=[self.x, self.y]
        if(totalMonedas<=self.coin):
            return math.dist(meta, robot)+self.totalMovs
        else:
            return ((totalMonedas-self.coin)/2+math.dist(meta, robot)/2+math.dist(self.getMonedaCercana(),robot)/3)+self.totalMovs
        
    def getMonedaCercana(self):
        fila=0
        robot=[self.x, self.y]
        mejorMoneda=[-1,-1]
        actualMoneda=[-1,-1]
        mejorValor=0
        actualValor=0
        for linea in self.tablero:
            columna=0
            for valor in linea: 
                actualMoneda=[fila,columna]
                actualValor=valor/3-math.dist(robot, actualMoneda)
                if  1 <= valor <= 6 and mejorValor<actualValor:
                    mejorValor=actualValor
                    mejorMoneda=actualMoneda
                columna=columna+1            
            fila=fila+1 
        return mejorMoneda
        