from random import choice
from turtle import *
from freegames import floor, vector

#Estado inicial del juego : marcador en 0
state = {'score': 0}

#Cracion deelementos invisibles para dibujar el camino y el puntaje
path = Turtle(visible=False)
writer = Turtle(visible=False)

#Direccion inicial de Pacman
aim = vector(5, 0)

#Posicion inicial de Pacman
pacman = vector(-40, -80)

#Lista de Fantasmas con sus posiciones iniciales y direcciones
ghosts = [
    [vector(-180, 160), vector(10, 0)],
    [vector(-180, -160), vector(0, 10)],
    [vector(100, 160), vector(0, -10)],
    [vector(100, -160), vector(-10, 0)],
]

#Mapa deñ mundo donde 0 es vacio y 1 camino
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0,
    0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0,
]

def square(x, y):
    """
    Dibuja un cuadrado en la posición (x, y) usando la tortuga `path`.
    """
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for _ in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()

def offset(point):
    """
    Devuelve el índice del punto en la lista de baldosas.
    Calcula la posición x e y basándose en el tamaño del mundo y las baldosas.
    """
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    return int(x + y * 20)

def valid(point):
    """
    Verifica si el punto dado es válido (es decir, si está dentro de las baldosas
    transitables). Devuelve True si es válido, False en caso contrario.
    """
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    # Solo es válido si el punto está alineado con la cuadrícula
    return point.x % 20 == 0 or point.y % 20 == 0

def world():
    """
    Dibuja el mundo basándose en la lista de baldosas. Las paredes son dibujadas
    en verde y las rutas transitables son representadas con puntos blancos.
    """
    bgcolor('black')  # Fondo negro
    path.color('green')  # Color del laberinto en verde

    for index, tile in enumerate(tiles):
        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')  # Puntos blancos que representan el camino

def move():
    """
    Mueve a Pacman y a todos los fantasmas. También actualiza el estado del
    marcador y verifica colisiones.
    """
    writer.undo()  # Borra el puntaje anterior
    writer.write(state['score'])  # Escribe el nuevo puntaje

    clear()

    # Mueve a Pacman si la nueva posición es válida
    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    # Verifica si Pacman ha comido un punto
    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')  # Dibuja a Pacman

    # Mueve a los fantasmas
    for point, course in ghosts:
        options = [
            vector(5, 0),
            vector(-5, 0),
            vector(0, 5),
            vector(0, -5),
        ]

        # Solo se permiten movimientos válidos
        valid_options = [option for option in options if valid(point + option)]

        # Encuentra la dirección más cercana a Pacman
        min_distance = float('inf')
        best_course = course
        for option in valid_options:
            distance = abs((point + option) - pacman)
            if distance < min_distance:
                min_distance = distance
                best_course = option

        point.move(best_course)

        # Si el fantasma se puede mover, lo hace; si no, elige una nueva dirección
        if valid(point + course):
            point.move(course)
        else:
            plan = choice(options)
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, 'red')  # Dibuja a los fantasmas

    update()

    # Verifica si Pacman colisionó con algún fantasma
    for point, _ in ghosts:
        if abs(pacman - point) < 20:
            return

    # Mueve los personajes nuevamente después de 70 milisegundos
    ontimer(move, 70)

def change(x, y):
    """
    Cambia la dirección de Pacman si la nueva dirección es válida.
    """
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

# Configura la pantalla y el juego
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])  # Muestra el puntaje inicial
listen()

# Asigna teclas para mover a Pacman
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')

world()
move()
done()