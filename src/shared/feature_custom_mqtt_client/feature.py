"""
Module responsibility:

Custom MQTT Client: Provides a custom MQTT client that enhances and
extends the capabilities of the paho.mqtt.client. It allows for independent
management of the properties required to be instantiated in the MQTT client and
its associated events.
"""

# pylint:disable=missing-class-docstring
# pylint:disable=missing-function-docstring

from typing import Any

import paho.mqtt.client as mqtt


class CustomMqttClient(mqtt.Client):
    def __init__(self):
        super().__init__()
        self._enable_parameter_publish: bool = True
        self._callback_on_publish: Any = "Evie"

    @property
    def enable_parameter_publish(self):
        return self._enable_parameter_publish

    @enable_parameter_publish.setter
    def enable_parameter_publish(self, value: bool):
        self._enable_parameter_publish = value

    @property
    def callback_on_publish(self):
        return self._callback_on_publish

    @callback_on_publish.setter
    def callback_on_publish(self, value: Any):
        self._callback_on_publish = value
