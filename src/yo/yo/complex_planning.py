from ultralytics import YOLO
import cv2
import torch
import numpy as np
import rclpy
from rclpy.node import Node
from steady_msgs import WriteCar


class YOLOPlanning(Node):
    def __init__(self):
        super().__init__('yolo_planning')
        self.erp_pub = self.create_publisher(WriteCar, 'complex_control', 10)
        self.erp = WriteCar()

    def pub_serial(self, go, speed, steer):
        self.erp.complex = go
        self.erp.write_speed = speed
        self.erp.write_steer = steer
        self.erp_pub.publish(self.erp)

model = YOLO('complex1.pt')  # pretrained YOLOv8n model
# model = YOLO('yolov8n.pt')  # pretrained YOLOv8n model


results = model.predict("z2.jpg", show=True)
# results = model.predict("twodog.jpg", show=True)

go = False
steer = 0
speed = 60


#xyxy, first xy(top left), second xy(bottom right)
# if]
# x -> y -> stop_line -> speedbump -> z -> speed_sign
'''
speed_sign : 0
speedbump : 1
stop_line : 2
x : 3
y : 4
z : 5
'''
def yolo_steer(node):
    for r in results:
        box = r.boxes
        box_cls = box.cls.cpu().detach().numpy().tolist()
        box_xys = box.xyxy.cpu().detach().numpy().tolist()
        # cam_centre = 320
        image_x = r.orig_shape
        cam_centre = image_x[1]/2
        #normalized 0~1 사이인지 보고 0.5 도 확인

        
        # if gap is +, it's on left, when - it's on right

        print("box_cls : ", box_cls)
        print("box_xys : ", box_xys)

        if len(box_cls) > 0:
            go = True
            print("True")


        if 3.0 in box_cls:
            box_ind = box_cls.index(3.0)
            print("x")
            print("=======")
            box_x = (box_xys[box_ind][0] + box_xys[box_ind][2])/2
            gap = cam_centre - box_x
            # if box_x < cam_centre:
            if 0 <= gap < 30:
                steer = 0
                print("turn left, steer 0")
            elif 30 <= gap < 60:
                steer = -60
                print("turn left, steer -60")
            elif 60 <= gap:
                steer = -90
                print("turn left, steer -90")
            elif -30 < gap <= 0:
                steer = 0
                print("turn right, steer 0")
            elif -60 < gap <= -30:
                steer = 60
                print("turn right, steer 60")
            elif gap <= -60:
                steer = 90
                print("turn right, steer 90")

        elif 4.0 in box_cls:
            box_ind = box_cls.index(4.0)
            print("y")
            print("=======")
            box_x = (box_xys[box_ind][0] + box_xys[box_ind][2])/2
            gap = cam_centre - box_x
            if 0 <= gap < 30:
                steer = 0
                print("turn left, steer 0")
            elif 30 <= gap < 60:
                steer = -60
                print("turn left, steer -60")
            elif 60 <= gap:
                steer = -90
                print("turn left, steer -90")
            elif -30 < gap <= 0:
                steer = 0
                print("turn right, steer 0")
            elif -60 < gap <= -30:
                steer = 60
                print("turn right, steer 60")
            elif gap <= -60:
                steer = 90
                print("turn right, steer 90")

        elif 2.0 in box_cls:
            box_ind = box_cls.index(2.0)
            print("stop_line")
            print("=======")
            box_x = (box_xys[box_ind][0] + box_xys[box_ind][2])/2
            gap = cam_centre - box_x
            if 0 <= gap < 30:
                steer = 0
                print("turn left, steer 0")
            elif 30 <= gap < 60:
                steer = -60
                print("turn left, steer -60")
            elif 60 <= gap:
                steer = -90
                print("turn left, steer -90")
            elif -30 < gap <= 0:
                steer = 0
                print("turn right, steer 0")
            elif -60 < gap <= -30:
                steer = 60
                print("turn right, steer 60")
            elif gap <= -60:
                steer = 90
                print("turn right, steer 90")

        elif 1.0 in box_cls:
            box_ind = box_cls.index(1.0)
            print("speedbump")
            print("=======")
            box_x = (box_xys[box_ind][0] + box_xys[box_ind][2])/2
            gap = cam_centre - box_x
            if 0 <= gap < 30:
                steer = 0
                print("turn left, steer 0")
            elif 30 <= gap < 60:
                steer = -60
                print("turn left, steer -60")
            elif 60 <= gap:
                steer = -90
                print("turn left, steer -90")
            elif -30 < gap <= 0:
                steer = 0
                print("turn right, steer 0")
            elif -60 < gap <= -30:
                steer = 60
                print("turn right, steer 60")
            elif gap <= -60:
                steer = 90
                print("turn right, steer 90")

        elif 5.0 in box_cls:
            box_ind = box_cls.index(5.0)
            steer = 0
            print("z")
            print("=======")
            print("steer 0")
        
        elif 0.0 in box_cls:
            box_ind = box_cls.index(0.0)
            steer = 0
            print("speed_sign")
            print("=======")
            print("steer 0")


        # Tollgate
        indices = [i for i, value in enumerate(box_cls) if value == 16.0]
        if len(indices) == 2:
            box_x_values = []

            for tollgate_ind in indices:
                box_x = (box_xys[tollgate_ind][0] + box_xys[tollgate_ind][2]) / 2
                box_x_values.append(box_x)

            avg_box_tollgate = sum(box_x_values) / 2
            print("Average box_x : ", avg_box_tollgate)
            gap_tollgate = cam_centre - avg_box_tollgate
            if 0 <= gap_tollgate < 30:
                steer = 0
                print("turn left, steer 0")
            elif 30 <= gap_tollgate < 60:
                steer = -60
                print("turn left, steer -60")
            elif 60 <= gap_tollgate:
                steer = -90
                print("turn left, steer -90")
            elif -30 < gap_tollgate <= 0:
                steer = 0
                print("turn right, steer 0")
            elif -60 < gap_tollgate <= -30:
                steer = 60
                print("turn right, steer 60")
            elif gap_tollgate <= -60:
                steer = 90
                print("turn right, steer 90")


        node.pub_serial(go, speed, steer)


def main(args=None):
    rclpy.init(args=args)
    node = YOLOPlanning()

    yolo_steer(node)

    node.destroy_node()
    rclpy.shutdown()



if __name__ == '__main__':
    main()

