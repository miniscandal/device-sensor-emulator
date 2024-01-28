"""
Module responsibility:

Define callback functions: Sets up callback functions for events in an MQTT client lifecycle.
"""

# pylint:disable=import-error

from feature_on_connect.feature import on_connect
from feature_on_message.feature import on_message
from feature_on_publish.feature import on_publish
from feature_on_disconnect.feature import on_disconnect
from shared.feature_custom_mqtt_client.feature import CustomMqttClient


def define_callback_handlers(client: CustomMqttClient) -> CustomMqttClient:
    """
    return:
        client: instance of the MQTT client.
    """

    client.on_connect = on_connect  # type: ignore
    client.on_disconnect = on_disconnect  # type: ignore
    client.on_message = on_message  # type: ignore
    client.on_publish = on_publish  # type: ignore

    return client
