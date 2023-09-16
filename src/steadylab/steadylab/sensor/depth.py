import sys

import cv2
import numpy as np   
from cv_bridge import CvBridge                                                                                                                        

import rclpy
from rclpy.node import Node

sys.path.append("src/steadylab/steadylab")

from messages.data_hub import data_hub_messages as msg

class Depth(Node):
    def __init__(self):
        super().__init__("depth")
        self.qos_profile = 5
        self._subscriber = self.create_subscription(msg["depth"].msg_type,
                                                    msg["depth"].topic,
                                                    self.depth_callback,
                                                    self.qos_profile)
        self.bridge = CvBridge()
        self.shape = (360, 640, 4)

    def depth_callback(self, msg):
        # self.depth = np.array(msg.data).reshape(self.shape)
        # self.depth = cv2.cvtColor(self.depth, cv2.COLOR_RGBA2GRAY)
        # self.depth = 255 - self.depth
        depth = self.bridge.imgmsg_to_cv2(msg, desired_encoding='32FC1')
        depth[np.isnan(depth)] = 0
        depth[np.isinf(depth)] = 0

        raw_depth = depth
        depth = np.clip(depth*10, 0, 255)

        # self.get_logger().info(f"mean depth : {np.mean(raw_depth):.4f}")

        cv2.imshow("depth", depth.astype(np.uint8))
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