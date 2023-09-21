import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from steady_msgs.msg import WriteCar

class Control(Node):
    def __init__(self):
        super().__init__('control')
        
        qos = QoSProfile(depth=1)
        self.speed = 0
        self.steer = 0
        self.lane_steer = 0
        self.lane_speed = 0
        self.complex_steer = 0
        self.complex_speed = 0
        self.go = False
        # self.final_speed = 0
        # self.final_steer = 0

        self.erp_sub = self.create_subscription(WriteCar, '/control', self.callback, 1)
        self.lane_control = self.create_subscription(WriteCar, "/lane_control", self.lane_callback, qos)
        self.complex_control = self.create_subscription(WriteCar, "complex_control", self.complex_callback, qos)
        self.erp_pub = self.create_publisher(WriteCar, '/write_car', 1)
        self.erp = WriteCar()

    def pub_serial(self, speed, steer):
        self.erp.write_speed = speed
        self.erp.write_steer = steer
        self.erp_pub.publish(self.erp)
        print("Published speed:", speed)
        print("Published steer:", steer)

    def callback(self, data: WriteCar):
        self.speed = data.write_speed
        self.steer = data.write_steer
        # self.pub_serial(self.speed, self.steer)

    def lane_callback(self, data):
        self.lane_speed = data.write_speed
        self.lane_steer = data.write_steer

    def complex_callback(self, data):
        self.go = data.complex
        self.complex_speed = data.write_speed
        self.complex_steer = data.write_steer

    def final_control(self):
        final_speed = 60
        final_steer = 0
        final_speed = self.lane_speed
        final_steer = self.lane_steer

        if self.go == True:
            final_speed = self.complex_speed
            final_steer = self.complex_steer

        print(final_speed, final_steer)

        return final_speed, final_steer
    
    # def final_control(self):
    #     final_speed = 60
    #     final_steer = 0
    #     final_speed = self.lane_speed
    #     final_steer = self.lane_steer

    #     if self.go == True:
    #         final_speed = self.complex_speed
    #         final_steer = self.complex_steer

        

        



    

def main(args=None):
    rclpy.init(args=args)
    s = Control()
    speed, steer = s.final_control()
    s.pub_serial(speed, steer)
    rclpy.spin(s)  # Continuously process callbacks.

    s.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()