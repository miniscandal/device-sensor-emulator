"""
Module responsibility:

"""

# pylint:disable=missing-function-docstring

import logging


def log(message: str) -> None:
    logging.basicConfig(
        format="\n%(pathname)s:%(lineno)d\n%(message)s\n",
        level=logging.DEBUG,
    )
    logging.debug(message)
