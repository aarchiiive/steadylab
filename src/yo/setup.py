from setuptools import find_packages, setup

package_name = 'yo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools',
                      'torch'],
    zip_safe=True,
    maintainer='bg',
    maintainer_email='okharry1@naver.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'realtime_bev_ros2 = yo.realtime_bev_ros2:main',
        ],
    },
)
