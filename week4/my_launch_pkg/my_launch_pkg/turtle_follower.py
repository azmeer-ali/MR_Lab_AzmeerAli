#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math


class TurtleFollower(Node):
    """Node that makes turtle2 follow turtle1."""

    def __init__(self):
        super().__init__('turtle_follower')
        
        # Store turtle1's pose
        self.turtle1_pose = None
        self.turtle2_pose = None
        
        # Control parameters
        self.linear_speed = 2.0  # m/s
        self.angular_speed = 4.0  # rad/s
        self.distance_threshold = 1.0# meters
        self.orientation_threshold = 0.05  # rad
        
        # Subscribe to turtle1's pose
        self.turtle1_sub = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.turtle1_pose_callback,
            10
        )
        
        # Subscribe to turtle2's pose
        self.turtle2_sub = self.create_subscription(
            Pose,
            '/turtle2/pose',
            self.turtle2_pose_callback,
            10
        )
        
        # Publish velocity commands to turtle2
        self.turtle2_pub = self.create_publisher(
            Twist,
            '/turtle2/cmd_vel',
            10
        )
        
        # Create timer to run control loop
        self.timer = self.create_timer(0.1, self.control_loop)
        
        self.get_logger().info('Turtle Follower Node started')

    def turtle1_pose_callback(self, msg):
        """Callback for turtle1's pose."""
        self.turtle1_pose = msg

    def turtle2_pose_callback(self, msg):
        """Callback for turtle2's pose."""
        self.turtle2_pose = msg

    def control_loop(self):
        """Main control loop to make turtle2 follow turtle1."""
        if self.turtle1_pose is None or self.turtle2_pose is None:
            return
        
        # Calculate distance and angle to target
        dx = self.turtle1_pose.x - self.turtle2_pose.x
        dy = self.turtle1_pose.y - self.turtle2_pose.y
        distance = math.sqrt(dx**2 + dy**2)
        
        # Create velocity command
        twist_cmd = Twist()

        # Move toward turtle1 while far, then align with turtle1's heading when close.
        if distance > self.distance_threshold:
            desired_angle = math.atan2(dy, dx)
            angle_diff = desired_angle - self.turtle2_pose.theta
            angle_diff = math.atan2(math.sin(angle_diff), math.cos(angle_diff))
            twist_cmd.linear.x = self.linear_speed
            twist_cmd.angular.z = self.angular_speed * angle_diff
        else:
            twist_cmd.linear.x = 0.0
            heading_diff = self.turtle1_pose.theta - self.turtle2_pose.theta
            heading_diff = math.atan2(math.sin(heading_diff), math.cos(heading_diff))

            if abs(heading_diff) > self.orientation_threshold:
                twist_cmd.angular.z = self.angular_speed * heading_diff
            else:
                twist_cmd.angular.z = 0.0
        
        # Publish velocity command
        self.turtle2_pub.publish(twist_cmd)


def main(args=None):
    rclpy.init(args=args)
    follower = TurtleFollower()
    
    try:
        rclpy.spin(follower)
    except KeyboardInterrupt:
        pass
    finally:
        follower.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
