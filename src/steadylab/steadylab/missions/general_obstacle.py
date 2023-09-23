import sys

import cv2
import numpy as np   
from cv_bridge import CvBridge   

from shapely import Point   
from shapely.geometry.polygon import Polygon

import rclpy
from rclpy.node import Node

sys.path.append("src/steadylab/steadylab")

from core.message import Image, Int64


class GeneralObstacle(Node):
    def __init__(self, qos: int = 5):
        super().__init__("general_obstacle")
        self.w, self.h = (640, 360)
        p, q = (0.42, 0.2)
        m, n = (0.7, 1.0)
        self.points = [(int(self.w*p), int(self.h*m)),
                       (int(self.w*(1 - p)), int(self.h*m)),
                       (int(self.w*(1 - q)), self.h*n),
                       (int(self.w*q), self.h*n),]
        self.inner = Polygon(self.points)
        
        self.thres = 4.0
        
        self.bridge = CvBridge()
        self._publishers = {"steer": self.create_publisher(Int64, "/obstacle_steer", qos)}
        self._subscriber = {"depth": self.create_subscription(Image, "/depth", self.depth_callback, qos)}
    
    def depth_callback(self, msg: Image):
        depth = self.bridge.imgmsg_to_cv2(msg, desired_encoding='32FC1')
        depth[np.isnan(depth)] = 0
        depth[np.isinf(depth)] = 0
        raw_depth = depth
        
        y, x = np.where((0 < raw_depth) & (raw_depth < self.thres))
        
        # visualize
        depth = np.clip(depth*20, 0, 255).astype(np.uint8)
        depth = cv2.cvtColor(depth, cv2.COLOR_GRAY2BGR)
        
        for xi, yi in zip(x, y):
            if not self.polygon.contains(Point(xi, yi)):
                cv2.circle(depth, (xi, yi), 1, (120, 50, 0), 1)
            
        # for xi, yi  in zip(self.points_set[1], self.points_set[0]):
        #     cv2.circle(depth, (xi, yi), 1, (10, 120, 50), 2)
        
        cv2.polylines(depth, [np.array(self.points, dtype=np.int32)], True, (0, 50, 180), 8, lineType=cv2.LINE_8)
        cv2.imshow("general_obstacle", depth)
        cv2.waitKey(1)
        
        
def main(args=None):
    rclpy.init(args=args)
                                      
    general_obstacle = GeneralObstacle()
                                                                          
    rclpy.spin(general_obstacle)

    general_obstacle.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()