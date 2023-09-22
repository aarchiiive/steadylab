import sys
import time
from ultralytics import YOLO
from collections import deque
import rclpy
from rclpy.node import Node
from steady_msgs.msg import BoundingBox, BoundingBoxes, WriteCar

sys.path.append("src/steadylab/steadylab")

from core.message import Int16
from missions.mission import Mission

class ComplexArea(Mission):
    def __init__(self, queue_size: int = 10,min_duration: float = 2.0,qos: int = 5):
        super().__init__("complex_area", queue_size, min_duration, qos)
        self.objects = [24, 25, 26, 27, 28, 29]
        self.erp = WriteCar()
        # self.box = BoundingBox()
        
        self.model = YOLO('complex1.pt')
        self._subscribers = self.create_subscription(BoundingBoxes, '/yolo', self.yolo_callback, qos)
    

    def yolo_callback(self, data):
        
        box_cls = data.boxes[0]
        box_name = data.boxes[1]
        box_xn = data.boxes[4][0]
        # boxes[4] = xywhn, boxes[4][0] = normalized x(0~1)
        box_conf = data.boxes[2]

        if 27 == box_cls and box_conf > 0.3:
            print("x_arrow")
            if (0.5-0.01) <= box_xn < (0.5-0.005):
                self.steer = -60
                print("turn left, steer -60")
            elif (0.5-0.4) <= box_xn < (0.5-0.01):
                self.steer = -90
                print("turn left, steer -90")
            elif (0.5+0.005) <= box_xn < (0.5+0.01):
                self.steer = 60
                print("turn right, steer 60")
            elif (0.5+0.01) <= box_xn < (0.5+0.04):
                self.steer = 90
                print("turn right, steer 90")

        elif 28 == box_cls and box_conf > 0.3:
            print(box_name) #left_arrow
            if (0.5-0.01) <= box_xn < (0.5-0.005):
                self.steer = -60
                print("turn left, steer -60")
            elif (0.5-0.4) <= box_xn < (0.5-0.01):
                self.steer = -90
                print("turn left, steer -90")
            elif (0.5+0.005) <= box_xn < (0.5+0.01):
                self.steer = 60
                print("turn right, steer 60")
            elif (0.5+0.01) <= box_xn < (0.5+0.04):
                self.steer = 90
                print("turn right, steer 90")

        elif 26 == box_cls and box_conf > 0.3:
            print(box_name) #stop_line
            if (0.5-0.01) <= box_xn < (0.5-0.005):
                self.steer = -60
                print("turn left, steer -60")
            elif (0.5-0.4) <= box_xn < (0.5-0.01):
                self.steer = -90
                print("turn left, steer -90")
            elif (0.5+0.005) <= box_xn < (0.5+0.01):
                self.steer = 60
                print("turn right, steer 60")
            elif (0.5+0.01) <= box_xn < (0.5+0.04):
                self.steer = 90
                print("turn right, steer 90")

        elif 25 == box_cls and box_conf > 0.3:
            print(box_name) #speed_bump
            if (0.5-0.01) <= box_xn < (0.5-0.005):
                self.steer = -60
                print("turn left, steer -60")
            elif (0.5-0.4) <= box_xn < (0.5-0.01):
                self.steer = -90
                print("turn left, steer -90")
            elif (0.5+0.005) <= box_xn < (0.5+0.01):
                self.steer = 60
                print("turn right, steer 60")
            elif (0.5+0.01) <= box_xn < (0.5+0.04):
                self.steer = 90
                print("turn right, steer 90")

        elif 29 == box_cls and box_conf > 0.3:
            print(box_name) #slash
            self.steer = 0

        elif 24 == box_cls and box_conf > 0.3:
            print(box_name) #speed_sign
            self.steer = 0


    # def yolo_callback(self, msg: BoundingBoxes):
    #     # self.reset()
        
    #     for box in msg.boxes:
    #         _ = self.queue.popleft()
    #         self.queue.append(box.cls)
            
    #     counts = sum([self.queue.count(o) for o in self.objects])
        
    #     if counts >= int(0.8*len(self.queue)):
    #         self.running = True
    #         self.last = time.time()
    
    def run(self):
        if self.running:
            return self.steer
        
    def main(args=None):
        rclpy.init(args=args)
                                        
        complex_area = ComplexArea()
                                                                            
        rclpy.spin(complex_area)

        complex_area.destroy_node()
        rclpy.shutdown()

    if __name__ == "__main__":
        main()