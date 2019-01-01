"""
Init module of Jazzpy to expose the game settings and the
main play function.
"""
import yaml


def parse_yml_settings(file_path):
    """ Parses Yml file to python dict. """

    with open(file_path, "r") as stream:
        config_dict = yaml.load(stream)

        return config_dict


GAME_SETTINGS = parse_yml_settings("./jazzpy/settings.yml")

from .main import JazzPy  # exposes main play function
