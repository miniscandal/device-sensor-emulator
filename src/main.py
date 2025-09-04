# pylint:disable=line-too-long

"""
Module responsibility:

- Start the MQTT client: connects to an MQTT broker and handles publishing/subscribing.
- Continuously publish parameters at regular intervals, allowing a timely response
  to system changes.
- Handle callbacks:
    - on_connect(client, userdata, flags, rc): activated when the client connects to the MQTT server.
    - on_disconnect(client, userdata, rc): activated when the client disconnects.
    - on_subscribe(client, userdata, mid, granted_qos): activated when subscribing to a topic.
    - on_unsubscribe(client, userdata, mid): activated when unsubscribing from a topic.
    - on_publish(client, userdata, mid): activated when a message is successfully published.
    - on_message(client, userdata, message): activated when a message is received on a subscribed topic.
    - on_log(client, userdata, level, buf): activated when the library logs information.

Parameters used in callbacks:
- client: Instance of the MQTT client.
- userdata: User private data.
- flags: Response flags sent by the broker.
- rc: Connection result code.
- granted_qos: Granted Quality of Service (QoS) levels.
- message: The message received.
- level: Severity level of the log message.
- buf: Log message.

Additional features:
- Graceful shutdown on CTRL+C (KeyboardInterrupt) ensuring the MQTT client
  stops its loop and disconnects cleanly.
- Portable across Windows, Linux, and macOS.
- Simple and maintainable periodic publishing using a while loop with sleep.
"""

import json
import time
from dotenv import load_dotenv
from feature_system_arguments.feature import system_arguments
from shared.feature_update_env.feature import update_env_device_id
from feature_mqtt_client.feature import mqtt_client
from feature_define_callback_handlers.feature import define_callback_handlers
from feature_publish_parameters.feature import publish_parameters

# pylint: disable=missing-function-docstring

def final_payload(client, device_id: str) -> int:
    payload = { "device_id": str(device_id), "status": "offline" }
    msg = client.publish(topic="evie",payload=json.dumps(payload),qos=1,retain=True)
    msg.wait_for_publish()


def main():
    load_dotenv()
    arguments = system_arguments()
    update_env_device_id(device_id=arguments.device_id)

    client = mqtt_client()
    client = define_callback_handlers(client=client)
    client.loop_start()

    try:
        while True:
            if client.is_connected() and client.enable_parameter_publish:
                publish_parameters(client)
            time.sleep(arguments.publish_interval)
    except KeyboardInterrupt:
        print("\nStopping gracefully...")
        final_payload(client, '01')
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()
