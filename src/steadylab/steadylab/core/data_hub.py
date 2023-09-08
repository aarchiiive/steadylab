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
        self.test = self.create_publisher(Int16, "/test", 10)
        self.timer = self.create_timer(0.5, self.test_callback)

        for name, message in messages.items():
            self.callbacks[name] = self.make_callback(name)
            self.processors[name] = message.processor
            self.data[name] = None

            setattr(self, f"{name}_sub", self.create_subscription(
                message.msg_type,
                message.topic,
                self.callbacks[name],
                self.qos_profile,
            ))
            
            setattr(self, f"{name}_pub", self.create_publisher(
                message.msg_type,
                f"/{name}",
                self.qos_profile,
            ))

        print("Datahub Initialize...")

    def make_callback(self, name):
        def callback(msg):
            self.data[name] = msg
            getattr(self, f"{name}_pub").publish(msg)
        return callback
    
    def test_callback(self):
        msg = Int16()
        msg.data = 1
        self.test.publish(msg)
        print(f"publish : {msg.data}")