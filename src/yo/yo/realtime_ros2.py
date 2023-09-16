# ----------------------------------------------------------------------------
# Copyright (C) [2023] Byounggun Park
#
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ----------------------------------------------------------------------------


import time
from pathlib import Path
import cv2
import torch
import numpy as np
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from serial_communication.msg import WriteCar  # 메시지 타입에 맞게 변경해주세요.
import sys
import threading

# Conclude setting / general reprocessing / plots / metrices / datasets
from yo.utils.utils import \
    time_synchronized, select_device, increment_path, safe_polyfit,draw_grid,\
    scale_coords, xyxy2xywh, non_max_suppression, split_for_trace_model, show_lane_lines,\
    driving_area_mask, lane_line_mask, plot_one_box, show_seg_result, detect_lane_with_sliding_window,\
    AverageMeter, \
    LoadImages

class CarController(Node):
    def __init__(self):
        super().__init__('car_controller')
        self.erp_pub = self.create_publisher(WriteCar, 'car_control', 10)
        self.erp = WriteCar()

    def pub_serial(self, speed, steer):
        self.erp.write_speed = speed
        self.erp.write_steer = steer
        self.erp_pub.publish(self.erp)


def is_mask_empty(mask):
    return mask.sum() == 0


def draw_grid(image, grid_size, color=(0, 255, 0), line_width=1):
    """
    Draws a grid on the image.

    Args:
    - image: Input image.
    - grid_size: Size of the grid cells.
    - color: Color of the grid lines.
    - line_width: Width of the grid lines.

    Returns:
    - Image with overlayed grid.
    """
    # Copy the input image to avoid modifying it directly
    img = image.copy()

    # Compute spacing between grid lines
    spacing_x = img.shape[1] // grid_size
    spacing_y = img.shape[0] // grid_size

    # Draw vertical grid lines
    for x in range(0, img.shape[1], spacing_x):
        cv2.line(img, (x, 0), (x, img.shape[0]), color, line_width)

    # Draw horizontal grid lines
    for y in range(0, img.shape[0], spacing_y):
        cv2.line(img, (0, y), (img.shape[1], y), color, line_width)

    return img


def detect(node, source="0", weights="/home/bg/ros2_ws/src/yo/yo/data/weights/yolopv2.pt",
           img_size=256, conf_thres=0.3, iou_thres=0.45, device="0", save_conf=False,
           save_txt=False, nosave=False, classes=None, agnostic_nms=False,
           project="runs/detect", exist_ok=False):
    
    save_txt, imgsz = save_txt, img_size

    inf_time = AverageMeter()
    waste_time = AverageMeter()
    nms_time = AverageMeter()

    # Load model
    stride = 32
    model = torch.jit.load(weights)
    device = select_device(device)
    half = device.type != 'cpu'  # half precision only supported on CUDA
    model = model.to(device)
    if half:
        model.half()  # to FP16
    model.eval()

    # Set Dataloader
    vid_path, vid_writer = None, None
    if source == "0":  # 카메라 입력 체크
        cap = cv2.VideoCapture(2)
        cap.set(cv2.CAP_PROP_AUTOFOCUS, 2)
        if not cap.isOpened():
            raise IOError("Cannot open webcam")
    else:
        dataset = LoadImages(source, img_size=imgsz, stride=stride)

    if device.type != 'cpu':
        model(torch.zeros(1, 3, imgsz, imgsz).to(device).type_as(next(model.parameters())))  # run once

    t0 = time.time()


    def inference(img, im0, path):
        # Inference code
        t1 = time_synchronized()
        
        [pred, anchor_grid], seg, ll = model(img)
        # t2 = time_synchronized()
        # tw1 = time_synchronized()
        pred = split_for_trace_model(pred, anchor_grid)
        # tw2 = time_synchronized()
        # t3 = time_synchronized()
        pred = non_max_suppression(pred, conf_thres, iou_thres, classes=classes,
                                   agnostic=agnostic_nms)
        t4 = time_synchronized()

        # da_seg_mask = driving_area_mask(seg, grid_size=10, grid_range=(0,5,0,10))
        da_seg_mask = driving_area_mask(seg)
        ll_seg_mask_left = lane_line_mask(ll, grid_size=11, grid_range=(6,10,3,4))
        ll_seg_mask_light_left = lane_line_mask(ll, grid_size=11, grid_range=(6,10,2,3))
        ll_seg_mask_right = lane_line_mask(ll, grid_size=11, grid_range=(6,10,7,8))
        ll_seg_mask_light_right = lane_line_mask(ll, grid_size=11, grid_range=(6,10,7,8))

        steer = 0
        for i, det in enumerate(pred):
            p = Path(path)
            if source != "0":
                frame = getattr(dataset, 'frame', 0)

            s = '%gx%g ' % img.shape[2:]
            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]

            if len(det):
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()

                for *xyxy, conf, cls in reversed(det):
                    if save_txt:
                        xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()
                        line = (cls, *xywh, conf) if save_conf else (cls, *xywh)

            # print(f'{s}Done. ({t2 - t1:.3f}s)')
            show_seg_result(im0, (da_seg_mask, ll_seg_mask_left, ll_seg_mask_right), img_shape=im0.shape[:2], is_demo=True)

            l = is_mask_empty(ll_seg_mask_left)
            light_l = is_mask_empty(ll_seg_mask_light_left)
            r = is_mask_empty(ll_seg_mask_right)


            if l == False and r == True:
                steer = 1200
                print("left, 1200")
            elif l == True and r == False:
                steer = -1200
                print("right, -1200")
            elif light_l == False:
                steer = 600
                print("light left, 600")
            else:
                steer = 0
                print("0 steer")
            

            speed = 40

            node.pub_serial(speed, steer)
            img_with_grid = draw_grid(im0, grid_size=11)

            cv2.imshow('Detection', img_with_grid)
            if cv2.waitKey(1) == ord('q'):
                if cap:
                    cap.release()
                cv2.destroyAllWindows()
                exit()

        # inf_time.update(t2 - t1, img.size(0))
        # nms_time.update(t4 - t3, img.size(0))
        # waste_time.update(tw2 - tw1, img.size(0))

    if source == "0":
        while True:
            path = "webcam_frame"
            ret, im0 = cap.read()
            if not ret:
                break

            img = cv2.resize(im0, (imgsz, imgsz))
            img = torch.from_numpy(img).permute(2, 0, 1).float().div(255.0).unsqueeze(0).to(device).type_as(
                next(model.parameters()))
            inference(img, im0, path)
    else:
        for path, img, im0s, vid_cap in dataset:
            inference(img, im0s, path)

    print('inf : (%.4fs/frame)   nms : (%.4fs/frame)' % (inf_time.avg, nms_time.avg))
    print(f'Done. ({time.time() - t0:.3f}s)')


def main(args=None):
    rclpy.init(args=args)
    node = CarController()

    with torch.no_grad():
        detect(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

