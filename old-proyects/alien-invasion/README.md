# Alien Invasion

Juego arcade 2D estilo _Space Invaders_ desarrollado con Python y Pygame. El jugador controla una nave espacial para eliminar oleadas de alienígenas mientras la dificultad aumenta progresivamente.

## Características

- Sistema de niveles con dificultad dinámica (velocidad y puntuación escalan por nivel).
- Sistema de audio completo con música de fondo y efectos de sonido.
- Puntuación persistente con high score guardado en archivo.
- Controles por teclado.
- Interfaz con HUD que muestra puntuación, nivel, vidas y high score.
- Botón «Jugar» para iniciar la partida.

## Controles

| Tecla | Acción |
|-------|--------|
| `←` / `A` | Mover nave a la izquierda |
| `→` / `D` | Mover nave a la derecha |
| `Espacio` / `S` | Disparar bala |
| `P` | Iniciar juego |
| `Q` | Salir del juego |
| **Ratón** | Clic en botón "Jugar" para iniciar |

## Requisitos previos

> [!IMPORTANT]
> Se requiere Python 3.x y la librería Pygame para ejecutar el juego.

- Python 3.x (desarrollado en Python 3.14.6)
- Pygame 2.6.1

## Instalación

1. Clona el repositorio:

```
git clone https://github.com/rosendocamal/alien-invasion.git
cd alien-invasion
```

2. Instala las dependencias:

```
pip install pygame
```

En algunos casos puede instalarse así:

```
sudo apt-get install python3-pygame
```

## Ejecución

```
python main.py
```

## Arquitectura del proyecto

El diagrama muestra cómo se relacionan los archivos, clases y funciones principales del proyecto.

```mermaid
graph TD
    main["main.py<br/>Punto de entrada"] --> settings["settings.py<br/>Configuración"]
    main --> game_functions["game_functions.py<br/>Lógica del juego"]
    main --> game_stats["game_stats.py<br/>Estadísticas"]
    main --> scoreboard["Scoreboard<br/>Interfaz HUD"]
    main --> ship["Ship<br/>Nave del jugador"]
    main --> alien["Alien<br/>Enemigos"]

    game_functions --> ship
    game_functions --> alien
    game_functions --> bullet["Bullet<br/>Proyectiles"]
    game_functions --> button["Button<br/>Botón Jugar"]
    game_functions --> settings

    game_stats --> scoreboard
    scoreboard --> settings

    ship --> settings
    alien --> settings
    bullet --> settings
```

## Flujo del juego

El siguiente diagrama de flujo muestra la dinámica del juego.

```mermaid
flowchart TD
    A[Inicio] --> B[Menú]
    B --> C{Jugador presiona Jugar}
    C -->|No| B
    C -->|Sí| D[Iniciar nivel 1]
    D --> E[Bucle del juego]
    E --> F{¿Hay colisión?}
    F -->|Bala-Alien| G[Eliminar alien + sumar puntos]
    F -->|Alien-Nave| H[Perder vida]
    F -->|No| I{¿Todos los aliens eliminados?}
    G --> I
    H --> J{¿Vidas restantes?}
    J -->|Sí| K[Esperar 1 segundo]
    J -->|No| L[Game Over]
    K --> E
    I -->|Sí| M[Siguiente nivel]
    I -->|No| E
    M --> N[Aumentar dificultad]
    N --> E
    L --> B
```

## Tecnologías utilizadas

| Tecnología | Versión | Propósito |
| -----------|---------|-----------|
|Python |	3.14.6 | Lenguaje de programación |
| Pygame | 2.6.1 | Framework de desarrollo de juegos 2D|
|BMP |	-|	Formato de sprites|
|WAV/MP3 |	-|	Formatos de audio|

>[!NOTE]
> No se requieren dependencias adicionales más allá de Pygame.

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Autor

Proyecto realizado por **Rosendo Camal**.

- GitHub: [rosendocamal](https://www.github.com/rosendocamal)
- LinkedIn: [rosendocamal](https://www.linkedin.com/in/rosendocamal)
