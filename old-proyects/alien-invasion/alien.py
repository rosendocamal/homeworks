import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Clase que representa un solo alien."""

    def __init__(self, ai_settings, screen):
        """Inicia el alien y su posición inicial."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Carga la imagen del alien.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada alien en la parte arriba-izquierda de la pantalla.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Obtiene la posición exacta del alien.
        self.x = float(self.rect.x)

    def blitme(self):
        """Dibuja el alien en la ubicación actual."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Devuelve True si el alien está en el borde de la pantalla."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Mueve el alien a la derecha."""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
