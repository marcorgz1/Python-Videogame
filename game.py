# Importar la librería "pygame"
import pygame
# Importar librería "random"
import random
# Importar la clase "Character" del fichero "Character.py"
from Character import Character  
from Enemy import Enemy

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

# Añadir enemigo al array "enemies" cuando ya ha bajado totalmente
enemies.append(Enemy(width / 2, 100))

# Varaible que indica si se el usuario está jugando actualmente, se incializa en "true" ya que por defecto
# si está jugando
playing = True

# Función que se encarga de controlar las teclas presionadas por el usuario
# y del movimiento del cubo
def handle_movement(keys):
    # Si el usuario presiona la tecla "W"
    if keys[pygame.K_w]:
        # Mover el personaje a la izquierda
        # Incrementar el valor del personaje en el eje Y para hacer el efecto 
        # de que se mueve hacia arriba
        character.posY -= character.speed

    # Si el usuario presiona la tecla "W"
    if keys[pygame.K_s]:
        # Mover el personaje a la izquierda
        # Decrementar el valor del personaje en el eje Y para hacer el efecto 
        # de que se mueve hacia abajo
        character.posY += character.speed

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

# Bucle para impedir que el juego se cierre al correrlo
# Mientras que "playing" no cambie, es decir, sea "True" y "lifes" sea mayor a 0, 
# es decir, existan vidas
while playing and lifes > 0:
    # Incrementar el tiempo lleva jugando el usuario dependiendo de cada frame que se aumente,
    # ya que si el frame aumenta, significa que la partida no ha terminado
    time_playing += clock.tick(fps)

    # Saber si ya han pasado 500 milisegundos en el tiempo que se lleva jugando la partida
    if time_playing > time_new_enemy:
        # Añadir nuevo enemigo en una posición aleatoria de la ventana a la partida
        # Enemy(random.randint(0, width), -100): Crear nuevo enemigo en una posición entre 0 y el ancho total 
        # de la ventana (0, width) y en la parte superior de esta (-100)
        enemies.append(Enemy(random.randint(0, width), -100))
        # Una vez el enemigo ha aparecido en el juego, reiniciar el contador de tiempo jugado
        time_playing = 0

        # Obtener todos los eventos necesarios del juego
        events = pygame.event.get()
        # Captura eventos de teclas del juego
        key_events = pygame.key.get_pressed()

        # Dibujar texto con los puntos y el número de vidas que tiene el usuario
        # En render ecibe tres parámetros: el texto a mostrar, si utiliza 
        # antialiasing (permite mostrar los bordes de las letras más suaves y nitidos) y el color del mismo
        show_lifes = gameFont.render(f"Nº Vidas: {lifes}", True, "white")
        show_points = gameFont.render(f"Nº Puntos: {points}", True, "white")

        # Llamar a la función encargada del movimiento y de las teclas que presiona 
        # el usuario en el juego para poder mover 
        # el personaje (se le pasa la variable "key_events" para saber qué teclas está presionando el usuario)
        handle_movement(key_events)

        # Recorrer cada uno de los eventos guardados en la variable "events"
        for event in events:
            # Si el evento que se está recorriendo es el de "QUIT", es decir, 
            # el usuario quiere cerrar la ventana
            if event.type == pygame.QUIT:
                # Cambiar el valor de la variable "playing" a "False" para indicar 
                # que el usuario ha dejado de jugar y se cierre la ventana del juego
                playing = False

        # Establecer color de fondo de la ventana en negro
        window.fill('black')
        # Dibujar el personaje en la ventana del juego llamando a la función "draw_character" 
        # de la clase "Character"
        character.draw_character(window)

        # Bucle que permite mostrar los enemigos en la ventana del juego

        # Recorrer cada uno de los enemigos del array enemigos
        for enemy in enemies:
            # Mostrar enemigo en la ventana del juego
            # LLamar a la función "draw_enemy" de la clase "Enemy" que es la que se engarga de 
            # dibujar al enemigo en la ventana del juego
            enemy.draw_enemy(window)
            # Hacer que el enemigo se vaya moviendo hacia abajo

            enemy.enemy_movement()

        # TODO: Cuando el personaje toque a un enemigo, que se le reste una vida y 
        # TODO: se elimine el enemigo ya tocado

        # Mostrar texto de vidas y puntos en la ventana del juego
        # El método "blit()" recibe dos parámetros: el texto a mostrar y en la posición 
        # en la que se va a mostrar
        window.blit(show_lifes, (20, 50))
        window.blit(show_points, (18, 100))

        # Actualizar la ventana del juego cada vez que exista un nuevo cambio en este
        pygame.display.update()

# Cuando se salga del bucle, terminará el juego
quit()
