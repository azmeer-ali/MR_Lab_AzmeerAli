from setuptools import find_packages, setup

package_name = 'my_turtle_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='azmeer53',
    maintainer_email='azmeerali1003@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        'my_node = my_turtle_package.my_node:main',
        'shapes = my_turtle_package.shapes:main',
        'spawn_turtles = my_turtle_package.spawn_turtles:main',
        'go_to_goal = my_turtle_package.go_to_goal:main',
        ],
    },
)
