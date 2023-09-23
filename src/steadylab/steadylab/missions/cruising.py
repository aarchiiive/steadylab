import sys
import time

import rclpy
from rclpy.node import Node

sys.path.append("src/steadylab/steadylab")

from core.message import Int64, Int16
from missions.mission import Mission

class Cruising(Mission):
    def __init__(self, 
                 queue_size: int = 5,
                 min_duration: float = 2.0,
                 qos: int = 5):
        super().__init__("cruising", queue_size, min_duration, qos)
        
        self._subscribers = {"steer": self.create_subscription(Int16, "/lane_steer", self.steer_callback, qos)}
    
    def steer_callback(self, msg: Int16):
        self.reset()
        if self.running:
            self.steer = msg.data
    
    def run(self):
        self.running = True
        self.last = time.time()
        return self.steer
        
        
def main(args=None):
    rclpy.init(args=args)
                                      
    node = Cruising()
                                                                          
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()
    
    return node

if __name__ == "__main__":
    main()