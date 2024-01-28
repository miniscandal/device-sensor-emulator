"""
Module responsibility:

Start the MQTT client: The MQTT client is an entity that connects to an MQTT
server and can publish or subscribe to topics to receive messages.

Continuously Publish Parameters: Updates the control system with recent
data at regular intervals, allowing a timely response to system changes.

Callbacks:
on_connect(client, userdata, flags, rc): This callback is activated when the client
connects to the MQTT server.

on_disconnect(client, userdata, rc): This callback is activated when the client
disconnects from the MQTT server.

on_subscribe(client, userdata, mid, granted_qos): This callback is activated
when the client subscribes to a topic.

on_unsubscribe(client, userdata, mid): This callback is activated when the client
unsubscribes from a topic.

on_publish(client, userdata, mid): This callback is activated when a message
that the client publishes has been sent.

on_message(client, userdata, message): This callback is activated when a message
has been received on a topic to which the client is subscribed.

on_log(client, userdata, level, buf): This callback is activated
when the library has log information.

Parameters:
client: Instance of the MQTT client.
userdata: User private data.
flags: Response flags sent by the broker.
rc: Connection result code.|
granted_qos: Granted Quality of Service (QoS) levels.
message: The message received.
level: Severity level of the log message.
buf: Log message.
"""

# pylint:disable=missing-function-docstring

import time

from dotenv import load_dotenv
from feature_system_arguments.feature import system_arguments
from shared.feature_update_env.feature import update_env_device_id
from feature_mqtt_client.feature import mqtt_client
from feature_define_callback_handlers.feature import define_callback_handlers
from feature_publish_parameters.feature import publish_parameters


def main():
    load_dotenv()
    arguments = system_arguments()
    update_env_device_id(device_id=arguments.device_id)

    client = mqtt_client()
    client = define_callback_handlers(client=client)
    client.loop_start()

    while True:
        if not client.is_connected() or not client.enable_parameter_publish:
            continue

        publish_parameters(client=client)
        time.sleep(arguments.seconds)


if __name__ == "__main__":
    main()
