"""
Main game module.
"""
import pygame

from jazzpy.config.config import GAME_ROOT
from jazzpy.config.config import SCREEN_HEIGHT
from jazzpy.config.config import SCREEN_WIDTH
from jazzpy.levels.diamondus.diamondus_level_one import DiamondusLevelOne
from jazzpy.scenes.play_scene import PlayScene


def play():
    """
    Main function to start the game loop.
    """
    # initializes all pygame modules
    pygame.init()
    pygame.mixer.init()  # iniits mixer module for sound

    # gets game variables
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(
        "Jazz Jackrabbit Remake of Epic MegaGames (1994)"
    )
    clock = pygame.time.Clock()
    is_game_running = True

    # creates a play_scene at the level one
    diamondus_level_one = DiamondusLevelOne(
        GAME_ROOT + "/sprites/levels/diamondus/diamondus.png",
        GAME_ROOT + "/levels/diamondus/diamondus_level_one.txt",
        GAME_ROOT + "/music/levels/diamondus/marbelara.mp3",
        platforms_width=60,
        platforms_height=60,
    )

    play_scene = PlayScene(diamondus_level_one)

    # main game loop
    while is_game_running:
        # clears screen
        screen.fill((0, 0, 0))

        clock.tick(60)  # max of 60 fps

        if pygame.event.get(pygame.QUIT):
            is_game_running = False

            return

        # each scene handles the events of the queue
        play_scene.handle_events(pygame.event.get())

        # updates elements of the scene
        play_scene.update()

        # renders on the screen the updated scene
        play_scene.render_on(screen)

        # updates the whole display
        pygame.display.flip()


if __name__ == "__main__":
    play()  # starts the game loop
