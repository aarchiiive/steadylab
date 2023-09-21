import sys

from collections import deque

import cv2
import numpy as np
from cv_bridge import CvBridge  

import torch
import torch.nn as nn

import rclpy
from rclpy.node import Node

sys.path.append("src/steadylab/steadylab")

from core.message import String, Image, Int16

class Place(Node):
    def __init__(self,
                 queue_size: int = 4,
                 device: str = "cpu",
                 qos: int = 5):
        super().__init__("place")
        # self.classes = {0: "", ### TODO 
        #                 0: "",
        #                 0: "",
        #                 0: "",
        #                 0: "",
        #                 0: "",}
        # self.num_classes = len(self.classes) ### TODO 
        self.num_classes = 12
        
        self.queue = deque([None for _ in range(queue_size)])
        self.current = ""
        self.device = torch.device(device)
        
        state_dict = torch.load("src/steadylab/weights/place/best.pt")
        self.model = torch.hub.load('pytorch/vision:v0.10.0', 'resnet34', pretrained=True)
        self.model.fc = nn.Linear(self.model.fc.in_features, self.num_classes)
        self.model.load_state_dict(state_dict['model'])
        self.model.to(self.device)
        self.model.eval()
        
        self.bridge = CvBridge()
        # self.place = String()
        self.place = Int16()
        
        self._publishers = {"place": self.create_publisher(Int16, "/place", qos)}
        self._subscribers = {"image": self.create_subscription(Image, "/image", self.image_callback, qos)}
        
        self.timer = self.create_timer(0.2, self.callback)
        
    def image_callback(self, msg: Image):
        img = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgra8').astype(np.uint8)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        img = cv2.resize(img, (256, 256))
        
        with torch.no_grad():
            inputs = torch.from_numpy(img).permute(2, 0, 1).unsqueeze(0).to(self.device)
            outputs = torch.sigmoid(self.model(inputs))
            _, preds = torch.max(outputs, 1)
            # self.current = self.classes[int(preds)]
            self.current = int(preds)
            
    def callback(self):
        self.place.data = self.current
        self._publishers["place"].publish(self.place)        
    
    
def main(args=None):
    rclpy.init(args=args)
                                      
    place = Place()
                                                                          
    rclpy.spin(place)

    place.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()