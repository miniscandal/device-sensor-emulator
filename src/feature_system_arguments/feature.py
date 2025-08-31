"""
Module responsibility:

This module is responsible for configuring and parsing command-line arguments.

- Argument configuration: Defines the available CLI arguments, their types,
  and their help messages.
- Argument parsing: Parses the provided CLI arguments and returns them in a
  structured format (argparse.Namespace), making them accessible within the
  application.
"""

import argparse

from feature_system_arguments.constants.messages_args_help import HELP_MSG_DEVICE_ID_ARG
from feature_system_arguments.constants.messages_args_help import HELP_MSG_SECONDS_ARG


def configuration_arguments_parser(
    device_id_help: str = HELP_MSG_DEVICE_ID_ARG,
    publish_interval_help: str = HELP_MSG_SECONDS_ARG,
) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--device_id", required=True, type=int, help=device_id_help
    )
    parser.add_argument(
        "-s", "--publish_interval", required=True, type=int, help=publish_interval_help
    )
    return parser


def system_arguments(
    device_id_help: str = HELP_MSG_DEVICE_ID_ARG,
    publish_interval_help: str = HELP_MSG_SECONDS_ARG,
) -> argparse.Namespace:
    """Parse and return system arguments.

    Args:
        device_id_help (str): Help message for the device_id argument.
        publish_interval_help (str): Help message for the publish interval argument.

    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """
    parser = configuration_arguments_parser(device_id_help, publish_interval_help)

    return parser.parse_args()
