"""
Module responsibility:

Manage callback on publish: It calls the callback function specified in the user data
when a message is published.
"""

# pylint:disable=missing-function-docstring
# pylint:disable=import-error

from shared.feature_custom_mqtt_client.feature import CustomMqttClient


def on_publish(
    client: CustomMqttClient,
    userdata: dict[str, str | int],
    mid: int,
) -> None:
    if client.callback_on_publish is None:
        return

    client.callback_on_publish(client=client, userdata=userdata, mid=mid)
    client.callback_on_publish = None
