# Importar librería "pygame"
import pygame

class Character:
    def __init__(self, x, y):
        self.posX = x # Posición inicial del personaje en el eje X
        self.posY = y # Posición inicial del personaje en el eje Y
        # Tamaño del personaje (en píxeles)
        self.width = 55
        self.height = 55
        self.speed = 10 # velocidad a la que se va a mover el personaje
        self.color = '#c500ff' # color del personaje
        # Indicar posición inicial y tamaño del personaje con la info anterior
        self.rect = pygame.Rect(self.posX, self.posY, self.width, self.height)

# Función para dibujar el personaje en el juego
def draw_character(self, window):
    # Obtener el tamaño especificado y las posiciones especificadas en la clase anterior
    self.rect = pygame.Rect(self.posX, self.posY, self.width, self.height)
    # Dibujar personaje en la ventana del juego con el color y el tamaño especificado
    # Dibujarlo en la posición inicial establecida en la clase anterior
    pygame.draw.rect(window, self.color, self.rect)