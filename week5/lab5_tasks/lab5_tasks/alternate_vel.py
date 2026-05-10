import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class AlternateVelocity(Node):
    def __init__(self):
        super().__init__('alternate_velocity_node')
        # Create a publisher to the /cmd_vel topic [cite: 182]
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        # Create a timer that triggers every 2 seconds [cite: 182]
        self.timer = self.create_timer(2.0, self.timer_callback)
        self.is_moving = False

    def timer_callback(self):
        msg = Twist()
        
        # Alternate the logic between moving and stopping
        if self.is_moving:
            msg.linear.x = 0.0  # Stop [cite: 182]
            self.get_logger().info('Publishing: Stop (0.0 m/s)')
        else:
            msg.linear.x = 0.2  # Move forward [cite: 182]
            self.get_logger().info('Publishing: Forward (0.2 m/s)')
            
        msg.angular.z = 0.0 # Ensure no rotation
        self.publisher_.publish(msg)
        
        # Flip the boolean state for the next timer cycle
        self.is_moving = not self.is_moving

def main(args=None):
    rclpy.init(args=args)
    node = AlternateVelocity()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
