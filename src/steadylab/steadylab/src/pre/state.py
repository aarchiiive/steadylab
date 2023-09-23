from typing import Dict

import os
import sys

import cv2
import numpy as np
from cv_bridge import CvBridge   

import rclpy
from rclpy.node import Node

from steady_msgs.msg import ReadCar, WriteCar, BoundingBox, BoundingBoxes

sys.path.append("src/steadylab/steadylab")

from core.message import String, Bool, Int64
from planning.pre.driving_mode import DrivingMode


"""

# rubber_cone
{0: 'orange_cone', 1: 'large_orange_cone', 2: 'other_cone', 3: 'tg_arrow', 4: 'tg_cone', 5: 'tg_sign'}

"""
class State(Node):
    def __init__(self, 
                 qos: int = 5):
        super().__init__("state")
        self.qos = qos
        
        self.erp = WriteCar()
        self.objects = BoundingBoxes()
        
        self.driving_mode = DrivingMode.CRUISING
        
        self.speed = 60
        self.steer = Int64()
        self._steer = {"left": -1900, 
                       "straight": 0, 
                       "right": -1900}
        
        self._publishers = {"steer": self.create_publisher(Int64, "/control", qos)}
        self._create_subscribers()
        self.timer = self.create_timer(0.1, self.callback)
    
    def _create_subscribers(self):
        missions = ["cruising", "complex_area", "uturn", "tollgate", "tunnel", "general_obstacle", "static_obstacle", "dynamic_obstacle"]

        self._subscribers = {}
        self.missions = {}
        for m in missions:
            running = f"{m}"
            steer = f"{m}_steer"
            self._subscribers[running] = self.create_subscription(Bool, running, getattr(self, f"_{running}"), self.qos)
            self._subscribers[steer] = self.create_subscription(Int64, steer, getattr(self, f"_{steer}"), self.qos)
            self.missions[m] = {"running": False, "steer": 0}
            

    def callback(self):
        # self.update()
        # for k, v in self.missions.items():
        #     if k == "tollgate":
        #         print(f"{k} : {v}")
        self.steer.data = self.missions["cruising"]["steer"]
        print(self.steer)
        self._publishers["steer"].publish(self.steer)
    
    
    def process_steer(self, speed: int = None, steer: int = None):
        self.erp.write_speed = self.speed if speed is None else speed
        self.erp.write_steer = max(-1900, min(1900, steer))
    
    def combine_steer(self):
        pass
    
    def _cruising(self, msg: Bool):
        # Callback for complex_area topic
        self.missions["cruising"]["running"] = msg.data
        
    def _complex_area(self, msg: Bool):
        # Callback for complex_area topic
        self.missions["complex_area"]["running"] = msg.data

    def _uturn(self, msg: Bool):
        # Callback for uturn topic
        self.missions["uturn"]["running"] = msg.data

    def _tollgate(self, msg: Bool):
        # Callback for tollgate topic
        self.missions["tollgate"]["running"] = msg.data

    def _tunnel(self, msg: Bool):
        # Callback for tunnel topic
        self.missions["tunnel"]["running"] = msg.data

    def _general_obstacle(self, msg: Bool):
        # Callback for static_obstacle topic
        self.missions["general_obstacle"]["running"] = msg.data

    def _static_obstacle(self, msg: Bool):
        # Callback for static_obstacle topic
        self.missions["static_obstacle"]["running"] = msg.data

    def _dynamic_obstacle(self, msg: Bool):
        # Callback for dynamic_obstacle topic
        self.missions["dynamic_obstacle"]["running"] = msg.data

    def _cruising_steer(self, msg: Int64):
        # Callback for complex_area topic
        self.missions["cruising"]["steer"] = msg.data
        
    def _complex_area_steer(self, msg: Int64):
        # Callback for complex_area_steer topic
        self.missions["complex_area"]["steer"] = msg.data

    def _uturn_steer(self, msg: Int64):
        # Callback for uturn_steer topic
        self.missions["uturn"]["steer"] = msg.data

    def _tollgate_steer(self, msg: Int64):
        # Callback for tollgate_steer topic
        self.missions["tollgate"]["steer"] = msg.data

    def _tunnel_steer(self, msg: Int64):
        # Callback for tunnel_steer topic
        self.missions["tunnel"]["steer"] = msg.data

    def _general_obstacle_steer(self, msg: Int64):
        # Callback for static_obstacle_steer topic
        self.missions["general_obstacle"]["steer"] = msg.data
    
    def _static_obstacle_steer(self, msg: Int64):
        # Callback for static_obstacle_steer topic
        self.missions["static_obstacle"]["steer"] = msg.data

    def _dynamic_obstacle_steer(self, msg: Int64):
        # Callback for dynamic_obstacle_steer topic
        self.missions["dynamic_obstacle"]["steer"] = msg.data
    
    
def main(args=None):
    rclpy.init(args=args)
                                      
    state = State()
                                                                          
    rclpy.spin(state)

    state.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()