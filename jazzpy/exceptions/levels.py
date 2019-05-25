"""
Exceptions raised due to some problem related to the game levels.
"""


class CorruptedLevelFile(BaseException):
    """
    Raised when a level charcode of unexpected length is encountered during the level build.
    """

    pass


class MissingJazzInitialPositionOnLevelfile(BaseException):
    """
    Raised when a level charcode of unexpected length is encountered during the level build.
    """

    pass
