"""
Module Responsibility:

State update and reporting: It involves updating the state and communicating it
to the control system.

Define a callback for on_publish event: It runs the module target when
the device status update is successfully sent to the control system.
"""

# pylint:disable=missing-function-docstring
# pylint:disable=import-error

from shared.feature_custom_mqtt_client.feature import CustomMqttClient
from shared.feature_inform_control_system.feature import inform_control_system
from shared.constants.constants import STATUS_CODE_CONNECTED
from shared.constants.constants import PROCEDURE_CODE_CONNECT
from shared.constants.constants import USERDATA_PROPERTY_STATUS_CODE
from shared.constants.constants import USERDATA_PROPERTY_PROCEDURE_CODE
from shared.constants.constants import MSG_ON_CONNECT


def callback_on_publish(
    client: CustomMqttClient, userdata: dict[str, str | int], mid: int
) -> None:
    # pylint:disable=unused-argument

    pass


def on_connect(
    client: CustomMqttClient,
    userdata: dict[str, str | int],
    flags: dict[str, int],
    rc: int,
) -> None:
    # pylint:disable=W0613

    print(MSG_ON_CONNECT.format(rc=rc))
    userdata.update(
        {
            USERDATA_PROPERTY_STATUS_CODE: STATUS_CODE_CONNECTED,
            USERDATA_PROPERTY_PROCEDURE_CODE: PROCEDURE_CODE_CONNECT,
        }
    )
    client.user_data_set(userdata)
    client.callback_on_publish = callback_on_publish
    client.enable_parameter_publish = True
    inform_control_system(client=client, userdata=userdata)
