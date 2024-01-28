"""
Module responsibility:

Message Publishing: It publishes the messages to the specified topic and informs
the control system.
"""

# pylint:disable=import-error
# pylint:disable=missing-function-docstring

import os
import json

from shared.feature_custom_mqtt_client.feature import CustomMqttClient
from shared.constants.constants import MSG_PUBLISH
from shared.constants.constants import ENV_MQTT_TOPIC_PUBLISH


def publish_message(client: CustomMqttClient, message: str, topic: str) -> None:
    print(MSG_PUBLISH.format(topic=topic, message=message))
    client.publish(topic, message)


def inform_control_system(
    client: CustomMqttClient,
    userdata: dict[str, str | int],
) -> None:
    topic = os.getenv(ENV_MQTT_TOPIC_PUBLISH)
    message = json.dumps(userdata)
    publish_message(client=client, topic=topic, message=message)  # type: ignore
