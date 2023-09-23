import os
import glob
from setuptools import setup

package_name = 'steadylab'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob.glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='song',
    maintainer_email='song@todo.todo',
    description='SteadyLab inc.',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # zed
            'zed_image = steadylab.zed.image:main',
            'zed_depth = steadylab.zed.depth:main',
            'zed_pose = steadylab.zed.pose:main',
            'zed_path_map = steadylab.zed.path_map:main',
            'zed_pointcloud = steadylab.zed.pointcloud:main',
            'zed_imu = steadylab.zed.imu:main',
            'zed_tf = steadylab.zed.tf:main',
            
            # src
            'data_hub = steadylab.src.data_hub:main',
            'state = steadylab.src.state:main',
            'pre_state = steadylab.src.pre.state:main',
            'serial = steadylab.src.serial:main',
            'recorder = steadylab.src.recorder:main',
            'control = steadylab.src.control:main',
            
            # missions
            'cruising = steadylab.missions.cruising:main',
            'complex_area = steadylab.missions.complex_area:main',
            'uturn = steadylab.missions.uturn:main',
            'tollgate = steadylab.missions.tollgate:main',
            'tunnel = steadylab.missions.tunnel:main',
            'general_obstacle = steadylab.object.general_obstacle:main',
            'static_obstacle = steadylab.object.static_obstacle:main',
            'dynamic_obstacle = steadylab.object.dynamic_obstacle:main',
            
            # sensors
            'yolo = steadylab.sensor.yolo:main',
            'depth = steadylab.sensor.depth:main',
            'lane = steadylab.sensor.lane:main',
            'pose = steadylab.sensor.pose:main',
            
            # objects & obstacles
            'traffic_light = steadylab.object.traffic_light:main',
            
            # planning
            'steer = steadylab.planning.steer:main',
            
            # test
            'test_yolo = steadylab.test.yolo:main',
            'player = steadylab.test.player:main',
        ],                                                                                                                  
    },
)
