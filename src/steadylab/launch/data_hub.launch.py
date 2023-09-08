import os

from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node

# this is the function launch  system will look for
def generate_launch_description():

    # create and return launch description object
    return LaunchDescription(
        [
            Node(package="steadylab",
                 executable="zed_image"),

            Node(package="steadylab",
                 executable="zed_depth"),

            Node(package="steadylab",
                 executable="zed_pose"),

            Node(package="steadylab",
                 executable="zed_path_map"),

            Node(package="steadylab",
                 executable="zed_pointcloud"),
        ]
    )