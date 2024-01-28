"""
Module responsibility:

State update and reporting: It involves updating the state and communicating it
to the control system.

Define a callback for on_publish event: It runs the module target when
the device status update is successfully sent to the control system.
"""
# pylint:disable=import-error
# pylint:disable=missing-function-docstring

import paho.mqtt.client as mqtt

from shared.feature_custom_mqtt_client.feature import CustomMqttClient
from shared.feature_inform_control_system.feature import inform_control_system
from shared.constants.constants import USERDATA_PROPERTY_STATUS_CODE
from shared.constants.constants import USERDATA_PROPERTY_PROCEDURE_CODE
from shared.constants.constants import MSG_ENABLE_PARAMETER_PUBLISH
from shared.constants.constants import STATUS_CODE_ENABLED_PARAMETER_PUBLISH
from shared.constants.constants import PROCEDURE_CODE_ENABLE_PARAMETER_PUBLISH


def callback_on_publish(
    client: CustomMqttClient,
    userdata: dict[str, str | int],
    mid: int,
) -> None:
    # pylint:disable=unused-argument

    print(MSG_ENABLE_PARAMETER_PUBLISH.format(mid=mid))
    client.enable_parameter_publish = True


def enable_parameter_publish(
    client: CustomMqttClient,
    userdata: dict[str, str | int],
    message: mqtt.MQTTMessage,
) -> None:
    # pylint:disable=unused-argument

    userdata.update(
        {
            USERDATA_PROPERTY_STATUS_CODE: STATUS_CODE_ENABLED_PARAMETER_PUBLISH,
            USERDATA_PROPERTY_PROCEDURE_CODE: PROCEDURE_CODE_ENABLE_PARAMETER_PUBLISH,
        }
    )
    client.user_data_set(userdata)
    client.callback_on_publish = callback_on_publish
    inform_control_system(client=client, userdata=userdata)
