# Importar librería "pygame"
import pygame

class Enemy:
    def __init__(self, x, y):
        self.posX = x # Posición inicial del enemigo en el eje X
        self.posY = y # Posición inicial del enemigo en el eje Y
        # Tamaño del enemigo (en píxeles)
        self.width = 75
        self.height = 75
        self.speed = 10 # velocidad a la que se va a mover el enemigo
        self.color = 'red' # color del enemigo
        # Indicar posición inicial y tamaño del enemigo con la info anterior
        self.rect = pygame.Rect(self.posX, self.posY, self.width, self.height)

    # Función para dibujar el enemigo en el juego
    def draw_enemy(self, window):
        # Obtener el tamaño especificado y las posiciones especificadas en la clase anterior
        self.rect = pygame.Rect(self.posX, self.posY, self.width, self.height)
        # Dibujar enemigo en la ventana del juego con el color y el tamaño especificado
        # Dibujarlo en la posición inicial establecida en la clase anterior
        pygame.draw.rect(window, self.color, self.rect)

    # Función para mover al enemigo de arriba a abajo
    def enemy_movement(self):
        # Incrementar la posición en el eje Y en función de la velocidad para que el enemigo vaya hacia abajo
        # Ejemplo: Si la posición inicial del enemigo es 100, cuando vaya hacia abajo irá incrementando de 5
        # en 5, ya que la velocidad está establecida en 5, por lo que será 105, 110, 115...
        self.posY += self.speed