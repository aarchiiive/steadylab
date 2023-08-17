import os
import sys

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

from typing import Any
from overrides import overrides

sys.path.append("src/steadylab/steadylab")

class Publisher(Node):
    """
    Base class of publisher
    """
    def __init__(self, name : str, msg_type : Any):
        super().__init__(name)
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
    
    def timer_callback(self):
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