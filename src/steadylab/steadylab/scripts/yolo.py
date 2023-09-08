import os
import sys

import cv2
import numpy as np      
from cv_bridge import CvBridge  

import torch
from ultralytics import YOLO
from ultralytics.engine.results import Results

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8, Int16, Float32MultiArray, Float32

sys.path.append("src/steadylab/steadylab")

from msg import Boxes
from core.message import Image
from core.processor import ImageProcessor

class ObjectDetector(Node):
    def __init__(self, webcam=0, conf=0.6):
        super().__init__("yolo")
        self.qos_profile = 5
        self.shape = (360, 640, 4)
        self.conf = conf
        
        # self.yolo = YOLO("src/steadylab/steadylab/weights/traffic_lights/last.pt")
        self.yolo = YOLO("yolov8m.pt")
        self.processor = ImageProcessor("image", vis=False)
        self.cap = cv2.VideoCapture(webcam)
        self.bridge = CvBridge()
        
        self.timer = self.create_timer(0.1, self.timer_callback)
        self._subscriber = self.create_subscription(Image, "/image", self.callback, self.qos_profile)
        self._publishers = {
            "probs": self.create_publisher(Float32MultiArray, "/probs", 1), # [0.1, ... 0.56]
            "boxes": self.create_publisher(Float32MultiArray, "/boxes", 1), # [x, y, w, h]
        }

    def callback(self, msg):
        img = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgra8').astype(np.uint8)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        res = self.yolo.predict(img, conf=self.conf)[0]
        cv2.imshow("yolo", res.plot())
        cv2.waitKey(1)

    def timer_callback(self):
        _, frame = self.cap.read()
        res = self.yolo.predict(frame, conf=self.conf)[0].cpu().numpy()
        
        for b in res.boxes:
            cls = Int8()
            conf = Float32()
            xywh = Float32MultiArray()
            print(f"cls : {b.cls[0]}")
            print(f"conf : {b.conf[0]}")
            print(f"xywh : {b.xywh}")
            
        
        # self.publishers["probs"].publish(probs)
        # self.publishers["boxes"].publish(boxes)

        cv2.imshow("yolo", res.plot())
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
                                      
    yolo = ObjectDetector()
                                                                          
    rclpy.spin(yolo)

    yolo.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()