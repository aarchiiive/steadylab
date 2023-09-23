import sys
import time

from collections import deque

import rclpy
from rclpy.node import Node

import cv2
import numpy as np
from cv_bridge import CvBridge  

from steady_msgs.msg import BoundingBox, BoundingBoxes

sys.path.append("src/steadylab/steadylab")

from core.message import Int64, Image, Bool
from missions.mission import Mission

"""
- blue_arrow # 0
- construction_sign # 1
- hipass # 2
- left_arrow # 3
- left_sign # 4
- pe_drum # 5
- red_cone # 6
- red_pe_drum # 7
- slash # 8
- speed_bump # 9
- speed_sign # 10
- stop_line # 11
- tollgate_box # 12
- tollgate_sign # 13
- tubular_marker # 14
- tunnel_arrow # 15
- tunnel_entrance # 16
- tunnel_message # 17
- x_arrow # 18
"""

class ComplexArea(Mission):
    def __init__(self, 
                 queue_size: int = 10,
                 min_duration: float = 2.0,
                 qos: int = 5):
        super().__init__("complex_area", queue_size, min_duration, qos)
        self.objects = [24, 25, 26, 27, 28, 29]
        
        self._publishers = {"steer": self.create_publisher(Int64, "/dynamic_obstacle_steer", qos),
                            "running": self.create_publisher(Bool, "/dynamic_obstacle", qos)}
        self._subscribers = {"yolo": self.create_subscription(BoundingBoxes, "/yolo", self.yolo_callback, qos)}
    
        self.timer = self.create_timer(0.1, self.callback)
    
    def callback(self):
        steer, running = Int64(), Bool()
        steer.data = self.steer
        running.data = self.running
        self._publishers["steer"].publish(steer)
        self._publishers["running"].publish(running)
    
    
    def yolo_callback(self, msg: BoundingBoxes):
        self.reset()
        
        for box in msg.boxes:
            _ = self.queue.popleft()
            self.queue.append(box.cls)
            
        counts = sum([self.queue.count(o) for o in self.objects])
        
        if counts >= int(0.8*len(self.queue)):
            self.running = True
            self.last = time.time()
    
    
def main(args=None):
    rclpy.init(args=args)
                                      
    node = ComplexArea()
                                                                          
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()
    
    return node

if __name__ == "__main__":
    main()