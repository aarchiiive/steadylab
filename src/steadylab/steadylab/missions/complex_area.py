import sys
import time
from ultralytics import YOLO
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
    def __init__(self, queue_size: int = 10,min_duration: float = 2.0,qos: int = 5):
        super().__init__("complex_area", queue_size, min_duration, qos)
        
        self._publishers = {"steer": self.create_publisher(Int64, "/complex_steer", qos),
                            "running": self.create_publisher(Bool, "/complex_area", qos)}
        self._subscribers = {"yolo": self.create_subscription(BoundingBoxes, "/yolo", self.yolo_callback, qos)}
    
        self.timer = self.create_timer(0.1, self.callback)
    
    def callback(self):
        steer, running = Int64(), Bool()
        steer.data = self.steer
        running.data = self.running
        self._publishers["steer"].publish(steer)
        self._publishers["running"].publish(running)
    
    
    def yolo_callback(self, data):
        self.reset()
        box_cls = data.boxes[0]
        box_name = data.boxes[1]
        box_xn = data.boxes[4][0]
        # boxes[4] = xywhn, boxes[4][0] = normalized x(0~1)
        box_conf = data.boxes[2]

        if 18 == box_cls and box_conf > 0.3:
            print("x_arrow")
            if (0.5-0.01) <= box_xn < (0.5-0.005):
                self.steer = -60
                print("turn left, steer -60")
            elif (0.5-0.4) <= box_xn < (0.5-0.01):
                self.steer = -90
                print("turn left, steer -90")
            elif (0.5+0.005) <= box_xn < (0.5+0.01):
                self.steer = 60
                print("turn right, steer 60")
            elif (0.5+0.01) <= box_xn < (0.5+0.04):
                self.steer = 90
                print("turn right, steer 90")

        elif 3 == box_cls and box_conf > 0.3:
            print(box_name) #left_arrow
            if (0.5-0.01) <= box_xn < (0.5-0.005):
                self.steer = -60
                print("turn left, steer -60")
            elif (0.5-0.4) <= box_xn < (0.5-0.01):
                self.steer = -90
                print("turn left, steer -90")
            elif (0.5+0.005) <= box_xn < (0.5+0.01):
                self.steer = 60
                print("turn right, steer 60")
            elif (0.5+0.01) <= box_xn < (0.5+0.04):
                self.steer = 90
                print("turn right, steer 90")

        elif 11 == box_cls and box_conf > 0.3:
            print(box_name) #stop_line
            if (0.5-0.01) <= box_xn < (0.5-0.005):
                self.steer = -60
                print("turn left, steer -60")
            elif (0.5-0.4) <= box_xn < (0.5-0.01):
                self.steer = -90
                print("turn left, steer -90")
            elif (0.5+0.005) <= box_xn < (0.5+0.01):
                self.steer = 60
                print("turn right, steer 60")
            elif (0.5+0.01) <= box_xn < (0.5+0.04):
                self.steer = 90
                print("turn right, steer 90")

        elif 9 == box_cls and box_conf > 0.3:
            print(box_name) #speed_bump
            if (0.5-0.01) <= box_xn < (0.5-0.005):
                self.steer = -60
                print("turn left, steer -60")
            elif (0.5-0.4) <= box_xn < (0.5-0.01):
                self.steer = -90
                print("turn left, steer -90")
            elif (0.5+0.005) <= box_xn < (0.5+0.01):
                self.steer = 60
                print("turn right, steer 60")
            elif (0.5+0.01) <= box_xn < (0.5+0.04):
                self.steer = 90
                print("turn right, steer 90")

        elif 8 == box_cls and box_conf > 0.3:
            print(box_name) #slash
            self.steer = 0

        elif 10 == box_cls and box_conf > 0.3:
            print(box_name) #speed_sign
            self.steer = 0

    
    
def main(args=None):
    rclpy.init(args=args)
                                      
    node = ComplexArea()
                                                                          
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()
    
    return node

if __name__ == "__main__":
    main()
