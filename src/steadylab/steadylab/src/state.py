import os
import sys

import numpy as np
from cv_bridge import CvBridge   

import rclpy
from rclpy.node import Node

from steady_msgs.msg import ReadCar, WriteCar, BoundingBox, BoundingBoxes
from sensor_msgs.msg import Image

"""

# rubber_cone
{0: 'orange_cone', 1: 'large_orange_cone', 2: 'other_cone', 3: 'tg_arrow', 4: 'tg_cone', 5: 'tg_sign'}


"""
class State(Node):
    def __init__(self, qos=1):
        super().__init__("state")
        self.size = (640, 360)
        self.steer_amount = {"left": -100 ,
                             "right": 100}
        self.window = [1/8, 2/8, 3/8, 4/8, 5/8, 6/8, 7/8, 1]
        self.ratio = [0.9, 0.75, 0.6, 0.45, 0.4, 0.3, 0.2, 0]
        self.init_ratio = 0.2
        self.thres = [2.0, 4.0] # rubber cone u-turn
        self.bridge = CvBridge()

        self.start = False
        self.finish = False
        self.speed = 50
        self.steer = 0
        self.erp = WriteCar()

        self._subscribers = {"yolo": self.create_subscription(BoundingBoxes, "/yolo", self.yolo_callback, qos),
                             "depth": self.create_subscription(Image, "/depth", self.depth_callback, qos)}
        self._publishers = {"steer": self.create_publisher(WriteCar, "/car_control", qos)}
        
        self.timer = {"steer": self.create_timer(0.5, self.steer_callback)}
        self.box = {"center": (0, 0),
                    "depth:": 0,
                    "points": None,
                    "count": 0}
        self.raw_depth = None

    def yolo_callback(self, msg):
        cls, conf, x, y, w, h = msg.data
        # self.get_logger().info(f"cls : {cls}")

        if not self.finish:
            if int(cls) in [0, 1]: # and w > self.size[0] * 0.1:
                if not self.start: 
                    points = [(a, b) for a in np.arange(x, x + w) for b in np.arange(y, y + h)]
                    self.box["center"] = (x // 2, y // 2)
                    if self.raw_depth is not None and int(cls) == 0: 
                        mean_depth = self.raw_depth[int(x // 2), int(y // 2)]
                        self.get_logger().info(f"center : {mean_depth}")
                    if x < self.size[0] * 0.5 and int(cls) == 0 and self.thres[0] < mean_depth < self.thres[1]:
                        self.start = True
                else:
                    # self.get_logger().info(f"width : {w} height : {h}")
                    for i, r in enumerate(self.ratio):
                        if x < self.size[0] * self.window[i]:
                            self.steer += int(self.steer_amount["right"] * r)

                self.box["count"] += 1

    def depth_callback(self, msg):
        depth = self.bridge.imgmsg_to_cv2(msg, desired_encoding='32FC1')
        depth[np.isnan(depth)] = 0
        depth[np.isinf(depth)] = 0

        self.raw_depth = depth
        depth = np.clip(depth*10, 0, 255)

    def steer_callback(self):
        # self.get_logger().info(f"speed : {self.speed}")
        # self.get_logger().info(f"steer : {self.steer}")
        self.erp.write_speed = self.speed
        self.erp.write_steer = max(-1900, min(1900, self.steer))
        self._publishers["steer"].publish(self.erp)
        self.steer = int(self.steer * self.init_ratio)
        if self.finish: print("FINISH!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        if self.box["count"] == 0 and self.steer < 10:
            self.finish = True

        self.box["count"] = 0
        

def main(args=None):
    rclpy.init(args=args)
                                      
    state = State()
                                                                          
    rclpy.spin(state)

    state.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()