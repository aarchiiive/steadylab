import os
import sys

import cv2
import numpy as np      
from cv_bridge import CvBridge  

import array
import torch
from ultralytics import YOLO
from ultralytics.engine.results import Results

import rclpy 
from rclpy.node import Node
from steady_msgs.msg import BoundingBox, BoundingBoxes

sys.path.append("src/steadylab/steadylab")

from core.message import Int16
from core.processor import ImageProcessor

    
class Object(Node):
    def __init__(self, webcam=1, qos=5, conf=0.6):
        super().__init__("test_yolo")
        self.webcam = webcam
        self.conf = conf
        
        self.classes = None
        self.left_indexes = list(range(6)) # traffic_mode

        self.bridge = CvBridge()
        self.processor = ImageProcessor("image", vis=False)
        self.cap = cv2.VideoCapture(webcam)

        self.yolo = YOLO("yolov8n.pt") # for test
        
        # self._subscribers = {"image": self.create_subscription(Image, "/image", self.callback, qos)}
        self._publishers = {"yolo": self.create_publisher(BoundingBoxes, "/yolo", qos), # [cls, conf, x, y, w, h]
                            "direction": self.create_publisher(Int16, "/direction", qos),} # right : -1, straight : 0, left : 1
        
        # for test
        self.timer = self.create_timer(0.1, self.test_callback) 
    
    def test_callback(self):
        # img = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgra8').astype(np.uint8)
        _, img = self.cap.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        results = self.yolo.predict(img, imgsz=640, conf=self.conf)
        if self.classes is None: self.classes = results[0].names

        for res in results:
            msg = BoundingBoxes()
            bboxes = []
            for b in res.boxes:
                bbox = BoundingBox()
                bbox.cls = int(b.cls[0])
                bbox.name = results[0].names[bbox.cls] 
                bbox.conf = b.conf[0].item()
                bbox.xywh = array.array('f', b.xywh[0].detach().cpu().numpy())
                
                bboxes.append(bbox)

            msg.boxes = bboxes
            self._publishers["yolo"].publish(msg)

        cv2.imshow("yolo", results[0].plot())
        cv2.waitKey(1)


def main(args=None):
    rclpy.init(args=args)
                                      
    yolo = Object()
                                                                          
    rclpy.spin(yolo)

    yolo.destroy_node()
    rclpy.shutdown()
    # cv2.destroyAllWindows()


if __name__ == "__main__":
    main()