"""
Module responsibility:

Procedure Mapping: It maps the procedure codes to their respective
functions and returns them in a structured format.
"""

# pylint:disable=import-error

from feature_shut_down_device_system.feature import shut_down_device_system
from feature_report_status.feature import report_status
from feature_disable_parameter_publish.feature import disable_parameter_publish
from feature_enable_parameter_publish.feature import enable_parameter_publish
from feature_update_properties.feature import update_properties

from shared.constants.constants import PROCEDURE_CODE_SHUT_DOWN_DEVICE_SYSTEM
from shared.constants.constants import PROCEDURE_CODE_DISABLE_PARAMETER_PUBLISH
from shared.constants.constants import PROCEDURE_CODE_ENABLE_PARAMETER_PUBLISH
from shared.constants.constants import PROCEDURE_CODE_UPDATE_PROPERTIES
from shared.constants.constants import PROCEDURE_CODE_REPORT_STATUS


def get_procedures_dictionary():
    """
    Defines a dictionary with the procedures necessary for the script.

    return:
        dict: dictionary object that contains the available procedures used by this script.
    """

    procedures = {
        PROCEDURE_CODE_SHUT_DOWN_DEVICE_SYSTEM: shut_down_device_system,
        PROCEDURE_CODE_DISABLE_PARAMETER_PUBLISH: disable_parameter_publish,
        PROCEDURE_CODE_ENABLE_PARAMETER_PUBLISH: enable_parameter_publish,
        PROCEDURE_CODE_UPDATE_PROPERTIES: update_properties,
        PROCEDURE_CODE_REPORT_STATUS: report_status,
    }

    return procedures
