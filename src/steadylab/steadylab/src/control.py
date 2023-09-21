import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from serial_communication.msg import ReadCar
from serial_communication.msg import WriteCar

class Control(Node):
    def __init__(self):
        super().__init__('control')
        
        qos = QoSProfile(depth=1)
        self.speed = 0
        self.steer = 0

        self.erp_sub = self.create_subscription(WriteCar, '/control', self.callback, 1)
        self.erp_pub = self.create_publisher(WriteCar, '/write_car', 1)
        self.erp = WriteCar()

    def callback(self, data: WriteCar):
        self.speed = data.write_speed
        self.steer = data.write_steer
        self.pub_serial(self.speed, self.steer)

    def pub_serial(self, speed, steer):
        self.erp.write_speed = speed
        self.erp.write_steer = steer
        self.erp_pub.publish(self.erp)
        print("Published speed:", speed)
        print("Published steer:", steer)

def main(args=None):
    rclpy.init(args=args)
    s = Control()
    rclpy.spin(s)  # Continuously process callbacks.

    s.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()