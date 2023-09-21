from typing import List, Tuple, Sequence, Union                                      

import sys

import rclpy
from rclpy.node import Node
from steady_msgs.msg import ReadCar, WriteCar, BoundingBox, BoundingBoxes

sys.path.append("src/steadylab/steadylab")

from planning.window import Window
from core.message import Int64, Int8, Bool

class Steer(Node):
    def __init__(self, init_ratio=0.2, window_size=8, ratio=[0.4, 0.8], qos=1) -> None:
        super().__init__("steer")
        self.init_ratio = init_ratio
        self.steer = 0  # - : left + : right
        
        # -1 : stop / 0 : straight / 1 : right / 2 : left
        self.entire_state = 0 # 0 : depth + lane
        self.state = {"traffic": 0, "obstacle": 0}
        
        self.msg = {"steer": Int64()}
        self._publishers = {"steer": self.create_publisher(Int64, "/steer", qos)}
        self._subscribers = {
            "state":
            {
                "yolo": self.create_subscription(Int8, "/traffic_state", self.traffic_callback, qos),
                "obstacle": self.create_subscription(Int8, "/obstacle_state", self.obstacle_callback, qos),
            },
            "steer":
            {
                "depth": self.create_subscription(Int64, "/depth_steer", self.depth_callback, qos),
                "lane": self.create_subscription(Int64, "/lane_steer", self.lane_callback, qos),
                "obstacle": self.create_subscription(Int64, "/obstacle_steer", self.depth_callback, qos),
            }
        }

        self.timer = self.create_timer(0.2, self.callback)
    
    def traffic_callback(self, msg: Int8):
        self.state["traffic"] = msg.data
        
    def obstacle_callback(self, msg: Int8):
        self.state["obstacle"] = msg.data
    
    def yolo_callback(self, msg: Int64):
        self.steer += msg.data

    def depth_callback(self, msg: Int64):
        self.steer += msg.data
    
    def lane_callback(self, msg: Int64):
        self.steer = msg.data
        
    def combine(self):
        if -1 in self.state.values():
            self.entire_state = -1 # stop
        else:
            self.entire_state = 0

    def callback(self):
        self.combine()
        if self.entire_state == -1: # stop
            self.msg["steer"].data = 0
        elif self.entire_state == 0: # straight
            self.msg["steer"].data = min(max(int(self.steer), -2000), 2000)
        elif self.entire_state == 1: # left
            self.msg["steer"].data = min(max(int(self.steer), -2000), 2000)
        elif self.entire_state == 2: # right
            self.msg["steer"].data = min(max(int(self.steer), -2000), 2000)
        
        print("entire_state :", self.entire_state)
        print("steer :", self.msg["steer"].data)
                
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

