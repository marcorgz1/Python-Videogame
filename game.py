# Importar la librería "pygame"
import pygame
# Importar librería "random"
import random
# Importar la clase "Character" del fichero "Character.py"
from Character import Character  

pygame.init()

# Definir ancho y alto que va a tener la ventana del juego
width = 1200
height = 800
# Crear la ventana
# Indicar que va a tener el ancho y el alto que hemos indicado anteriormente
window = pygame.display.set_mode([width, height])
# Indicar a cuantos fotogramas por segundo va a ir el juego
fps = 60
# Indicar la fuente y el tamaño de la letra que se va a usar en el juego para mostrar la puntuación o 
# el número de vidas
gameFont = pygame.font.SysFont('Cascadia Code', 40)
# Guardar el tiempo que se lleva jugando la partida
time_playing = 0
# Guardar el margen de tiempo que existe entre la aparición de 
# un nuevo enemigo (500 milisegundos)
time_new_enemy = 500

# Crear personaje en la posición especificada de la clase "Character"
character = Character(width / 2, height - 75)

# Crear reloj para saber cuanto tiempo llevamos jugando
clock = pygame.time.Clock()

# Indicar el número de vidas que vamos a tener al iniciar el juego
lifes = 5
# Indicar el número de puntos que vamos a tener al iniciar el juego
points = 0

# Crear array para almacenar el número total de enemigos que han aparecido
# durante la partida
enemies = []

# Varaible que indica si se el usuario está jugando actualmente, se incializa en "true" ya que por defecto
# si está jugando
playing = True

# Función que se encarga de controlar las teclas presionadas por el usuario
# y del movimiento del cubo
def cube_movement(keys):
    # Si el usuario presiona la tecla "A"
    if keys[pygame.K_a]:
        # Mover el personaje a la izquierda
        # Decrementar el valor del personaje en el eje X para hacer el efecto 
        # de que se mueve a la izquierda
        character.posX -= character.speed
    
    # Si el usuario presiona la tecla "A"
    if keys[pygame.K_d]:
        # Mover el personaje a la izquierda
        # Incrementar el valor del personaje en el eje X para hacer el efecto 
        # de que se mueve a la derecha
        character.posX += character.speed
    
    # Si el usuario presiona la tecla "W"
    if keys[pygame.K_w]:
        # Mover el personaje a la izquierda
        # Incrementar el valor del personaje en el eje X para hacer el efecto 
        # de que se mueve a la derecha
        character.posX += character.speed

# Bucle para impedir que el juego se cierre al correrlo
# Mientras que "playing" no cambie, es decir, sea "True" y "lifes" sea mayor a 0, 
# es decir, existan vidas
while playing and lifes > 0:
    # Incrementar el tiempo lleva jugando el usuario dependiendo de cada frame que se aumente,
    # ya que si el frame aumenta, significa que la partida no ha terminado
    time_playing += clock.tick(fps)

    # Saber si ya han pasado 500 milisegundos en el tiempo que se lleva jugando la partida
    if time_playing > time_new_enemy:
        # Añadir nuevo enemigo a la partida
        # random.randint(0, width), -100: Crear nuevo enemigo en una posición aleatoria
        # del eje horizontal del juego
        enemies.append(random.randint(0, width), -100)
        # Una vez el enemigo ha aparecido en el juego, reiniciar el contador de tiempo jugado
        time_playing = 0

        # Captura eventos del juego
        events = pygame.event.get()
        # Captura eventos de teclas del juego
        key_events = pygame.key.get_pressed()
