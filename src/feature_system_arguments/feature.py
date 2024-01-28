"""
Module responsibility:

Argument configuration: It sets up the necessary arguments for the script.

Argument parsing: It parses the arguments passed to the script and returns
them in a structured format.
"""

# pylint:disable=import-error
# pylint:disable=missing-function-docstring

import argparse

from shared.constants.constants import HELP_MSG_DEVICE_ID_ARG
from shared.constants.constants import HELP_MSG_SECONDS_ARG


def configuration_arguments_parser() -> argparse.ArgumentParser:
    argument_parser = argparse.ArgumentParser()

    argument_parser.add_argument(
        "-i", "--device_id", required=True, type=int, help=HELP_MSG_DEVICE_ID_ARG
    )
    argument_parser.add_argument(
        "-s",
        "--seconds",
        required=True,
        type=int,
        help=HELP_MSG_SECONDS_ARG,
    )

    return argument_parser


def system_arguments() -> argparse.Namespace:
    """
    return:
        argparse.Namespace: namespace containing the parsed arguments.
    """

    sys_arguments = configuration_arguments_parser()

    return sys_arguments.parse_args()
