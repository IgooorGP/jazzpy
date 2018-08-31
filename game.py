"""
Main game module.
"""
import configparser
import sys

import pygame
from pygame.locals import *

from models.jazz.jazz import Jazz

# reads default configs
pygame.init()
config = configparser.RawConfigParser()
config.read("config.cfg")

WIDTH = config.getint("GAME_SCREEN", "WIDTH")
HEIGHT = config.getint("GAME_SCREEN", "HEIGHT")

# instantiates the first screen surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # pygame.surface.Surface
clock = pygame.time.Clock()  # creates a clock object for timing

# jazz sprite
jazz = Jazz()

# all sprites'group
all_sprites = pygame.sprite.Group()
all_sprites.add(jazz)

is_game_running = True

# main game loop
while is_game_running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False

        # tries to change jazz
        jazz.move(event)

    # blits the self.img onto the surface (screen)
    # uses self.rect for coordinates --> self.rect must be updated!
    all_sprites.draw(screen)
    all_sprites.update()  # updates rect.x

    clock.tick(60)  # only three images per second
    pygame.display.update()  # displays the UPDATED whole screen's new state
    screen.fill((0, 0, 0))  # paints the whole screen to black again before next blit

pygame.quit()
