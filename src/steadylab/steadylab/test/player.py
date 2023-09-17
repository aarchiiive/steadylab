import sys

import cv2
import numpy as np
from cv_bridge import CvBridge

import rclpy
from rclpy.node import Node

sys.path.append("src/steadylab/steadylab")

from core.message import Image

class Player(Node):
    def __init__(self,
                 video_path: str = "src/steadylab/videos/final.mp4",
                 time_period: float = 0.005,
                 qos: int = 5):
        super().__init__("player")
        
        self._publishers = {"image": self.create_publisher(Image, "/image", qos)}
        self.timer = self.create_timer(time_period, self.callback)
        
        self.bridge = CvBridge()
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)
        
    def callback(self):
        _, img = self.cap.read()
        img = cv2.resize(img, (640, 360))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
        img = self.bridge.cv2_to_imgmsg(img, encoding='bgra8')
        self._publishers["image"].publish(img)
        
def main(args=None):
    # args = parse_args()
    
    rclpy.init(args=args)
                                      
    player = Player()
                                                                          
    rclpy.spin(player)

    player.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()