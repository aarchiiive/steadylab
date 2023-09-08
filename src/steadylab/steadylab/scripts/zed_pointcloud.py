import sys
import cv2

import rclpy

sys.path.append("src/steadylab/steadylab")

from messages.zed import zed_messages
from core.node import Zed


def main(args=None):
    rclpy.init(args=args)

    msg = zed_messages["pointcloud"]
    subscriber = Zed(msg.node_name, msg.topic, msg.msg_type, msg.processor)
                                                                          
    rclpy.spin(subscriber)

    subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()