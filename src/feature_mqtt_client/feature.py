"""
Module responsibility:

MQTT broker connection: A connection is established with the MQTT broker, enabling
topic publication or subscription.

Topic subscription: Subscriptions are made to the topics predefined in the
environment variables."
"""

# pylint:disable=import-error
# pylint:disable=missing-function-docstring

from shared.feature_custom_mqtt_client.feature import CustomMqttClient

from shared.constants.constants import USERDATA_PROPERTY_DEVICE_ID


from shared.constants.config import MQTT_BROKER_HOST
from shared.constants.config import MQTT_BROKER_PORT
from shared.constants.config import MQTT_BROKER_KEEPALIVE

from shared.constants.config import DEVICE_ID

from shared.constants.config import MQTT_TOPIC_BROADCAST
from shared.constants.config import MQTT_TOPIC_DEVICE


def connect(client: CustomMqttClient) -> CustomMqttClient:
    client.connect(MQTT_BROKER_HOST, MQTT_BROKER_PORT, MQTT_BROKER_KEEPALIVE)  # type: ignore

    return client


def subscribe_topic(client: CustomMqttClient) -> CustomMqttClient:
    userdata = {USERDATA_PROPERTY_DEVICE_ID: DEVICE_ID}

    client.subscribe(MQTT_TOPIC_BROADCAST)  # type: ignore
    client.subscribe(MQTT_TOPIC_DEVICE)  # type: ignore
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
