"""
Main game module.
"""
import pygame

from config import SCREEN_HEIGHT, SCREEN_WIDTH
from scenes.play_scene import PlayScene


def main():
    """
    Main function to start the game loop.
    """
    # initializes all pygame modules
    pygame.init()

    # gets game variables
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    is_game_running = True
    play_scene = PlayScene()

    # main game loop
    while is_game_running:
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
    main()  # starts the game loop
