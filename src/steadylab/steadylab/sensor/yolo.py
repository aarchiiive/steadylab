import sys

import cv2
import numpy as np      
from cv_bridge import CvBridge  

import array
from ultralytics import YOLO
from ultralytics.engine.results import Results, Boxes

import rclpy
from rclpy.node import Node
from steady_msgs.msg import BoundingBox, BoundingBoxes

sys.path.append("src/steadylab/steadylab")

from core.message import Image, Int16
from core.processor import ImageProcessor

"""
[traffic_lights]
{0: '4_green', 1: '4_red', 2: '4_yellow', 3: '4_green_left', 
4: '4_red_left', 5: '4_green_yellow', 6: '3_green', 7: '3_red', 
8: '3_yellow', 9: '3_green_left', 10: '3_red_left', 
11: 'delivery_a1', 12: 'delivery_a2', 13: 'delivery_a3', 
14: 'delivery_b1', 15: 'delivery_b2', 16: 'delivery_b3'}

[rubber_cone]
{0: 'orange_cone', 1: 'large_orange_cone', 2: 'other_cone', 3: 'tg_arrow', 4: 'tg_cone', 5: 'tg_sign'}

"""

class Object(Node):
    def __init__(self, webcam: int = 0, qos: int = 5, conf: float = 0.8):
        super().__init__("yolo")
        self.conf = conf
        
        self.classes = None
        self.left_indexes = list(range(6)) # traffic_mode

        self.yolo = YOLO("src/steadylab/weights/traffic_lights/last.pt")
        # self.yolo = YOLO("src/steadylab/weights/rubber_cone/best.pt")
        
        self.bridge = CvBridge()
        
        self.msg = {"bboxes": BoundingBoxes()}
        self._publishers = {"yolo": self.create_publisher(BoundingBoxes, "/yolo", qos)} # [cls, conf, x, y, w, h]
        self._subscribers = {"image": self.create_subscription(Image, "/image", self.image_callback, qos)}
        
    def image_callback(self, msg: Image):
        img = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgra8').astype(np.uint8)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        results = self.yolo.predict(img, imgsz=640, conf=self.conf, half=True)
        
        if self.classes is None: self.classes = results[0].names

        for res in results:
            bboxes = []
            for b in res.boxes:
                bbox = BoundingBox()
                bbox.cls = int(b.cls[0])
                bbox.name = results[0].names[bbox.cls]
                bbox.conf = b.conf[0].item()
                bbox.xywh = array.array('f', b.xywh[0].detach().cpu().numpy())
                bbox.xywhn = array.array('f', b.xywhn[0].detach().cpu().numpy())
                bboxes.append(bbox)

            self.msg["bboxes"].boxes = bboxes
            self._publishers["yolo"].publish(self.msg["bboxes"])

        cv2.imshow("yolo", results[0].plot())
        cv2.waitKey(1)

def main(args=None):
    rclpy.init(args=args)
                                      
    yolo = Object()
                                                                          
    rclpy.spin(yolo)

    yolo.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()