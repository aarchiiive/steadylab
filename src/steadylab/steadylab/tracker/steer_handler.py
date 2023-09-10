import sys

import rclpy
from rclpy.node import Node
from steady_msgs.msg import ReadCar, WriteCar, BoundingBox, BoundingBoxes
from sensor_msgs.msg import Image

from .window import Window

class SteerHandler(Node):
    def __init__(self, init_ratio, window_size=8, qos=1) -> None:
        self.init_ratio = init_ratio

        self.window = Window(window_size)

        self._subscribers = {"yolo": self.create_subscription(BoundingBoxes, "/yolo", self.yolo_callback, qos),
                             "depth": self.create_subscription(Image, "/depth", self.depth_callback, qos)}
        
    def yolo_callback(self, msg):
        pass

    def depth_callback(self, msg):
        pass