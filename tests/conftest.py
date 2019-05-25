"""
Module with pytest configurations and hooks.
"""


def pytest_assertrepr_compare(config, op, left, right):
    """
    Function used to make dict differences easy to analyze while testing code.
    """
    if op in ("==", "!="):
        return ["{0} {1} {2}".format(left, op, right)]
