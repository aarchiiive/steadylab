import sys

sys.path.append("src/steadylab/steadylab")

from core.message import Message
from core.processor import *

data_hub_messages = {
    "image": Message(
        name="image",
        topic="/image", 
        msg_type=Image,
        processor=ImageProcessor("image"),
    ),

    "depth": Message(
        name="depth",
        topic="/depth", 
        msg_type=Image,
        processor=DepthProcessor("depth"),
    ),

    "pose": Message(
        name="pose",
        topic="/pose", 
        msg_type=PoseStamped,
        processor=PoseProcessor("pose"),
    ),

    "path_map": Message(
        name="path_map",
        topic="/path_map", 
        msg_type=Path,
        processor=PathMapProcessor("path_map"),
    ),

    "pointcloud": Message(
        name="pointcloud",
        topic="/pointcloud", 
        msg_type=PointCloud2,
        processor=PointCloudProcessor("pointcloud"),
    ),

    "imu": Message(
        name="imu",
        topic="/imu", 
        msg_type=Imu,
        processor=IMUProcessor("imu"),
    ),
    
    "tf": Message(
        name="tf",
        topic="/tf", 
        msg_type=TFMessage,
        processor=TFProcessor("tf"),
    ),
}