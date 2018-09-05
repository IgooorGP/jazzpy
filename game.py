"""
Main game module.
"""
import configparser
import sys

import pygame
from pygame.locals import *

from models.jazz.jazz import Jazz
from camera.camera import Camera

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

# hardcoded level width and height
total_level_width = 2000
total_level_height = 1000

# the game camera
camera = Camera(WIDTH, HEIGHT, total_level_width, total_level_height)

# all sprites group
# all_sprites = pygame.sprite.Group()
# all_sprites.add(jazz)

is_game_running = True

# main game loop
while is_game_running:
    clock.tick(60)  # only three images per second
    camera.update(jazz)  # camera follows jazz, camera gets updated

    # here we capture the events based on the event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_running = False

        # captures events to update jazz
        jazz.capture_event(event)

    # updates jazz based on the events on the event loop
    jazz.update()
    # blits jazz's surface based on the updated camera
    screen.blit(jazz.image, camera.apply(jazz))

    pygame.display.update()  # displays the UPDATED whole screen's new state
    screen.fill((0, 0, 0))  # paints the whole screen to black again before next blit

pygame.quit()
