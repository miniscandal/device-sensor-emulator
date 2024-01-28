"""
Module responsibility:

Manage callback on disconnect: Update the necessary information to know the
current status of the device and print that status.
"""

# pylint:disable=missing-function-docstring
# pylint:disable=import-error

from shared.feature_custom_mqtt_client.feature import CustomMqttClient
from shared.constants.constants import STATUS_CODE_DISCONNECTED
from shared.constants.constants import PROCEDURE_CODE_DISCONNECT
from shared.constants.constants import USERDATA_PROPERTY_STATUS_CODE
from shared.constants.constants import USERDATA_PROPERTY_PROCEDURE_CODE
from shared.constants.constants import MSG_ON_DISCONNECTED


def on_disconnect(
    client: CustomMqttClient,
    userdata: dict[str, str | int],
    rc: int,
) -> None:
    # pylint:disable=unused-argument

    userdata.update(
        {
            USERDATA_PROPERTY_STATUS_CODE: STATUS_CODE_DISCONNECTED,
            USERDATA_PROPERTY_PROCEDURE_CODE: PROCEDURE_CODE_DISCONNECT,
        }
    )
    print(userdata)
    print(MSG_ON_DISCONNECTED.format(rc=rc))
