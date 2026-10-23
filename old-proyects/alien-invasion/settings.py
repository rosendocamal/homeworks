class Settings():
    """Clase de la configuración de «Alien Invasion»."""

    def __init__(self):
        """Iniciando la configuración estática del juego."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Configuración de la nave.
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # Configuración de la bala.
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Configuración del alien.
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10

        # Velocidad del juego
        self.speedup_scale = 1.1
        # Valor del incremento de la puntuación.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Iniciando las configuraciones mientras pasa el juego."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction de 1 representa derecha; -1 representa izquierda.
        self.fleet_direction = 1

        # Puntuación.
        self.alien_points = 50

    def increase_speed(self):
        """Incrementa la velocidad de las configuraciones y los puntos por alien disparado."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
