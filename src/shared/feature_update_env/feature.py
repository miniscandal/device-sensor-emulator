"""
Module responsibility.

Environment management updates: Updates system environment variables to ensure
proper configuration and operation.
"""

# pylint:disable=missing-function-docstring
# pylint:disable=import-error

import os

from shared.constants.config import MQTT_TOPIC_DEVICE


def update_env_device_id(device_id: int) -> None:
    os.environ["MQTT_TOPIC_DEVICE"] = MQTT_TOPIC_DEVICE.format(id=device_id)
    os.environ["DEVICE_ID"] = str(device_id)
