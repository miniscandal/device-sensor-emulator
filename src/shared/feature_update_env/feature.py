"""
Module responsibility.

Environment management updates: Updates system environment variables to ensure
proper configuration and operation.
"""

# pylint:disable=missing-function-docstring
# pylint:disable=import-error

import os

from shared.constants.constants import ENV_MQTT_PRIVATE_TOPIC_SUBSCRIBE
from shared.constants.constants import ENV_DEVICE_ID


def update_env_device_id(device_id: int) -> None:
    env = os.getenv(ENV_MQTT_PRIVATE_TOPIC_SUBSCRIBE)
    os.environ[ENV_MQTT_PRIVATE_TOPIC_SUBSCRIBE] = env.format(id=device_id)  # type: ignore
    os.environ[ENV_DEVICE_ID] = str(device_id)
