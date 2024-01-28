"""
Module responsibility:

State update and reporting: It involves updating the state and communicating it
to the control system.

Define a callback for on_publish event: It runs the module target when
the device status update is successfully sent to the control system.
"""

# pylint:disable=missing-function-docstring
# pylint:disable=import-error

import paho.mqtt.client as mqtt

from shared.feature_custom_mqtt_client.feature import CustomMqttClient
from shared.feature_inform_control_system.feature import inform_control_system
from shared.constants.constants import MSG_REPORT_STATUS


def callback_on_publish(
    client: CustomMqttClient,
    userdata: dict[str, str | int],
    mid: int,
) -> None:
    # pylint:disable=unused-argument

    print(MSG_REPORT_STATUS.format(mid=mid))


def report_status(
    client: CustomMqttClient,
    userdata: dict[str, str | int],
    message: mqtt.MQTTMessage,
) -> None:
    # pylint:disable=unused-argument

    client.user_data_set(userdata)
    client.callback_on_publish = callback_on_publish
    inform_control_system(client=client, userdata=userdata)
