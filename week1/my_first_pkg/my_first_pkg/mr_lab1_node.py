import rclpy
from rclpy.node import Node
import os

class MobileRoboticsNode(Node):
    def __init__(self):
        super().__init__('mr_lab1_node')

        # Task 3: Declare and read student_name parameter
        self.declare_parameter('student_name', 'Not set')
        student_name = self.get_parameter('student_name').get_parameter_value().string_value

        # Task 1: Customize the log message
        self.get_logger().info('Welcome to Mobile Robotics Lab')

        # Print the student name based on the parameter
        if student_name != 'Not set':
            self.get_logger().info(f'{student_name}')
        else:
            self.get_logger().info('student_name not set')

        # Task 2: Counter implementation
        counter_file = os.path.expanduser('~/ros2_ws/src/my_first_pkg/run_counter.txt')
        count = 1

        if os.path.exists(counter_file):
            with open(counter_file, 'r') as f:
                content = f.read().strip()
                if content.isdigit():
                    count = int(content) + 1

        with open(counter_file, 'w') as f:
            f.write(str(count))

        self.get_logger().info(f'Run count: {count}')

def main(args=None):
    rclpy.init(args=args)
    node = MobileRoboticsNode()
    rclpy.spin_once(node, timeout_sec=0.1)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
