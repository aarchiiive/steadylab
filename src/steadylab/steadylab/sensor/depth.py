import sys

import cv2
import numpy as np   
from cv_bridge import CvBridge                                                                                                                        

import rclpy
from rclpy.node import Node

sys.path.append("src/steadylab/steadylab")

from messages.data_hub import data_hub_messages as msg
from core.message import Image

class Depth(Node):
    def __init__(self, qos: int = 5):
        super().__init__("depth")
        self._subscriber = {"depth": self.create_subscription(msg["depth"].msg_type, msg["depth"].topic, self.depth_callback, qos)}
        self.bridge = CvBridge()

    def depth_callback(self, msg: Image):
        depth = self.bridge.imgmsg_to_cv2(msg, desired_encoding='32FC1')
        depth[np.isnan(depth)] = 0
        depth[np.isinf(depth)] = 0
        raw_depth = depth

        # self.get_logger().info(f"mean depth : {np.mean(raw_depth):.4f}")

        cv2.imshow("depth", np.clip(depth*10, 0, 255).astype(np.uint8))
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
                                      
    subscriber = Depth()
                                                                          
    rclpy.spin(subscriber)

    subscriber.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()