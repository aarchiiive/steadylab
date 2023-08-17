import os
import sys

import cv2
import numpy as np

import torch

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from sensor_msgs.msg import Image

sys.path.append("src/steadylab/steadylab")

from subscriber import Subscriber


class ZedSubscriber(Subscriber):
    def __init__(self, name, topic, msg_type):
        super().__init__(name, topic, msg_type)
        self.subscription = self.create_subscription(msg_type, topic, self.callback, 1)
        print(f"Subscribe {topic}.....")

    def callback(self, msg):
        print(type(msg.data))
        # pass
        # self.get_logger().info('I heard: "%s"' % msg.data)
        # self.get_logger().info(f"{type(msg.data)}")
        # print(type(msg.data))

def main(args=None):
    rclpy.init(args=args)

    subscriber = ZedSubscriber("sub_zed_image", "/zed2i/zed_node/left_raw/image_raw_color", Image)

    rclpy.spin(subscriber)

    print("DFDF")

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()