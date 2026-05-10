import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import numpy as np

class LidarNavigator(Node):
    def __init__(self):
        super().__init__('lidar_navigator')
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # TODO: Define thresholds
        self.front_threshold = 0.6  # Stop if obstacle is within 0.6 meters
        self.side_threshold = 0.4   # Threshold for side clearance

    def scan_callback(self, msg):
        ranges = np.array(msg.ranges)
        
        # TODO 1: Clean data (remove inf/nan)
        # TurtleBot3 LiDAR returns 'inf' if out of range. We replace it with the max range (3.5m)
        ranges = np.where(np.isinf(ranges), 3.5, ranges)
        ranges = np.where(np.isnan(ranges), 3.5, ranges)
        ranges = np.where(ranges == 0.0, 3.5, ranges) # Filter false zeros
        
        # TODO 2: Define regions
        # The burger LiDAR has 360 points (0-359). 0 is straight ahead.
        # We slice the array to get the front, left, and right cones.
        front = np.concatenate((ranges[0:30], ranges[330:360])) 
        left = ranges[30:90]
        right = ranges[270:330]
        
        # Compute minimum distance in each region
        front_dist = np.min(front)
        left_dist = np.min(left)
        right_dist = np.min(right)
        
        twist = Twist()
        
        # TODO 3: Obstacle logic
        if front_dist < self.front_threshold:
            # obstacle in front -> Stop-on-obstacle behavior
            self.get_logger().info(f"Obstacle Ahead! Distance: {front_dist:.2f}m")
            twist.linear.x = 0.0 
            
            # TODO 4: Turn direction
            if left_dist > right_dist:
                # left clearer
                twist.angular.z = 0.5
            else:
                # right clearer
                twist.angular.z = -0.5
        else:
            # TODO 5: Forward motion & Wall Following
            twist.linear.x = 0.15
            
            # Task 4: Wall Following using Proportional Control
            # If walls are detected on the sides, calculate the error to stay centered
            if left_dist < 1.0 and right_dist < 1.0:
                error = left_dist - right_dist
                # Proportional gain (Kp) = 0.5
                twist.angular.z = 0.5 * error 
            else:
                twist.angular.z = 0.0
                
        self.publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = LidarNavigator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
