import rclpy
from rclpy.node import Node

class UTurn(Node):
    def __init__(self):
        super().__init__("uturn")


def main(args=None):
    rclpy.init(args=args)
                                      
    uturn = UTurn()
                                                                          
    rclpy.spin(uturn)

    uturn.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()