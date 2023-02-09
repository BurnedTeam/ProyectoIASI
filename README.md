***Go to english version: [ENG](#english-section)***

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

___
---
# <p align="center">English Section</p>
***
___
   




# PRACTICE STATEMENT FOR THE SUBJECT OF ARTIFICIAL INTELLIGENCE AND INTELLIGENT SYSTEMS
## Deadline:
April 18th version 1.1 (January 27th 2023)

## LABECOIN
Design and implement a system related to the movements and actions of a robot searching for a path to exit a labyrinth.

## Input parameters
- A labyrinth on a 10 x 10 board is provided as an input parameter.
- A minimum coin value (exit price) that must be achieved along the way is provided.
## Application output
- The robot's movements to exit must be shown.
## Input board
- The input board may differ in each case, although the size is always 10 x 10.
- Cells have an assigned value that corresponds to:
0 – EMPTY CELL
9 – WALL
8 – ROBOT
7 – EXIT
1-6 – COINS
## Robot movement
- The robot's movement can be Up, Down, Right, Left, and diagonals (AI, AD, BD, BI).
- You cannot move to a cell with a wall.
- When you move to a cell with coins, the coin amount should be added to the coin accumulator (wallet) of the path. The coin is only added once when passing through that cell.
## Search techniques
- Search techniques must be used to provide a solution, consisting of indicating the sequence of actions (movements) of the robot.
- This solution must meet the requirement that, when reaching the exit, the coin accumulator (wallet) must be equal to or greater than the indicated price.
- It is assumed that there is very little time to find a solution, so it is desirable to use heuristic searches, and you want to find a solution that has few movements.
## Conditions
- A solution must always be sought that meets the condition of wallet ≥ price.
## Example

### File board 1:
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
### Output:

~~~
UR, U, DL, DL, DL, D, D, D, DR, UL, U, UR, DR, R, DR, DR, D

↗ ⬆ ↙ ↙ ↙ ⬇ ⬇ ⬇ ↘ ↖ ⬆ ↗ ↘ ➡ ↘ ↘ ⬇
~~~
