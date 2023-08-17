import os
import sys

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

from typing import Any

sys.path.append("src/steadylab/steadylab")

from messages import is_compatible_msg

class Publisher(Node):
    """
    Base class of publisher
    """
    def __init__(self, name, topic, msg_type):
        super().__init__(name)
        assert is_compatible_msg(msg_type), f"{msg_type} is not compatible"
        self.publisher_ = self.create_publisher(msg_type, topic, 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.callback)
    
    def callback(self):
        pass

def main(args=None):
    rclpy.init(args=args)

    publisher = Publisher()

    rclpy.spin(publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()