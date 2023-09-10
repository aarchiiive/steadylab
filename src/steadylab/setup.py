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
            'zed_image = steadylab.zed.image:main',
            'zed_depth = steadylab.zed.depth:main',
            'zed_pose = steadylab.zed.pose:main',
            'zed_path_map = steadylab.zed.path_map:main',
            'zed_pointcloud = steadylab.zed.pointcloud:main',
            'zed_imu = steadylab.zed.imu:main',
            'zed_tf = steadylab.zed.tf:main',
            'data_hub = steadylab.src.data_hub:main',
            'yolo = steadylab.src.yolo:main',
            'depth = steadylab.src.depth:main',
            'state = steadylab.src.state:main',
            'serial = steadylab.src.serial:main',
            
            'comm = steadylab.comm:main',
            'keyboard_erp = steadylab.keyboard_erp:main',
            'main_status = steadylab.main_status:main',

            # test
            'test_yolo = steadylab.test.yolo:main',
        ],                                                                                                                  
    },
)
