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
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'zed_image = steadylab.scripts.zed_image:main',
            'zed_depth = steadylab.scripts.zed_depth:main',
            'zed_pose = steadylab.scripts.zed_pose:main',
            'zed_path_map = steadylab.scripts.zed_path_map:main',
            'zed_pointcloud = steadylab.scripts.zed_pointcloud:main',
            'zed_imu = steadylab.scripts.zed_imu:main',
            'zed_tf = steadylab.scripts.zed_tf:main',
            'data_hub = steadylab.scripts.data_hub:main',
            'yolo = steadylab.scripts.yolo:main',
            'depth = steadylab.scripts.depth:main',
        ],                                                                                                                  
    },
)
