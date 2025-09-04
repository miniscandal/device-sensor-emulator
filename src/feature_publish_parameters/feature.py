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
from shared.constants.constants import USERDATA_PROPERTY_STATUS_CODE
from shared.constants.constants import USERDATA_PROPERTY_PROCEDURE_CODE
from shared.constants.constants import USERDATA_PROPERTY_DEVICE_ID
from shared.constants.constants import STATUS_CODE_REPORTED_PARAMETERS
from shared.constants.constants import PROCEDURE_CODE_REPORT_PARAMETERS
from shared.constants.config import MQTT_TOPIC_CS_WEB_STATUS



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
    device_id = os.getenv("DEVICE_ID")
    parameters: dict[str, float | str | int] = calculate_parameters()
    data: dict[str, float | str | int] = {
        USERDATA_PROPERTY_DEVICE_ID: device_id,
        USERDATA_PROPERTY_STATUS_CODE: STATUS_CODE_REPORTED_PARAMETERS,
        USERDATA_PROPERTY_PROCEDURE_CODE: PROCEDURE_CODE_REPORT_PARAMETERS,
        **parameters,
    }
    message = json.dumps(data)
    publish_message(client, message, MQTT_TOPIC_CS_WEB_STATUS)
