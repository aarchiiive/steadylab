import os
import sys

import torch
import numpy as np

from rclpy.node import Node

class Traffic(Node):
    def __init__(self, messages: dict):
        super().__init__("traffic")
        self.qos_profile = 5
        self.callbacks = {}
        self.processors = {}
        self.data = {}

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

        print("Traffic Initialize...")

    def make_callback(self, name):
        def callback(msg):
            self.data[name] = self.processors[name](msg)
            getattr(self, f"{name}_pub").publish(msg)
        return callback