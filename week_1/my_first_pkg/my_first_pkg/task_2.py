import rclpy
from rclpy.node import Node
import os

class CounterNode(Node):
        def __init__(self):
                super().__init__('counter_node')
                
                # Create a path to store the counter.txt file in the same directory as this script
                file_path = os.path.join(os.path.dirname(__file__), 'counter.txt')
                
                # Initialize count
                count = 1
                
                # Check if the file exists and read the current count
                if os.path.exists(file_path):
                        with open(file_path, 'r') as f:
                                content = f.read().strip()
                                if content.isdigit():
                                        count = int(content)
                
                # Log the current run count
                self.get_logger().info(f'Run count: {count}')
                
                # Increment the counter and save it back to the text file
                with open(file_path, 'w') as f:
                        f.write(str(count + 1))

def main(args=None):
        rclpy.init(args=args)
        node = CounterNode()

        # spin_once lets us create the node, log once, and exit cleanly
        rclpy.spin_once(node, timeout_sec=0.1)
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
        main()
