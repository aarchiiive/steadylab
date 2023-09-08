import sys
import rclpy

sys.path.append("src/steadylab/steadylab")

from messages.zed import zed_messages
from core.data_hub import DataHub


def main(args=None):
    rclpy.init(args=args)

    data_hub = DataHub(zed_messages)
                                                                          
    rclpy.spin(data_hub)

    data_hub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()