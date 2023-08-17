import os
import sys

import rclpy
from rclpy.node import Node

from std_msgs.msg import String

sys.path.append("src/steadylab/steadylab")

from messages import is_compatible_msg

class Subscriber(Node):
    def __init__(self, name, topic, msg_type):
        super().__init__(name)
        assert is_compatible_msg(msg_type), f"{msg_type} is not compatible"
        self.subscription = self.create_subscription(msg_type, topic, self.callback, 1)
        # self.subscription  # prevent unused variable warning

    def callback(self, msg):
        pass

def main(args=None):
    rclpy.init(args=args)

    subscriber = Subscriber()

    rclpy.spin(subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()