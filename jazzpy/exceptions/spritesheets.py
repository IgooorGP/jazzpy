"""
Module with custom exceptions that are raised due to spritesheet errors.
"""


class SpritesheetImpossibleMatrixRowRequired(BaseException):
    """
    Raised when the a negative or impossible row is asked to the spritesheet class.
    """

    pass


class SpritesheetImpossibleMatrixColumnRequired(BaseException):
    """
    Raised when the a negative or impossible column is asked to the spritesheet class.
    """

    pass


class SpritesheetMatrixDimensionsNotConfigured(BaseException):
    """
    Raised when a spritesheet has no default matrix rows and columns defined.
    """

    pass
