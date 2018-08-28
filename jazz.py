"""
Main game module.
"""
import sys
import configparser
import pygame

from sprites.jazz.jazz import Jazz
from pygame.locals import *

# reads default configs
pygame.init()
config = configparser.RawConfigParser()
config.read("config.cfg")

WIDTH = config.getint("GAME_SCREEN", "WIDTH")
HEIGHT = config.getint("GAME_SCREEN", "HEIGHT")

# instantiates the first screen surface
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # pygame.surface.Surface
clock = pygame.time.Clock()  # creates a clock object for timing


# jazz_x, jazz_y = 50, 50
# jazz_img = pygame.image.load("jazz.png")
jazz = Jazz()

game_loop = True

move_right = False
move_left = False

while game_loop:

    # updates the screen surface to a new state
    # screen.blit(jazz_img, (jazz_x, jazz_y), (20, 20, 30, 35))

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_d:
                move_right = True

        if event.type == KEYDOWN:
            if event.key == K_a:
                move_left = True

        if event.type == KEYUP:
            if event.key == K_d:
                move_right = False

        if event.type == KEYUP:
            if event.key == K_a:
                move_left = False

        if event.type == pygame.QUIT:
            game_loop = False
            pygame.quit()
            sys.exit()

    if move_right:
        jazz.move(10, 0)

    if move_left:
        jazz.move(-10, 0)

    clock.tick(60)  # only three images per second
    pygame.display.update()  # displays the UPDATED whole screen's new state
    screen.fill((0, 0, 0))  # paints the whole screen to black again and then blits jazz

pygame.quit()
