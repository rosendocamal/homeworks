import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    # Iniciando el juego, las configuraciones y el objeto de pantalla
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
            (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Crea el botón de Iniciar juego.
    play_button = Button(ai_settings, screen, "Jugar")
    # Crea la instancia de las estadísticas del juego y crea el tablero.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    # Crear la nave
    ship = Ship(ai_settings, screen)
    # Crea un grupo de balas
    bullets = Group()
    # Crea un grupo de aliens
    aliens = Group()

    # Crear la flota de aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Reproducción de la música de fondo.
    try:
        pygame.mixer.init()
        pygame.mixer.music.load('audio/background.mp3')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
    except:
        print('ayuda')

    # Empezando el bucle principal del juego.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()
