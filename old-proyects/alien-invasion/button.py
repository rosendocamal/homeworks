import pygame.font

class Button():

    def __init__(self, ai_settings, screen, msg):
        """Inicializador de los atributos del botón."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Conjunto de las dimensiones y propiedades del botón.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Hacer el objeto de la recta del botón y centrarlo.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Mensaje del botón que se necesita una vez.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Muestra el mensaje y renderiz la imagen, centrando el texto en el botón."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Dibuja el botón blanco y luego dibuja el mensaje.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
