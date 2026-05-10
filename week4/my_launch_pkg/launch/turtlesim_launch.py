from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, TimerAction

def generate_launch_description():
    
    # Define the spawn command
    spawn_turtle2 = ExecuteProcess(
        cmd=['ros2', 'service', 'call', '/spawn', 'turtlesim/srv/Spawn', "{x: 2.0, y: 2.0, theta: 0.0, name: 'turtle2'}"],
        output='screen'
    )

    return LaunchDescription([
        # 1. Start the main turtlesim window
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),
        
        # 2. DELAY the spawn command by 2 seconds to wait for turtlesim to open
        TimerAction(
            period=2.0,
            actions=[spawn_turtle2]
        ),
        
        # 3. Start the follower node
        Node(
            package='my_launch_pkg', 
            executable='follower_node',
            name='follower'
        ),
        
        # 4. Start the teleop node
        Node(
            package='turtlesim',
            executable='turtle_teleop_key',
            name='teleop',
            prefix='xterm -e'
        )
    ])