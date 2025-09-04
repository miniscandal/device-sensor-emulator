"""
Module responsibility:

Message Publishing: It publishes the messages to the specified topic and informs
the control system.
"""

# pylint:disable=import-error
# pylint:disable=missing-function-docstring

import json

from shared.feature_custom_mqtt_client.feature import CustomMqttClient
from shared.constants.constants import MSG_PUBLISH
from shared.constants.config import MQTT_TOPIC_CS_WEB_STATUS


def publish_message(client: CustomMqttClient, message: str, topic: str) -> None:
    print(MSG_PUBLISH.format(topic=topic, message=message))
    client.publish(topic, message)


def inform_control_system(
    client: CustomMqttClient,
    userdata: dict[str, str | int],
) -> None:
    message = json.dumps(userdata)
    publish_message(client=client, topic=MQTT_TOPIC_CS_WEB_STATUS, message=message)  # type: ignore
