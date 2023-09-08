import sys

import cv2
import numpy as np   
from cv_bridge import CvBridge                                                                                                                        
import torch

import rclpy
from rclpy.node import Node

sys.path.append("src/steadylab/steadylab")

from messages.data_hub import data_hub_messages as msg
from core.message import Image
from core.processor import ImageProcessor

class Depth(Node):
    def __init__(self):
        super().__init__("yolo")
        self.shape = (360, 640, 4)
        self._shape = (360, 640, 3)
        
        self.qos_profile = 5
        self.sub_modules = {}
        for n in ["image", "depth", "pointcloud"]:
            self.sub_modules[n] = self.create_subscription(
                msg[n].msg_type, 
                msg[n].topic, 
                getattr(self, f"{n}_callback"), 
                self.qos_profile
            )

        self.image = np.zeros(self._shape)
        self.depth = np.zeros(self._shape)
        
        self.bridge = CvBridge()

    def image_callback(self, msg):
        self.image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgra8').astype(np.uint8)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGRA2BGR)
        cv2.imshow("image", self.image)
        cv2.waitKey(1)

    def depth_callback(self, msg):
        self.depth = self.bridge.imgmsg_to_cv2(msg, desired_encoding='32FC1')
        # self.depth = np.nan_to_num(self.depth, nan=0.0)
        # # self.depth = np.where(np.isinf(self.depth), 0.0, self.depth)
        # self.depth[self.depth < 0] = 0.0
        # self.depth[self.depth > 100000] = 0.0

        # print(self.depth)
        # print("="*50)
        # print(np.mean(self.depth))
        # print(np.min(self.depth))
        # print(np.max(self.depth))
        # print("="*50)

        cv2.imshow("depth", self.depth.astype(np.uint8))
        cv2.waitKey(1)

        # self.depth = (self.depth / np.max(self.depth) * 255).astype(np.uint8)
        # # i = np.unravel_index(np.argmax(self.depth), self.depth.shape)
        # # print(np.max(self.depth))
        # # depth_colored = cv2.applyColorMap(self.depth, cv2.COLORMAP_JET)
        # # self.depth = cv2.addWeighted(self.image, 0.4, depth_colored, 0.6, 0) 
        # # cv2.circle(self.depth, i, 10, (0, 0, 255), -1)
        # cv2.imshow("depth", self.depth)
        # # cv2.imshow("overlap", depth_colored)
        # cv2.waitKey(1)

    def pointcloud_callback(self, msg):
        pcl = np.array(msg.data).reshape(360, 640, -1) # [:,:,-4:]

        # B G R A
        res = np.concatenate((
            np.concatenate((pcl[:,:,0], pcl[:,:,4], pcl[:,:,8], pcl[:,:,12]), axis=0),
            np.concatenate((pcl[:,:,1], pcl[:,:,5], pcl[:,:,9], pcl[:,:,13]), axis=0),
            np.concatenate((pcl[:,:,2], pcl[:,:,6], pcl[:,:,10], pcl[:,:,14]), axis=0),
            np.concatenate((pcl[:,:,3], pcl[:,:,7], pcl[:,:,11], pcl[:,:,15]), axis=0),
        ), axis=1)

        color = np.concatenate((
            pcl[:,:,:3], pcl[:,:,4:7], pcl[:,:,8:11] , pcl[:,:,12:15] 
        ), axis=1)

        color = (cv2.applyColorMap(color.astype(np.uint8), cv2.COLORMAP_JET) * 0.9).astype(np.uint8)
        res = (cv2.applyColorMap(res.astype(np.uint8), cv2.COLORMAP_JET) * 0.9).astype(np.uint8)
        
        res = np.concatenate((res, color), axis=0)
        h, w, _ = np.shape(res)
        res = cv2.resize(res, (int(w * 0.6), int(h * 0.6)))
        cv2.imshow("poitncloud(16ch)", res)
        cv2.imshow("pcl", pcl[:,:,-4:])
        cv2.waitKey(1)
        print(np.array(msg.data).reshape(360, 640, -1).shape)




def main(args=None):
    rclpy.init(args=args)
                                      
    subscriber = Depth()
                                                                          
    rclpy.spin(subscriber)

    subscriber.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()