"""
Module responsibility:
"""

from feature_mqtt_client.feature import CustomMqttClient

def publish_offline(client: CustomMqttClient, topic: str = "evie", payload: any = None):
    msg = client.publish(topic=topic, payload=payload, qos=1)
    msg.wait_for_publish()
