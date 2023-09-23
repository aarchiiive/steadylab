import sys
import time

from collections import deque

import rclpy
from rclpy.node import Node

import cv2
import numpy as np
from cv_bridge import CvBridge   

from shapely import Point   
from shapely.geometry.polygon import Polygon

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
class Tollgate(Mission):
    def __init__(self, 
                 queue_size: int = 5,
                 min_duration: float = 4.0,
                 qos: int = 5):
        super().__init__("tollgate", queue_size, min_duration, qos)
        w, h = (640, 360)
        p, q = (0.42, 0.2)
        m, n = (0.7, 1.0)
        self.points = [(int(w*p), int(h*m)),
                       (int(w*(1 - p)), int(h*m)),
                       (int(w*(1 - q)), h*n),
                       (int(w*q), h*n),]
        self.polygon = Polygon(self.points)
        
        self.thres = 4.0
        self.bridge = CvBridge()
        
        self.classes = {
            "hipass": 2,
            "tollgate_box": 12,
            "tollgate_sign": 13,
            "tublar_marker": 14,
        }
        
        self.objects = [0, 2, 12, 13, 14]
        self.markers = {
            "left": [],
            "right": [],
        }
        
        self._publishers = {"steer": self.create_publisher(Int64, "/tollgate_steer", qos),
                            "running": self.create_publisher(Bool, "/tollgate", qos)}
        self._subscribers = {"yolo": self.create_subscription(BoundingBoxes, "/yolo", self.yolo_callback, qos)}
        
        self.timer = self.create_timer(0.1, self.callback)
    
    def callback(self):
        steer, running = Int64(data=self.steer), Bool(data=self.running)
        self._publishers["steer"].publish(steer)
        self._publishers["running"].publish(running)
    
    def yolo_callback(self, msg: BoundingBoxes):
        self.reset()
        if self.running:
            classes = []
            xywhns = []
            # for box in msg.boxes:
            #     if box.cls == self.classes["tublar_marker"]:
        
        else:
            for box in msg.boxes:
                _ = self.queue.popleft()
                self.queue.append(box.cls)
                
            counts = sum([self.queue.count(o) for o in self.objects])
            
            if counts >= int(0.8*len(self.queue)):
                self.running = True
                self.last = time.time()
                
    # def depth_callback(self, msg: Image):
    #     depth = self.bridge.imgmsg_to_cv2(msg, desired_encoding='32FC1')
    #     depth[np.isnan(depth)] = 0
    #     depth[np.isinf(depth)] = 0
    #     raw_depth = depth
        
    #     y, x = np.where((0 < raw_depth) & (raw_depth < self.thres))
        
    #     # visualize
    #     depth = np.clip(depth*20, 0, 255).astype(np.uint8)
    #     depth = cv2.cvtColor(depth, cv2.COLOR_GRAY2BGR)
        
    #     for xi, yi in zip(x, y):
    #         if not self.polygon.contains(Point(xi, yi)):
    #             cv2.circle(depth, (xi, yi), 1, (120, 50, 0), 1)
                
    #     cv2.polylines(depth, [np.array(self.points, dtype=np.int32)], True, (0, 50, 180), 8, lineType=cv2.LINE_8)
    #     cv2.imshow("obstacle", depth)
    #     cv2.waitKey(1)
        
    def reset(self):
        self.markers = {
            "left": [],
            "right": [],
        }
        print(time.time() - self.last)
        if time.time() - self.last > self.min_duration and self.running: 
            self.running = False
            self.queue = deque([None for _ in range(self.queue_size)])

        if not self.running: self.last = time.time()
            
        
def main(args=None):
    rclpy.init(args=args)
                                      
    node = Tollgate()
                                                                          
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()
    
    return node

if __name__ == "__main__":
    main()