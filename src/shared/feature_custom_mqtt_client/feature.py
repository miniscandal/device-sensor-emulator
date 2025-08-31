"""
Module responsibility:

Custom MQTT Client: Provides a custom MQTT client that enhances and
extends the capabilities of the paho.mqtt.client. It allows for independent
management of the properties required to be instantiated in the MQTT client and
its associated events, including Last Will and Testament (LWT) configuration,
callback management, and property control.
"""

# pylint:disable=missing-class-docstring
# pylint:disable=missing-function-docstring

from typing import Any, Optional
import paho.mqtt.client as mqtt


class CustomMqttClient(mqtt.Client):
    def __init__(
        self,
        client_id: Optional[str] = None,
        clean_session: bool = True,
        userdata: Any = None,
    ):
        super().__init__(
            client_id=client_id, clean_session=clean_session, userdata=userdata
        )
        self._enable_parameter_publish: bool = False
        self._callback_on_publish: Optional[Any] = None
        self.configurar_lwt()

    @property
    def enable_parameter_publish(self) -> bool:
        return self._enable_parameter_publish

    @enable_parameter_publish.setter
    def enable_parameter_publish(self, value: bool):
        self._enable_parameter_publish = value

    @property
    def callback_on_publish(self) -> Optional[Any]:
        return self._callback_on_publish

    @callback_on_publish.setter
    def callback_on_publish(self, value: Any):
        self._callback_on_publish = value

    def configurar_lwt(
        self,
        topic: str = "evie",
        payload: str = "descendants",
        qos: int = 1,
        retain: bool = True,
    ):
        self.will_set(topic=topic, payload=payload, qos=qos, retain=retain)
