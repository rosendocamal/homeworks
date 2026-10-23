import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Clase que maneja las balas que dispara la nave"""

    def __init__(self, ai_settings, screen, ship):
        """Crea el objeto bala según la posición de la nave"""
        super().__init__()
        self.screen = screen

        # Crea una bala recta en (0,0) y luego en la posición correcta
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Obtener la posición decimal de la bala
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Movimiento de la bala arriba de la pantalla"""
        # Actualizar la posición decimal de la bala
        self.y -= self.speed_factor
        # Actualizar la posición de la recta
        self.rect.y = self.y

    def draw_bullet(self):
        """Dibujar la bala en la pantalla"""
        pygame.draw.rect(self.screen, self.color, self.rect)
