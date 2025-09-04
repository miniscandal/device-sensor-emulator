"""
Application configuration module.

Centralizes environment variables with safe defaults.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# MQTT Broker configuration

MQTT_BROKER_HOST = os.getenv("MQTT_BROKER_HOST", "localhost")
MQTT_BROKER_PORT = int(os.getenv("MQTT_BROKER_PORT", "1883"))
MQTT_BROKER_KEEPALIVE = int(os.getenv("MQTT_BROKER_KEEPALIVE", "60"))

# Device configuration

DEVICE_ID = os.getenv("DEVICE_ID", "0")

# MQTT Topics - Subscription

MQTT_TOPIC_BROADCAST = os.getenv("MQTT_TOPIC_SUB_BROADCAST", "broadcast")
MQTT_TOPIC_DEVICE = os.getenv("MQTT_TOPIC_DEVICE", f"broadcast/device/{DEVICE_ID}")

# MQTT Topics - Publication

MQTT_TOPIC_CS_WEB_CMDS = os.getenv("MQTT_TOPIC_CS_WEB_CMDS", "control-system-web/commands")
MQTT_TOPIC_CS_WEB_STATUS = os.getenv("MQTT_TOPIC_CS_WEB_STATUS", "control-system-web/status")
MQTT_TOPIC_CS_WEB_METRICS = os.getenv("MQTT_TOPIC_CS_WEB_METRICS", "control-system-web/metrics")
