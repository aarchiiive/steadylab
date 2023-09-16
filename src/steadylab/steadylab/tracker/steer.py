from typing import List, Tuple, Sequence, Union                                      

import sys

import rclpy
from rclpy.node import Node
from steady_msgs.msg import ReadCar, WriteCar, BoundingBox, BoundingBoxes

sys.path.append("src/steadylab/steadylab")

from tracker.window import Window
from core.message import Int64

class Steer(Node):
    def __init__(self, init_ratio=0.2, window_size=8, ratio=[0.4, 0.8], qos=1) -> None:
        super().__init__("steer_handler")
        self.init_ratio = init_ratio
        self.steer = 0  # - : left + : right

        self._subscribers = {"yolo": self.create_subscription(Int64, "/yolo_steer", self.yolo_callback, qos),
                             "depth": self.create_subscription(Int64, "/depth_steer", self.depth_callback, qos),
                             "lane": self.create_subscription(Int64, "/lane_steer", self.lane_callback, qos)}
        self._publishers = {"steer": self.create_publisher(Int64, "/steer", qos)}
        self.msg = {"steer": Int64()}
        
        self.timer = self.create_timer(0.2, self.callback)
        
    def yolo_callback(self, msg: Int64):
        self.steer += msg.data

    def depth_callback(self, msg: Int64):
        self.steer += msg.data
    
    def lane_callback(self, msg: Int64):
        self.steer += msg.data

    def callback(self):
        self.msg["steer"].data = int(self.steer)
        self._publishers["steer"].publish(self.msg["steer"])
        self.steer = int(self.steer * self.init_ratio)

def main(args=None):
    rclpy.init(args=args)
                                      
    steer = Steer()
                                                                          
    rclpy.spin(steer)

    steer.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

