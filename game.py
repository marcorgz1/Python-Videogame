import pygame

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

# Crear reloj para saber cuanto tiempo llevamos jugando
clock = pygame.time.Clock()

# Indicar el número de vidas que vamos a tener al iniciar el juego
vidas = 5
# Indicar el número de puntos que vamos a tener al iniciar el juego
puntos = 0