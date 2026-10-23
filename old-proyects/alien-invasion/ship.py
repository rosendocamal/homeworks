import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        super().__init__()
        """Iniciando la nave y su posición inicial."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Carga de la imagen.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Comenzar cada nave en el centro-abajo de la pantalla.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Valor decimal del centro de la nave.
        self.center = float(self.rect.centerx)

        # Movimiento de bandera.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Actualizar la posición de la nave basado en la bandera."""
        # Actualizar el valor del centro de la nave, no de la recta.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Actualizar el objeto de la recta de self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Dibujar la nave en la ubicación actual."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Centra la nave en la pantalla."""
        self.center = self.screen_rect.centerx
