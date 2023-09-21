import sys
import time

from collections import deque

from rclpy.node import Node

class Mission(Node):
    def __init__(self, 
                 node_name: str,
                 queue_size: int = 5,
                 min_duration: int = 2,
                 qos: int = 5):
        super().__init__(node_name)
        self.steer = 0
        self.running = False
        self.last = time.time()
        self.min_duration = min_duration
        
        self.queue = deque([None for _ in range(queue_size)])
    
    def reset(self):
        if time.time() - self.last > self.min_duration and self.running: 
            self.running = False
            