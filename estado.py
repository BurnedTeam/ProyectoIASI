# estado.py
# Clase estado donde esta el estado del tablero, el movimiento que hemos hecho para llegar en el 
# estado anterior a este y las monedas que lleva el robot
class Estado:
    coin=0
    x=0
    y=0
    tablero=[None][None]
    movimientoRealizado=''
    
    def __init__(self, x, y, coin, tablero, movimientoRealizado):              
        self.x = x                                  
        self.y = y                                  
        self.coin = coin               
        self.tablero = tablero
        self.movimientoRealizado = movimientoRealizado
        
    def getestado(self):
        return (self.tablero, self.x, self.y, self.coin, self.movimientoRealizado)
