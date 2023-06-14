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
# Soluciones implementadas

Hemos utilizado tres algoritmos heurísticos para resolver el problema del laberinto y encontrar un camino para salir:

1. A*: Este algoritmo utiliza una función heurística para estimar el costo del camino desde el inicio hasta cada celda y selecciona la mejor opción en cada paso. Utiliza una combinación de la distancia euclidiana y el número de monedas recogidas como función heurística.

2. Escalada simple: Este algoritmo comienza desde una posición inicial y selecciona el vecino con el menor costo heurístico en cada paso. Si no hay un vecino con menor costo, se detiene. Utiliza la distancia euclidiana como función heurística.

3. Escalada máxima pendiente: Similar al algoritmo de escalada simple, pero en lugar de seleccionar el vecino con el menor costo heurístico, selecciona el vecino con el mayor aumento en el costo heurístico. Esto permite explorar caminos subóptimos en busca de mejores soluciones. Utiliza la distancia euclidiana como función heurística.

Además de los algoritmos heurísticos, también hemos implementado un modelo de redes neuronales utilizando Keras como método no heurístico. Este modelo aprende a través de los datos de entrenamiento creados por el metodo A* y permite proporcionar una solución basada en patrones identificados en el algoritmo A*.

En resumen, hemos utilizado A*, escalada simple y escalada máxima pendiente como soluciones heurísticas para encontrar un camino en el laberinto, considerando la acumulación de monedas requerida. También hemos explorado un enfoque no heurístico utilizando un modelo de redes neuronales implementado en Keras.

¡Estas soluciones nos permiten resolver el problema del laberinto y encontrar un camino óptimo hacia la salida!

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

# Implemented Solutions

We have used three heuristic algorithms to solve the maze problem and find a path to exit:

1. A*: This algorithm uses a heuristic function to estimate the cost of the path from the start to each cell and selects the best option at each step. It uses a combination of the Euclidean distance and the number of collected coins as the heuristic function.

2. Simple Hill Climbing: This algorithm starts from an initial position and selects the neighbor with the lowest heuristic cost at each step. If there is no neighbor with a lower cost, it stops. It uses the Euclidean distance as the heuristic function.

3. Maximum Slope Ascent: Similar to the Simple Hill Climbing algorithm, but instead of selecting the neighbor with the lowest heuristic cost, it selects the neighbor with the highest increase in heuristic cost. This allows exploring suboptimal paths in search of better solutions. It uses the Euclidean distance as the heuristic function.

In addition to the heuristic algorithms, we have also implemented a neural network model using Keras as a non-heuristic method. This model learns from the training data created by the A* algorithm and can provide a solution based on patterns identified in the A* algorithm.

In summary, we have used A*, Simple Hill Climbing, and Maximum Slope Ascent as heuristic solutions to find a path in the maze, considering the required accumulation of coins. We have also explored a non-heuristic approach using a neural network model implemented in Keras.

These solutions allow us to solve the maze problem and find an optimal path to the exit!

