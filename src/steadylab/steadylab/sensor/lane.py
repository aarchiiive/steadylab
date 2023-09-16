from typing import Dict, Sequence

import os
import sys

import cv2
import numpy as np
from cv_bridge import CvBridge 

import torch

import rclpy
from rclpy.node import Node

sys.path.append("src/steadylab/steadylab")

from core.mode import Mode
from core.message import Image, Int64
from utils.parser import parse_args 
from utils.lane import *

class Lane(Node):
    def __init__(self, 
                 imgsz: int = 256, 
                 conf_thres: float = 0.3,
                 iou_thres: float = 0.45,
                 qos: int = 5, 
                 frame_rate: int = 10,
                 mode: str = "auto", 
                 fp16: bool = True):
        super().__init__("lane")
        self.frame_rate = frame_rate
        self.imgsz = (imgsz, imgsz)
        self.conf_thres = conf_thres
        self.iou_thres = iou_thres
        self.gn = None
        self.grid_size = 11
        self.grid_range = {"left": (6,10,3,4),
                           "light_left": (6,10,2,3),
                           "right": (6,10,7,8),
                           "light_right": (6,10,7,8)}
        
        self.bridge = CvBridge()
        self.model = torch.jit.load("src/steadylab/weights/lane/yolopv2.pt")
        self.device = torch.device("cuda:0")
        self.model = self.model.to(self.device).eval()
        self.fp16 = fp16
        
        if fp16: self.model.half()
        
        self.steer = 0
        self.steers = {"left": -1200,
                       "right": 1200,
                       "straight": 0}
        self.directions = ["left", "light_left", "right", "light_right"]
        
        self._publishers = {"center": self.create_publisher(Int64, "/center", qos),
                            "steer": self.create_publisher(Int64, "/lane_steer", qos),}
        self._subscribers = {"image": self.create_subscription(Image, "/image", self.image_callback, qos)}
        
        if mode == "auto":
            self.mode = Mode.Auto
        elif mode == "test":
            self.mode = Mode.Test
            self.video = "src/steadylab/videos/pre.mp4"
            self.cap = cv2.VideoCapture(self.video)
            self.timer = self.create_timer(0.01, self.callback)
            
        # self.get_logger().info(self.mode)
            
    def callback(self):
        if self.mode == Mode.Auto:
            pass
        elif self.mode == Mode.Test:
            for _ in range(self.frame_rate):
                _, frame = self.cap.read()
                        
            res = self.infer(frame)
            
            cv2.imshow("lane", res)
            cv2.waitKey(1)
            
    def image_callback(self, msg: Image):
        # if self.mode == Mode.Auto:
        img = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgra8').astype(np.uint8)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        res = self.infer(img)
        
        cv2.imshow("lane", res)
        cv2.waitKey(1)
        
    def infer(self, img: np.ndarray):
        with torch.no_grad():
            im = self.resize(img)
            (preds, grid), seg, lane = self.model(im)
            preds = split_for_trace_model(preds, grid)
            preds = non_max_suppression(preds, self.conf_thres, self.iou_thres)
            mask = self.get_mask(seg, lane)
            
            self.predict(mask)
            # self.visualize(lane)

            # xywh = self.detect(img, preds)
            # show_seg_result(img, (mask["driving_area"], mask["left"], mask["right"]), img_shape=img.shape[:2], is_demo=True)
            
            return draw_grid(img, self.grid_size)
            
    def resize(self, img: np.ndarray) -> torch.Tensor:
        img = cv2.resize(img, self.imgsz)
        img = torch.from_numpy(img).permute(2, 0, 1).float().div(255.0).unsqueeze(0).to(self.device)
        
        if self.fp16:
            return img.half()
        else:
            return img
        
    def detect(self, img: np.ndarray, preds: torch.Tensor):
        if not self.gn: self.gn = torch.tensor(img.shape)[[1, 0, 1, 0]]
        for det in preds:
            if len(det):
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], img.shape).round()
                
                for *xyxy, _, _ in reversed(det):
                    xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / self.gn).view(-1).tolist()
        
        return xywh
    
    def predict(self, mask: Dict[str, np.ndarray]):
        empty = {x: self.is_empty(mask[x]) for x in self.directions}

        if not empty["left"] and empty["right"]:
            self.steer = self.steers["right"]
        elif empty["left"] and not empty["right"]:
            self.steer = self.steers["left"]
        elif not empty["light_left"]:
            self.steer = self.steers["right"] // 2
        else:
            self.steer = self.steers["straight"]
        
        self.print_steer()
        
    def is_empty(self, mask: torch.Tensor):
        return mask.sum() == 0

    def print_steer(self):
        if self.steer < 0:
            print(f"left {self.steer}")
        elif self.steer > 0:
            print(f"right {self.steer}")
        else:
            print(f"straight {self.steer}")

    def get_mask(self, seg: torch.Tensor, lane: torch.Tensor):
        return {"driving_area": driving_area_mask(seg),
                "left": lane_line_mask(lane, self.grid_size, self.grid_range["left"]),
                "light_left": lane_line_mask(lane, self.grid_size, self.grid_range["light_left"]),
                "right": lane_line_mask(lane, self.grid_size, self.grid_range["right"]),
                "light_right": lane_line_mask(lane, self.grid_size, self.grid_range["light_right"])}
        
    def visualize(self, img: torch.Tensor) -> None:
        print(img.shape)
        img = img.squeeze(0).permute(1, 2, 0).detach().cpu().numpy().astype(np.uint8)
        cv2.imshow("binary", img)
    
def main(args=None):
    # args = parse_args()
    
    rclpy.init(args=args)
                                      
    lane = Lane()
                                                                          
    rclpy.spin(lane)

    lane.destroy_node()
    rclpy.shutdown()
    
    lane.cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()