import sys

sys.path.append("src/steadylab/steadylab")

from core.message import Message
from core.processor import *

zed_messages = {
    "image": Message(
        name="image",
        topic="/zed2i/zed_node/rgb/image_rect_color", 
        msg_type=Image,
        processor=ImageProcessor("image"),
        device="zed",
    ),

    "depth": Message(
        name="depth",
        topic="/zed2i/zed_node/depth/depth_registered", 
        msg_type=Image,
        processor=DepthProcessor("depth"),
        device="zed",
    ),

    "pose": Message(
        name="pose",
        topic="/zed2i/zed_node/pose", 
        msg_type=PoseStamped,
        processor=PoseProcessor("pose"),
        device="zed",
    ),

    "path_map": Message(
        name="path_map",
        topic="/zed2i/zed_node/path_map", 
        msg_type=Path,
        processor=PathMapProcessor("path_map"),
        device="zed",
    ),

    "pointcloud": Message(
        name="pointcloud",
        topic="/zed2i/zed_node/point_cloud/cloud_registered", 
        msg_type=PointCloud2,
        processor=PointCloudProcessor("pointcloud"),
        device="zed",
    ),

    "imu": Message(
        name="imu",
        topic="/zed2i/zed_node/imu/data", 
        msg_type=Imu,
        processor=IMUProcessor("imu"),
        device="zed",
    ),
    
    "tf": Message(
        name="tf",
        topic="/tf", 
        msg_type=TFMessage,
        processor=TFProcessor("tf"),
        device="zed",
    ),
}