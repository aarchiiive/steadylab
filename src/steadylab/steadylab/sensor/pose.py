import sys

from collections import deque

import rclpy
from rclpy.node import Node

sys.path.append("src/steadylab/steadylab")

from core.message import Path, PoseStamped, Imu


class Pose(Node):
    def __init__(self, qos=5):
        super().__init__("pose")
        self.queue = deque([0 for _ in range(10)])
        self._subscribers = {"path_map": self.create_subscription(Path, "/path_map", self.path_map_callback, qos),
                             "imu": self.create_subscription(Path, "/imu", self.imu_callback, qos)}
        
        self.pose = {'x': 0, 'y': 0}
        self.quaternion = {'x': 0, 'y': 0, 'z': 0, 'w': 0}
        
    def path_map_callback(self, msg: Path):
        pose_stamped: PoseStamped = msg.poses[-1]
        orientation = pose_stamped.pose.orientation
        self.pose['x'] = pose_stamped.pose.position.x
        self.pose['y'] = pose_stamped.pose.position.y
        
        self.quaternion['x'] = pose_stamped.pose.orientation.x
        self.quaternion['y'] = pose_stamped.pose.orientation.y
        self.quaternion['z'] = pose_stamped.pose.orientation.z
        self.quaternion['w'] = pose_stamped.pose.orientation.w
        
        print("[Pose]")        
        for k, v in self.pose.items():
            print(f"{k} : {v}")
            
        print("[Quaternion]")        
        for k, v in self.quaternion.items():
            print(f"{k} : {v}")
        
        # self.get_logger().log()
        
    def imu_callback(self, msk: Imu):
        pass

def main(args=None):
    rclpy.init(args=args)
                                      
    pose = Pose()
                                                                          
    rclpy.spin(pose)

    pose.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()