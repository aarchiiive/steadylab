#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import serial
import struct
import numpy as np
from serial_communication.msg import ErpRead, ErpWrite

# Constants
MAX = 18
PI = np.pi

# Global variables - callback functions cannot access rospy.Publisher and rospy.Subscriber
steer1 = 0
steer2 = 0
speed1 = 0
brake = 0
gear = 0
E_stop = False
inputbool = 0

# Write callback function
def write_callback(write):
    global steer1, steer2, speed1, brake, gear, E_stop, inputbool
    inputbool = 1
    E_stop = write.write_e_stop
    gear = write.write_gear
    steer = write.write_steer
    steer1 = (steer/256)
    steer2 = (steer%256)
    if steer < 0: 
        steer1 = steer1 - 1
    speed1 = write.write_speed
    brake = write.write_brake

# Initialize ROS node, publisher, and subscriber
rclpy.init_node("serial_node")
serial_pub = rclpy.Publisher("erp_read", ErpRead, queue_size=1)
serial_sub = rclpy.Subscriber("erp_write", ErpWrite, write_callback)
rate = rclpy.Rate(50)

# Initialize serial communication
ser = serial.Serial(port="/dev/ttyUSB0", baudrate=115200, timeout=1)

if ser.isOpen():
    rclpy.loginfo("Serial Port initialized")
else:
    rclpy.logfatal("Unable to open serial port")
    exit(1)

# Initialize local variables
#uint8_t
a = 0
PCU_to_UPPER = [0x00] * 18

UPPER_to_PCU = [0x53, 0x54, 0x58, 0x01, 0x00, gear, 0x00, speed1, steer1, steer2, brake, a, 0x0D, 0x0A]

erp42_state = ErpRead()

# Main loop
while not rclpy.is_shutdown():
    # If the input is available
    if ser.in_waiting:
        PCU_to_UPPER = list(ser.read(18))

        rclpy.loginfo(" ".join("{:02X}".format(c) for c in PCU_to_UPPER))

        # When the callback function is called
        if inputbool:
            a += 1
            UPPER_to_PCU = [0x53, 0x54, 0x58, 0x01, 0x00, gear, 0x00, speed1, steer1, steer2, brake, a, 0x0D, 0x0A]
            ser.write(bytearray(UPPER_to_PCU))
            rate.sleep()

        # When the callback function is not called
        else:
            a += 1
            UPPER_to_PCU = [0x53, 0x54, 0x58, 0x01, 0x00, 0x01, 0x00, 0x00, steer1, steer2, 0x80, a, 0x0D, 0x0A]
            ser.write(bytearray(UPPER_to_PCU))
            rate.sleep()

ser.close()
