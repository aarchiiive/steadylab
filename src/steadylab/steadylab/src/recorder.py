import os
import sys
import datetime

import cv2
import numpy as np
from cv_bridge import CvBridge 

import rclpy
from rclpy.node import Node

sys.path.append("src/steadylab/steadylab")

from core.message import Image, Int16
from core.processor import ImageProcessor

class Recorder(Node):
    def __init__(self, qos: int = 5):
        super().__init__("recorder")
        self.current_time = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
        self.save_path = os.path.join("record", self.current_time)
        
        os.makedirs(self.save_path, exist_ok=True)
        
        self.bridge = CvBridge()
        self._subscribers = {"image": self.create_subscription(Image, "/image", self.image_callback, qos)}

    def image_callback(self, msg: Image):
        img = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgra8').astype(np.uint8)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        filename = os.path.join(self.save_path, f"{len(os.listdir(self.save_path)):06d}.jpg")
        cv2.imwrite(filename, img)
        
def main(args=None):
    rclpy.init(args=args)
                                      
    recorder = Recorder()
                                                                          
    rclpy.spin(recorder)

    recorder.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()