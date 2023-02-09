# ENUNCIADO DE LA PRÁCTICA DE LA ASIGNATURA DE INTELIGENCIA ARTIFICIAL Y SISTEMAS INTELIGENTES 2022/2023
## Fecha límite de entrega:
18 de abril versión 1.1 (27 enero 2023)

## LABECOIN
Se pide diseñar e implementar un sistema relacionado con los movimientos y acciones de un robot que busque un camino para salir de un laberinto.

## Parámetros de entrada
- Se proporciona un laberinto en un tablero de 10 x 10, que se da como parámetro de entrada.
- Se proporciona un mínimo valor de monedas (precio de salida) que se deben conseguir en el camino.
## Salida de la aplicación
- Deben mostrarse los movimientos del robot hasta la salida.
## Tablero de entrada
- El tablero de entrada podrá ser diferente en cada caso, aunque el tamaño es siempre de 10 x 10.
- Las celdas tienen un valor asignado que se corresponden con:
0 – CELDA VACÍA
9 – MURO
8 – ROBOT
7 – SALIDA
1-6 – MONEDAS
## Movimiento del robot
- El movimiento del robot puede ser Arriba, Abajo, Derecha, Izquierda, y las diagonales (AI, AD, BD, BI).
- No se podrá mover a una casilla que haya un muro.
- Cuando se mueva a una casilla con monedas, debe sumarse esa cantidad al acumulado de monedas (cartera) del camino. Sólo se suma una vez la moneda al pasar por esa casilla.
## Técnicas de búsqueda
- Se deben utilizar técnicas de búsquedas de forma que proporcione una solución, consistente en indicar la secuencia de acciones (movimientos) del robot.
- Esta solución debe cumplir que, al llegar a la salida, el acumulado de monedas (cartera) debe ser igual o superior al precio indicado.
- Se parte desde el supuesto de que se dispone de muy poco tiempo para encontrar la solución, por lo que interesa utilizar búsquedas con heurísticas, y se quiere encontrar una solución que no tenga muchos movimientos.
## Condiciones
- Siempre debe buscarse una solución para que supere la condición de que cartera ≥ precio.
## Ejemplo

### Fichero tablero 1:
~~~
12
9,9,9,9,9,9,9,9,9,9,
9,2,9,0,6,0,0,0,0,9,
9,0,9,0,0,9,9,9,9,9,
9,1,0,8,9,0,9,0,0,9,
9,0,9,9,9,0,0,4,0,9,
9,0,0,0,0,0,9,9,9,9,
9,1,9,0,0,0,0,0,1,9,
9,1,9,9,9,0,9,9,9,9,
9,1,6,6,9,0,0,0,3,9,
9,9,9,9,9,9,7,9,9,9,
~~~
### Salida:

~~~
AD, A, BI, BI, BI, B, B, B, BD, AI, A, AD, BD, D, BD, BD, B

↗ ⬆ ↙ ↙ ↙ ⬇ ⬇ ⬇ ↘ ↖ ⬆ ↗ ↘ ➡ ↘ ↘ ⬇
~~~
