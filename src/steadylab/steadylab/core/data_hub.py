import os
import sys

import torch
import numpy as np

from rclpy.node import Node
from std_msgs.msg import Int16

sys.path.append("src/steadylab/steadylab")


class DataHub(Node):
    def __init__(self, messages: dict):
        super().__init__("data_hub")
        self.qos_profile = 5
        self.callbacks = {}
        self.processors = {}
        self.data = {}

        for name, message in messages.items():
            self.callbacks[name] = self.create_callback(name)
            self.processors[name] = message.processor
            self.data[name] = None

            setattr(self, f"sub_{name}", self.create_subscription(
                message.msg_type,
                message.topic,
                self.callbacks[name],
                self.qos_profile,
            ))
            
            setattr(self, f"pub_{name}", self.create_publisher(
                message.msg_type,
                f"/{name}",
                self.qos_profile,
            ))

        print("Datahub Initialize...")

    def create_callback(self, name):
        def callback(msg):
            self.data[name] = msg
            getattr(self, f"pub_{name}").publish(msg)
        return callback