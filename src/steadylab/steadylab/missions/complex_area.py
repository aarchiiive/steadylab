import sys
import time

from collections import deque

import rclpy
from rclpy.node import Node

from steady_msgs.msg import BoundingBox, BoundingBoxes

sys.path.append("src/steadylab/steadylab")

from core.message import Int16
from missions.mission import Mission

class ComplexArea(Mission):
    def __init__(self, 
                 queue_size: int = 10,
                 min_duration: float = 2.0,
                 qos: int = 5):
        super().__init__("complex_area", queue_size, min_duration, qos)
        self.objects = [24, 25, 26, 27, 28, 29]
        
        """
        
        """
        
        self._subscribers = {"yolo": self.create_subscription(BoundingBoxes, "/yolo", self.yolo_callback, qos)}
    
    def yolo_callback(self, msg: BoundingBoxes):
        self.reset()
        
        for box in msg.boxes:
            _ = self.queue.popleft()
            self.queue.append(box.cls)
            
        counts = sum([self.queue.count(o) for o in self.objects])
        
        if counts >= int(0.8*len(self.queue)):
            self.running = True
            self.last = time.time()
    
    def run(self):
        if self.running:
            pass