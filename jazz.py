"""
Bootstrap module to start the game for development.
"""
from jazzpy import JazzPy


if __name__ == "__main__":
    game = JazzPy()
    game.play()  # starts the game loop
