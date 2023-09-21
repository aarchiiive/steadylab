from typing import Dict

import os
import sys

import numpy as np
from cv_bridge import CvBridge   

import rclpy
from rclpy.node import Node

from steady_msgs.msg import ReadCar, WriteCar, BoundingBox, BoundingBoxes

sys.path.append("src/steadylab/steadylab")

from core.message import String
from missions.mission import Mission
from missions.cruising import Cruising
from missions.right_turn import RightTurn
from missions.complex_area import ComplexArea
from missions.uturn import UTurn
from missions.tollgate import Tollgate
from missions.tunnel import Tunnel
from missions.static_obstacle import StaticObstacle
from missions.dynamic_obstacle import DynamicObstacle
from planning.pre.driving_mode import DrivingMode

"""

# rubber_cone
{0: 'orange_cone', 1: 'large_orange_cone', 2: 'other_cone', 3: 'tg_arrow', 4: 'tg_cone', 5: 'tg_sign'}

"""
class State(Node):
    def __init__(self, 
                 qos: int = 5):
        super().__init__("state")
        self.erp = WriteCar()
        self.objects = BoundingBoxes()
        self.driving_mode = DrivingMode.CRUISING
        self.speed = 60
        self.steer = 0
        self._steer = {"left": -1900, 
                       "straight": 0, 
                       "right": -1900}
        
        self.missions: Dict[DrivingMode, Mission] = {DrivingMode.CRUISING: Cruising(),
                                                     DrivingMode.RIGHT_TURN: RightTurn(),
                                                     DrivingMode.COMPLEX_AREA: ComplexArea(),
                                                     DrivingMode.UTURN: UTurn(),
                                                     DrivingMode.TOLLGATE: Tollgate(),
                                                     DrivingMode.TUNNEL: Tunnel(),
                                                     DrivingMode.STATIC_OBSTACLE: StaticObstacle(),
                                                     DrivingMode.DYNAMIC_OBSTACLE: DynamicObstacle()}
        
        self._publishers = {"steer": self.create_publisher(WriteCar, "/control", qos)}
        self._subscribers = {"yolo": self.create_subscription(BoundingBoxes, "/yolo", self.yolo_callback, qos),
                             "place": self.create_subscription(String, "/place", self.place_callback, qos)}
        self.timer = self.create_timer(0.1, self.callback)
    
    def yolo_callback(self, msg: BoundingBoxes):
        self.objects = msg
        
    def place_callback(self, msg: String):
        self.place = msg.data
        
    def callback(self):
        self.update()
        
        if self.driving_mode == DrivingMode.CRUISING:
            self.steer = self.missions[self.driving_mode].steer
        elif self.driving_mode == DrivingMode.RIGHT_TURN:
            pass
        elif self.driving_mode == DrivingMode.COMPLEX_AREA:
            pass
        elif self.driving_mode == DrivingMode.UTURN:
            pass
        elif self.driving_mode == DrivingMode.TOLLGATE:
            pass
        elif self.driving_mode == DrivingMode.TUNNEL:
            pass
        elif self.driving_mode == DrivingMode.STATIC_OBSTACLE:
            pass
        elif self.driving_mode == DrivingMode.DYNAMIC_OBSTACLE:
            pass
    
    def update(self):
        if self._right_turn():
            self.driving_mode = DrivingMode.RIGHT_TURN
        elif self._complex_area():
            self.driving_mode = DrivingMode.COMPLEX_AREA
        elif self._uturn():
            self.driving_mode = DrivingMode.UTURN
        elif self._tollgate():
            self.driving_mode = DrivingMode.TOLLGATE
        elif self._tunnel():
            self.driving_mode = DrivingMode.TUNNEL
        elif self._static_obstacle():
            self.driving_mode = DrivingMode.STATIC_OBSTACLE
        elif self._dynamic_obstacle():
            self.driving_mode = DrivingMode.DYNAMIC_OBSTACLE
        else:
            self.driving_mode = DrivingMode.CRUISING

        for mode, mission in self.missions.items():
            if mode != self.driving_mode:
                mission.running = False
                
    def process_erp_msg(self, speed: int = None, steer: int = None):
        self.erp.write_speed = self.speed if speed is None else speed
        self.erp.write_steer = max(-1900, min(1900, steer))
    
    def combine_steer(self):
        pass
    
    # operate based on the driving mode
    def cruising(self) -> None:
        pass
    
    def right_turn(self) -> None:
        pass
    
    def complex_area(self) -> None:
        pass
    
    def uturn(self) -> None:
        pass
    
    def tollgate(self) -> None:
        pass
    
    def tunnel(self) -> None:
        pass
    
    def tunnel(self) -> None:
        pass
    
    def tunnel(self) -> None:
        pass
    
    # recognize places
    def _cruising(self) -> bool:
        pass
    
    def _right_turn(self) -> bool:
        return self.missions[DrivingMode.RIGHT_TURN].entered
    
    def _complex_area(self) -> bool:
        pass
    
    def _uturn(self) -> bool:
        pass
    
    def _tollgate(self) -> bool:
        pass
    
    def _tunnel(self) -> bool:
        pass
    
    def _static_obstacle(self) -> bool:
        pass
    
    def _dynamic_obstacle(self) -> bool:
        pass
    
    
    
def main(args=None):
    rclpy.init(args=args)
                                      
    state = State()
                                                                          
    rclpy.spin(state)

    state.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()