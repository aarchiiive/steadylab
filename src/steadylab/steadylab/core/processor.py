import sys

import cv2
import numpy as np
import torch

from typing import Any

sys.path.append("src/steadylab/steadylab")

from core.message import *


class Processor:
    def __init__(self, name) -> None:
        self.name = name
        self.gpu = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    def __call__(self, msg) -> Any:
        return msg

    def imshow(self, img : np.ndarray):
        cv2.imshow(self.name, img)
        cv2.waitKey(1)


class ImageProcessor(Processor):
    def __init__(self, name, vis=True) -> None:
        super().__init__(name)
        self._type = Image                           
        self.shape = (360, 640, 4)
        self.resize = False
        self.vis = vis
    
    def __call__(self, msg) -> np.ndarray:
        img = np.array(msg.data).reshape(self.shape) # RGBA
        img = cv2.resize(img, (1280, 720))
        if self.vis: self.imshow(img)
        del img
        return img


class DepthProcessor(Processor):
    def __init__(self, name, vis=True) -> None:
        super().__init__(name)
        self._type = Image
        self.shape = (360, 640, 4)
        self.vis = vis

    def __call__(self, msg):
        img = np.array(msg.data).reshape(self.shape)
        img = cv2.resize(img, (1280, 720))
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
        if self.vis: self.imshow(img)
        del img
        return img


class PoseProcessor(Processor):
    def __init__(self, name) -> None:
        super().__init__(name)
        self._type = PoseStamped

    def __call__(self, msg):
        # return {
        #     "pose" : msg.pose.position,
        #     "orientation" : msg.pose.orientation
        # }
    
        return msg
        

class PathMapProcessor(Processor):
    def __init__(self, name) -> None:
        super().__init__(name)
        self._type = Path

    def __call__(self, msg):
        # return {
        #     "header" : msg.header.stamp,
        #     "headers" : [p.header for p in msg.poses],
        #     "poses" : [p.pose for p in msg.poses],
        # }
    
        return msg
    

class PointCloudProcessor(Processor):
    def __init__(self, name, vis=True) -> None:
        super().__init__(name)
        self._type = PointCloud2
        self.shape = (360, 640, -1)
        self.vis = vis

    def __call__(self, msg):
        data = np.array(msg.data).reshape(self.shape)
        # print(np.shape(data))
        # print(data[0, 0, -3:])
        if self.vis: self.imshow(data[:, :, 3:6])
        # return msg.data
        return msg


class IMUProcessor(Processor):                                                                                     
    def __init__(self, name) -> None:
        super().__init__(name)
        self._type = Imu

    def __call__(self, msg):
        # return msg.header
        return msg


class TFProcessor(Processor):
    def __init__(self, name) -> None:
        super().__init__(name)
        self._type = TFMessage

    def __call__(self, msg):
        # return msg.transforms
        return msg