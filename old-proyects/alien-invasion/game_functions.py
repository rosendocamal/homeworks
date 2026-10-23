import sys
from time import sleep

import pygame
from bullet import Bullet
from alien import Alien

# Inicializador de los sonidos
pygame.mixer.init()

try:
    bullet_sound = pygame.mixer.Sound('audio/bullet.wav')
    boom_alien_sound = pygame.mixer.Sound('audio/boom_alien.wav')
    status_game_sound = pygame.mixer.Sound('audio/status_game.wav')
    boom_ship_sound = pygame.mixer.Sound('audio/boom_ship.wav')
    high_score_sound = pygame.mixer.Sound('audio/high_score.wav')
    level_sound = pygame.mixer.Sound('audio/level.wav')

    bullet_sound.set_volume(0.3)
    boom_alien_sound.set_volume(0.4)
    status_game_sound.set_volume(0.2)
    boom_ship_sound.set_volume(0.45)
    high_score_sound.set_volume(0.5)
    level_sound.set_volume(0.5)
except FileNotFoundError:
    bullet_sound, boom_alien_sound, status_game_sound = None, None, None
    boom_ship_sound, high_score_sound, level_sound = None, None, None

def check_keydown_events(event, ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Responde a la presión de teclas."""
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE or event.key == pygame.K_s:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        # Sonido de inicio/fin del juego.
        if status_game_sound:
            status_game_sound.play()
            sleep(0.2)
        sys.exit()
    elif event.key == pygame.K_p and not stats.game_active:
        # Sonido del inicio/fin del juego.
        if status_game_sound:
            status_game_sound.play()
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Limitación del fuego de las nuevas balas."""
    # Crear nuevas balas.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

    # Reproducción del sonido.
    if bullet_sound:
        bullet_sound.play()
        
def check_keyup_events(event, ship):
    """Responde a la actualización de teclas."""
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """Responde a los eventos del teclado y el mouse."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, stats, sb, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def start_game(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # Reinicia la configuración del juego.
    ai_settings.initialize_dynamic_settings()
    # Oculta el cursor del mouse.
    pygame.mouse.set_visible(False)
    # Reinicia las estadísticas del juego.
    stats.reset_stats()
    stats.game_active = True

    # Reinicia la imagen de la puntuación.
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()

    # Limpia la lista de aliens y balas.
    aliens.empty()
    bullets.empty()

    # Crea una nueva flota de aliens y centra la nave.
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()
    

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Inicia una nueva partida cuando se presiona Jugar."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        start_game(ai_settings, screen, stats, sb, ship, aliens, bullets)
        
        
def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """Actualizar imágenes en la pantalla."""
    # Redibuja la pantalla durante cada bucle.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)

    # Redibuja todas las balas.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Dibuja el tablero de la puntuación.
    sb.show_score()

    # Dibuja el botón de jugar cuando el juego está inactivo.
    if not stats.game_active:
        play_button.draw_button()

    # Muestra la pantalla más reciente.
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Actualizar posición de las balas y desaparecer las que deben desaparecer."""
    # Actualizar posición de las balas.
    bullets.update()

    # Balas desaparecidas.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Responde a las colisiones de las balas y los aliens."""
    # Revisa si alguna bala le ha dado a un alien.
    # Si esto sucede, elimina esa bala y ese alien en cuestión.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True) 

    if collisions:
        # Reproducción de las explosiones de aliens.
        if boom_alien_sound:
            boom_alien_sound.play()
        for alien in collisions.values():
            stats.score += ai_settings.alien_points * len(alien)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # Reproduce sonido de cambio de nivel.
        if level_sound:
            level_sound.play()
        # Destruye las balas existentes, cambia la velocidad del juego y crea una nueva flota de aliens, empieza un nuevo nivel.
        bullets.empty()
        ai_settings.increase_speed()

        # Aumenta nivel.
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)

def get_number_aliens_x(ai_settings, alien_width):
    """Determina el número de aliens que entran en una fila."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determina el número de filas de aliens que entran en la pantalla."""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Crea un alien y lo ubica en su lugar de la fila."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Crear toda la flota de aliens."""
    # Crear un alien y buscar el número máximo de aliens en la fila.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Crear la flota de aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
    """Responde apropiadamente a todas las naves cerca del borde."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Elimina toda la flota y cambia su dirección."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Responde a la colisión de la nave con el alien."""
    if stats.ships_left > 0:
        # Reproduce el sonido
        if boom_ship_sound:
            boom_ship_sound.play()

        # Decrece ships_left.
        stats.ships_left -= 1

        # Actualiza el tablero de puntuación.
        sb.prep_ships()

        # Vacía la lista de aliens y balas.
        aliens.empty()
        bullets.empty()

        # Crea una nueva flota y centra la nave.
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # Pausa
        sleep(1)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """Revisa si algún alien llegó a la parte de abajo de la pantalla."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break

def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    Inspecciona que si la flota está en el borde,
     y luego actualiza la posición de todos los aliens en el borde.
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Muestra si hubo alguna colisión entre la nave y un alien.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)

    # Muestra los aliens disparados en la parte de abajo de la pantalla.
    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_high_score(stats, sb):
    """Revisa si hay nueva puntuación."""
    if stats.score > stats.high_score:
        # Reproduce sonido para puntuación nueva
        if high_score_sound:
            high_score_sound.play()

        stats.high_score = stats.score
        sb.prep_high_score()

        # Guarda la puntuación más alta.
        stats.save_high_score()
