import os
import sys

import torch
import numpy as np

from rclpy.node import Node

sys.path.append("src/steadylab/steadylab")

# local
from core.message import is_compatible_msg
from core.processor import *


class Publisher(Node):
    def __init__(self, name, topic, msg_type, processor=None):
        super().__init__(name)
        assert is_compatible_msg(msg_type), f"{msg_type} is not compatible"
        self.name = name
        self.topic = topic
        self.msg_type = msg_type
        self.processor = processor
        self.pub = self.create_publisher(msg_type, topic, 1)
        # self.pub = self.create_publisher(msg_type, topic, 1)


class Subscriber(Node):
    def __init__(self, name, topic, msg_type, processor=None):
        super().__init__(name)
        assert is_compatible_msg(msg_type), f"{msg_type} is not compatible"
        self.name = name
        self.topic = topic
        self.msg_type = msg_type
        self.processor = processor
        self.sub = self.create_subscription(msg_type, topic, self.callback, 1)
        # self.pub = self.create_publisher(msg_type, topic, 1)

    def callback(self, msg):
        pass


class Zed(Subscriber):
    def __init__(self, name, topic, msg_type, processor=None):
        super().__init__(name, topic, msg_type, processor)

    def callback(self, msg):
        pass
        # data = self.processor(msg)

        # if isinstance(data, np.ndarray) and len(data.shape):
        #     pass
        
        # elif isinstance(data, torch.Tensor):
        #     pass

        # elif isinstance(data, dict):
        #     pass

        # else:
        #     pass

    
