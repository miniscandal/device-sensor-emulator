"""
Module resposibility:

Management of simulated parameters: Implementation of fictitious parameters for
the device and transmission of these simulated parameters to the control system.
"""

# pylint:disable=import-error
# pylint:disable=missing-function-docstring

import os
import random
import json
import datetime

from shared.feature_custom_mqtt_client.feature import CustomMqttClient
from shared.feature_inform_control_system.feature import publish_message
from shared.constants.constants import PARAMETER_HUMIDITY
from shared.constants.constants import PARAMETER_TEMPERATURE
from shared.constants.constants import PARAMETER_TIMESTAMP
from shared.constants.constants import PARAMETER_DEVICE_ID
from shared.constants.constants import ENV_MQTT_TOPIC_PUBLISH
from shared.constants.constants import ENV_DEVICE_ID


def calculate_parameters() -> dict[str, float | str]:
    """
    return:
        dict: dictionary containing the calculated parameters.
    """

    parameters = {
        PARAMETER_TEMPERATURE: round(random.uniform(-40, 85), 2),
        PARAMETER_HUMIDITY: round(random.uniform(0, 100), 2),
        PARAMETER_TIMESTAMP: datetime.datetime.now().isoformat(),
    }

    return parameters


def publish_parameters(client: CustomMqttClient) -> None:
    topic = os.getenv(ENV_MQTT_TOPIC_PUBLISH)
    device_id = os.getenv(ENV_DEVICE_ID)
    parameters = calculate_parameters()
    parameters.update({PARAMETER_DEVICE_ID: device_id})  # type: ignore
    message = json.dumps(parameters)
    publish_message(client, message, topic)  # type: ignore
