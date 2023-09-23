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

class RightTurn(Mission):
    def __init__(self, 
                 queue_size: int = 5,
                 min_duration: float = 2.0,
                 qos: int = 5):
        super().__init__("right_turn", queue_size, min_duration, qos)
        self.place = 1
        
        self.queue = deque([None for _ in range(queue_size)])
        
        self._subscribers = {"place": self.create_subscription(Int16, "/place", self.place_callback, qos)}
    
    def place_callback(self, msg: Int16):
        self.reset()
        
        _ = self.queue.popleft()
        self.queue.append(msg.data)
        
        if self.queue.count(self.place) >= int(0.8*len(self.queue)):
            self.running = True
            self.last = time.time()

def main(args=None):
    rclpy.init(args=args)
                                      
    node = RightTurn()
                                                                          
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()
    
    return node

if __name__ == "__main__":
    main()