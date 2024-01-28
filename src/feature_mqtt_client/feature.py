"""
Module responsibility:

MQTT broker connection: A connection is established with the MQTT broker, enabling
topic publication or subscription.

Topic subscription: Subscriptions are made to the topics predefined in the
environment variables."
"""

# pylint:disable=import-error
# pylint:disable=missing-function-docstring

import os

from shared.feature_custom_mqtt_client.feature import CustomMqttClient
from shared.constants.constants import ENV_MQTT_GENERAL_TOPIC_SUBSCRIBE
from shared.constants.constants import ENV_MQTT_PRIVATE_TOPIC_SUBSCRIBE
from shared.constants.constants import ENV_MQTT_BROKER_HOST
from shared.constants.constants import ENV_MQTT_BROKER_PORT
from shared.constants.constants import ENV_MQTT_BROKER_KEEPALIVE
from shared.constants.constants import ENV_DEVICE_ID
from shared.constants.constants import USERDATA_PROPERTY_DEVICE_ID


def connect(client: CustomMqttClient) -> CustomMqttClient:
    host = os.getenv(ENV_MQTT_BROKER_HOST)
    port = os.getenv(ENV_MQTT_BROKER_PORT)
    keepalive = os.getenv(ENV_MQTT_BROKER_KEEPALIVE)
    client.connect(host, int(port), int(keepalive))  # type: ignore

    return client


def subscribe_topic(client: CustomMqttClient) -> CustomMqttClient:
    general_topic = os.getenv(ENV_MQTT_GENERAL_TOPIC_SUBSCRIBE)
    private_topic = os.getenv(ENV_MQTT_PRIVATE_TOPIC_SUBSCRIBE)

    userdata = {USERDATA_PROPERTY_DEVICE_ID: os.getenv(ENV_DEVICE_ID)}

    client.subscribe(general_topic)  # type: ignore
    client.subscribe(private_topic)  # type: ignore
    client.user_data_set(userdata=userdata)

    return client


def mqtt_client() -> CustomMqttClient:
    """
    return:
        client: instance of the MQTT client.
    """

    client = CustomMqttClient()
    client = connect(client=client)
    client = subscribe_topic(client=client)

    return client
