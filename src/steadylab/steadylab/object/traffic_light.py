from typing import Tuple

import sys
import time

from collections import deque

import rclpy
from rclpy.node import Node
from steady_msgs.msg import BoundingBox, BoundingBoxes

sys.path.append("src/steadylab/steadylab")

from core.message import Bool, Int8

class TrafficLight(Node):
    def __init__(self, 
                 queue_size: int = 5,
                 x_thres: Tuple[float, float] = (0.3, 0.7),
                 y_thres: Tuple[float, float] = (0, 0.15),
                 init_freq: int = 1,
                 qos: int = 5):
        super().__init__("traffic_light")
        
        self.queue_size = queue_size
        self.x_thres = x_thres
        self.y_thres = y_thres
        self.init_freq = init_freq
        self.queue = deque([None for _ in range(queue_size)])
        self.last_detected = time.time()
        
        self.msg = {"state": Int8()} # -1 : stop / 0 : straight / 1 : right / 2 : left
        self._publishers = {"state": self.create_publisher(Int8, "/traffic_state", qos)} 
        self._subscribers = {"yolo": self.create_subscription(BoundingBoxes, "/yolo", self.yolo_callback, qos)}
        
        self.timer = {"queue": self.create_timer(0.2, self.queue_callback),
                      "direction": self.create_timer(0.2, self.direction_callback)}
        
    def queue_callback(self):
        if time.time() - self.last_detected > self.init_freq:
            self.queue = deque([None for _ in range(self.queue_size)])
    
    def direction_callback(self):
        if None in self.queue:
            self.publish_state(0)
        
    def yolo_callback(self, msg: BoundingBoxes):
        for box in msg.boxes:
            _ = self.queue.popleft()
            cls, name, conf, xywh, xywhn = self.get_box_data(box)
            self.queue.append([name, xywhn])
            self.predict()
        
    def get_box_data(self, box: BoundingBox):
        return box.cls, box.name, box.conf, list(box.xywh), list(box.xywhn)
    
    def predict(self):
        if None not in self.queue:
            for data in self.queue:
                name, xywhn = data
                if "delivery" in name:
                    print("delivery")
                    pass
                else:
                    if self.x_thres[0] < xywhn[0] < self.x_thres[1] and \
                        self.y_thres[0] < xywhn[1] < self.y_thres[1]:
                        print(f"{name} closed")
                        if name == "4_red":
                            self.publish_state(-1)
                        elif name == "3_red": # TODO : 3 + location -> right, straight.....
                            self.publish_state(-1)
                        elif '4' in name: # TODO : 4 + location -> left, straight.....
                            self.publish_state(1)

                        self.last_detected = time.time()
                
    def publish_state(self, msg: int):
        self.msg["state"].data = msg
        self._publishers["state"].publish(self.msg["state"])
    
def main(args=None):
    rclpy.init(args=args)
                                      
    traffic_light = TrafficLight()
                                                                          
    rclpy.spin(traffic_light)

    traffic_light.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()