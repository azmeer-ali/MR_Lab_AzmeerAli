import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class ShapePublisher(Node):
    def __init__(self):
        super().__init__('shape_publisher')
        self.publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        time.sleep(1) # Wait for connection
        self.draw_circle()
        self.draw_triangle()

    def draw_circle(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 2.0
        self.get_logger().info('Drawing Circle...')
        for _ in range(35): # Publish loop for curve
            self.publisher.publish(msg)
            time.sleep(0.1)
        self.stop()

    def draw_triangle(self):
        msg = Twist()
        self.get_logger().info('Drawing Triangle...')
        for _ in range(3):
            # Move forward
            msg.linear.x = 2.0
            msg.angular.z = 0.0
            self.publisher.publish(msg)
            time.sleep(1.5)
            
            # Turn 120 degrees
            msg.linear.x = 0.0
            msg.angular.z = 2.094 # ~120 degrees in radians
            self.publisher.publish(msg)
            time.sleep(1.0)
        self.stop()

    def stop(self):
        msg = Twist()
        self.publisher.publish(msg)
        time.sleep(0.5)

def main(args=None):
    rclpy.init(args=args)
    node = ShapePublisher()
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
