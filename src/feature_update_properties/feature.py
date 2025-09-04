"""
Module responsibility:

State update and reporting: It involves updating the state and communicating it
to the control system.

Define a callback for on_publish event: It runs the module target when
the device status update is successfully sent to the control system.
"""

# pylint:disable=missing-function-docstring
# pylint:disable=import-error

import os
import json

import paho.mqtt.client as mqtt

from shared.feature_custom_mqtt_client.feature import CustomMqttClient
from shared.feature_inform_control_system.feature import inform_control_system
from shared.feature_update_env.feature import update_env_device_id
from shared.constants.constants import USERDATA_PROPERTY_DEVICE_ID
from shared.constants.constants import USERDATA_PROPERTY_STATUS_CODE
from shared.constants.constants import USERDATA_PROPERTY_PROCEDURE_CODE
from shared.constants.constants import MSG_UPDATE_PROPERTIES
from shared.constants.constants import STATUS_CODE_UPDATED_PROPERTIES
from shared.constants.constants import PROCEDURE_CODE_UPDATE_PROPERTIES


def callback_on_publish(
    client: CustomMqttClient,
    userdata: dict[str, str | int],
    mid: int,
) -> None:
    # pylint:disable=unused-argument

    print(MSG_UPDATE_PROPERTIES.format(mid=mid))


def update_properties(
    client: CustomMqttClient,
    userdata: dict[str, str | int],
    message: mqtt.MQTTMessage,
) -> None:
    payload = json.loads(message.payload.decode("utf-8"))
    new_device_id = payload.get(USERDATA_PROPERTY_DEVICE_ID)
    update_env_device_id(device_id=new_device_id)  # type: ignore
    device_id = os.getenv("DEVICE_ID")
    userdata.update(
        {
            USERDATA_PROPERTY_DEVICE_ID: device_id,
            USERDATA_PROPERTY_STATUS_CODE: STATUS_CODE_UPDATED_PROPERTIES,
            USERDATA_PROPERTY_PROCEDURE_CODE: PROCEDURE_CODE_UPDATE_PROPERTIES,
        }  # type: ignore
    )

    client.user_data_set(userdata)
    client.callback_on_publish = callback_on_publish
    inform_control_system(client=client, userdata=userdata)
