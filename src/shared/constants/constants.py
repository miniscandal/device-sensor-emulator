"""
Module responsibility:
"""

# pylint:disable=W0105

"""
Device status code.
"""
STATUS_CODE_CLOSE_OPERATING_PROCESS = 100
STATUS_CODE_CONNECTED = 101
STATUS_CODE_DISCONNECTED = 102
STATUS_CODE_DISABLED_PARAMETER_PUBLISH = 103
STATUS_CODE_ENABLED_PARAMETER_PUBLISH = 104
STATUS_CODE_UPDATED_PROPERTIES = 105
STATUS_CODE_REPORTED_STATUS = 106


"""
Messages arguments help.
"""

HELP_MSG_DEVICE_ID_ARG = "Unique device identifier."
HELP_MSG_SECONDS_ARG = "Interval in seconds to repeat a publish."


"""
Device procedure code.
"""
PROCEDURE_CODE_SHUT_DOWN_DEVICE_SYSTEM = 0
PROCEDURE_CODE_CONNECT = 1
PROCEDURE_CODE_DISCONNECT = 2
PROCEDURE_CODE_DISABLE_PARAMETER_PUBLISH = 3
PROCEDURE_CODE_ENABLE_PARAMETER_PUBLISH = 4
PROCEDURE_CODE_UPDATE_PROPERTIES = 5
PROCEDURE_CODE_REPORT_STATUS = 6


"""
Properties received by the control system.
"""
REQUEST_PROPERTY_PROCEDURE_CODE = "procedure_code_request"


"""
Device parameters.
"""
PARAMETER_HUMIDITY = "humidity"
PARAMETER_TEMPERATURE = "temperature"
PARAMETER_DEVICE_ID = "device_id"
PARAMETER_TIMESTAMP = "timestamp"


"""
Client MQTT userdata.
"""
USERDATA_PROPERTY_STATUS_CODE = "status_code"
USERDATA_PROPERTY_PROCEDURE_CODE = "procedure_code"
USERDATA_PROPERTY_DEVICE_ID = "device_id"

"""
Messages handle client on events.
"""
MSG_ON_CONNECT = "on connect, rc: {rc}"
MSG_ON_MESSAGE = "on message, topic: {topic}, payload: {payload}"
MSG_ON_DISCONNECTED = "on disconnected, rc: {rc}"
MSG_ON_PROCEDURE_CODE_NOT_EXIST = "does not exist, procedure code: {procedure_code}"
MSG_PUBLISH = "publish, topic: {topic}, message: {message}"
MSG_CLOSE_OPERATING_PROCESS = "close operating process, mid: {mid}"
MSG_ENABLE_PARAMETER_PUBLISH = "enable parameter publishing, mid: {mid}"
MSG_DISABLE_PARAMETER_PUBLISH = "disable parameter publishing, mid: {mid}"
MSG_UPDATE_PROPERTIES = "updated properties, mid: {mid}"
MSG_REPORT_STATUS = "reported status, mid: {mid}"


"""
Messages errors.
"""
MSG_ERROR_ENV = "Environment variable is not set, env: {env}"


"""
Environment variable names.
"""
ENV_MQTT_BROKER_HOST = "MQTT_BROKER_HOST"
ENV_MQTT_BROKER_PORT = "MQTT_BROKER_PORT"
ENV_MQTT_BROKER_KEEPALIVE = "MQTT_BROKER_KEEPALIVE"
ENV_MQTT_GENERAL_TOPIC_SUBSCRIBE = "MQTT_GENERAL_TOPIC_SUBSCRIBE"
ENV_MQTT_PRIVATE_TOPIC_SUBSCRIBE = "MQTT_PRIVATE_TOPIC_SUBSCRIBE"
ENV_MQTT_TOPIC_PUBLISH = "MQTT_TOPIC_PUBLISH"
ENV_DEVICE_ID = "DEVICE_ID"
