#!/usr/bin/env python
import rclpy

# message file
from serial_communication.msg import ErpRead
from serial_communication.msg import ErpWrite

class Serial():
    def __init__(self):
        self.speed = 0
        self.steer = 0
    
        self.sub_speed_steer = rclpy.Subscriber('serial', ErpWrite, self.callback, queue_size=1)
        self.erp_sub = rclpy.Subscriber('erp_read', ErpRead, self.callback, queue_size=1)

        self.erp_pub = rclpy.Publisher("erp_write", ErpWrite, queue_size=1)
        self.erp = ErpWrite()

    def callback(self,data):
        self.speed = data.read_speed
        self.steer = data.read_steer

    def serial(self,key):
        
        if(key==8):
            self.speed = self.speed + 10
        elif(key==2):
            self.speed = self.speed - 10
        elif(key==4):
            self.steer = self.steer + 10
        elif(key==6):
           self.steer = self.steer - 10
        elif(key==0):
            self.steer = 0

        if(self.speed > 200):
            self.speed = 200
        elif(self.speed < 0):
            self.speed = 0
        if(self.steer > 2000):
            self.steer = 2000
        elif(self.steer < -2000):
            self.steer = -2000

        speed = self.speed
        steer = self.steer
        
        return speed, steer
    
    def pub_serial(self, speed, steer):
        speed, steer = speed, steer
        self.erp.write_speed = speed
        self.erp.write_steer = steer

        self.erp_pub.publish(self.erp)

    # def speed_planner(self):
    #     speed, brake, gear = 0, 1, 0

def main():
    rclpy.init_node("serial", anonymous=True)

    rate = rclpy.Rate(10)

    s = Serial()
    while not rclpy.is_shutdown():
        # speed, brake, gear = s.speed_planner()
        # speed = 0
        print("speed : 8 + 2 -, steer : 4 - 6+ ,stop : 0")
        key = input("key : ")

        speed, steer = s.serial(key)
        print("speed"),speed
        print("steer"),steer
        s.pub_serial(speed, steer)

        rate.sleep()


if __name__ == '__main__':
    main()