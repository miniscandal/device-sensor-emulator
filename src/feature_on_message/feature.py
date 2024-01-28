"""
Module Responsibility:

Manage callback on message: Receives messages from the MQTT server and prints
them for debugging and logging purposes.

Extracting procedure codes: It extracts procedure codes from the received
messages to determine the appropriate action or response.

Handling messages: Handles the received messages by updating the user
data as device status and executing the corresponding procedure based on the
extracted procedure code.
"""

# pylint:disable=missing-function-docstring
# pylint:disable=import-error

import json
import paho.mqtt.client as mqtt

from shared.feature_custom_mqtt_client.feature import CustomMqttClient
from shared.feature_procedures_dictionary.feature import get_procedures_dictionary
from shared.constants.constants import REQUEST_PROPERTY_PROCEDURE_CODE
from shared.constants.constants import MSG_ON_PROCEDURE_CODE_NOT_EXIST
from shared.constants.constants import MSG_ON_MESSAGE


def print_received_message(message: mqtt.MQTTMessage) -> None:
    topic = message.topic
    payload = message.payload.decode("utf-8")
    print(MSG_ON_MESSAGE.format(topic=topic, payload=payload))


def get_procedure_code(message: mqtt.MQTTMessage) -> int:
    """
    return:
        int: procedure code.
    """

    payload = message.payload.decode("utf-8")
    payload_loads = json.loads(payload)
    procedure_code = payload_loads[REQUEST_PROPERTY_PROCEDURE_CODE]

    return procedure_code


def on_message(
    client: CustomMqttClient,
    userdata: dict[str, str | int],
    message: mqtt.MQTTMessage,
) -> None:
    print_received_message(message=message)
    procedures = get_procedures_dictionary()
    procedure_code = get_procedure_code(message=message)
    procedure = procedures.get(procedure_code)
    if procedure is None:
        print(MSG_ON_PROCEDURE_CODE_NOT_EXIST.format(procedure_code=procedure_code))
    else:
        procedure(client=client, userdata=userdata, message=message)
