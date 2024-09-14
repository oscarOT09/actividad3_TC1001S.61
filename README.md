# Documentación del Juego de Pacman

Este código implementa un sencillo juego de Pacman utilizando la biblioteca `turtle` y `freegames` en Python. El objetivo del juego es mover a Pacman para recolectar puntos blancos mientras se evitan los fantasmas.

## Descripción del Juego

- **Pacman**: Se controla con las flechas del teclado.
- **Fantasmas**: Se mueven de manera automática y cambian de dirección si se encuentran con una pared.
- **Objetivo**: Recolectar todos los puntos blancos en el mapa mientras se evitan los fantasmas.

## Estructura del Código

### Importación de Módulos

```python
from random import choice
from turtle import *
from freegames import floor, vector
```

- **`random.choice`**: Se usa para elegir una dirección aleatoria para los fantasmas.
- **`turtle`**: Biblioteca para los gráficos del juego.
- **`freegames.vector`**: Se usa para manejar posiciones y direcciones de Pacman y los fantasmas.

### Variables Globales

- **`state`**: Diccionario que mantiene el puntaje del jugador.
- **`path`**: Tortuga invisible utilizada para dibujar el mapa.
- **`writer`**: Tortuga invisible utilizada para escribir el puntaje en la pantalla.
- **`aim`**: Dirección de Pacman.
- **`pacman`**: Posición de Pacman.
- **`ghosts`**: Lista de fantasmas, cada uno con una posición y una dirección.
- **`tiles`**: Lista que representa el mapa del mundo, donde `0` es un muro y `1` es un camino.

### Funciones

#### `square(x, y)`

```python
def square(x, y):
    """
    Dibuja un cuadrado en la posición (x, y) usando la tortuga `path`.
    """
```
- **Descripción**: Dibuja un cuadrado en la posición `(x, y)` para representar las paredes y los caminos del mapa.

#### `offset(point)`

```python
def offset(point):
    """
    Devuelve el índice del punto en la lista de baldosas.
    """
```
- **Descripción**: Calcula la posición en el mapa para un punto determinado y devuelve su índice en la lista de baldosas.

#### `valid(point)`

```python
def valid(point):
    """
    Verifica si el punto dado es válido (transitable).
    """
```
- **Descripción**: Comprueba si el punto está en una posición válida del mapa, es decir, si no es un muro.

#### `world()`

```python
def world():
    """
    Dibuja el mundo en la pantalla basándose en la lista de baldosas.
    """
```
- **Descripción**: Dibuja el mapa del mundo en la pantalla, donde las paredes son verdes y los caminos tienen pequeños puntos blancos.

#### `move()`

```python
def move():
    """
    Mueve a Pacman y los fantasmas. También actualiza el marcador y verifica colisiones.
    """
```
- **Descripción**: Mueve a Pacman y a los fantasmas. También actualiza el puntaje y verifica si Pacman colisiona con un fantasma.

#### `change(x, y)`

```python
def change(x, y):
    """
    Cambia la dirección de Pacman si la nueva dirección es válida.
    """
```
- **Descripción**: Cambia la dirección de Pacman según las teclas presionadas por el jugador, pero solo si la dirección es válida.

### Configuración Inicial

```python
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()
```

- **Pantalla**: Configura la ventana del juego con un tamaño de 420x420.
- **Ocultar la tortuga**: Se oculta el cursor de la tortuga.
- **Escribir puntaje**: Se muestra el puntaje inicial en la esquina superior derecha.
- **Asignación de teclas**: Las flechas del teclado controlan el movimiento de Pacman.

### Asignación de Teclas

```python
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
```

- **Movimiento**: Se asignan las teclas de flecha para cambiar la dirección de Pacman.

### Iniciar el Juego

```python
world()
move()
done()
```

- **`world()`**: Dibuja el mapa del juego.
- **`move()`**: Comienza el movimiento de Pacman y los fantasmas.
- **`done()`**: Mantiene la ventana abierta hasta que el jugador la cierre.

---

¡Disfruta del juego mientras evitas a los fantasmas y recolectas todos los puntos!
