class GameStats():
    """Trazado de las estadísticas de «Alien Invasion»."""

    def __init__(self, ai_settings):
        """Inicializador de estadísticas."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Iniciar el juego en estado inactivo.
        self.game_active = False

        # Puntuación alta, se reinicia.
        self.high_score = self.load_high_score()

    def reset_stats(self):
        """Inicia las estadísticas durante la partida y las actualiza."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def load_high_score(self):
        """Carga la puntuación más alta desde un archivo de texto."""
        try:
            with open('score/highscore.txt', 'r') as file:
                return int(file.read().strip())
        except (FileNotFoundError, ValueError):
            return 0

    def save_high_score(self):
        """Guarda el récord acutal en un archivo de texto."""
        with open('score/highscore.txt', 'w') as file:
            file.write(str(self.high_score))
