import sys
import time

from collections import deque

import rclpy
from rclpy.node import Node

import cv2

from steady_msgs.msg import BoundingBox, BoundingBoxes

sys.path.append("src/steadylab/steadylab")

from core.message import Int16
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

class Tunnel(Mission):
    def __init__(self, 
                 queue_size: int = 5,
                 min_duration: float = 3.0,
                 qos: int = 5):
        super().__init__("tunnel", queue_size, min_duration, qos)
        self.place_index = 1
        
        self.queue = deque([None for _ in range(queue_size)])
        
        self._subscribers = {"place": self.create_subscription(Int16, "/place", self.place_callback, qos)}
    
    def place_callback(self, msg: Int16):
        self.reset()
        _ = self.queue.popleft()
        self.queue.append(msg.data)
        if self.queue.count(self.place_index) >= 4:
            self.running = True
            self.last = time.time()
            
            
def spin(args=None):
    rclpy.init(args=args)
                                      
    node = Tunnel()
                                                                          
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()
    
    return node