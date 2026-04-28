import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class GoToGoal(Node):
    def __init__(self):
        super().__init__('go_to_goal')
        self.publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.subscriber = self.create_subscription(Pose, 'turtle1/pose', self.pose_callback, 10)
        self.pose = Pose()
        
        # Target Goal
        self.goal_x = 8.0
        self.goal_y = 8.0
        self.timer = self.create_timer(0.1, self.move_to_goal)

    def pose_callback(self, msg):
        self.pose = msg

    def move_to_goal(self):
        msg = Twist()
        distance = math.sqrt(pow((self.goal_x - self.pose.x), 2) + pow((self.goal_y - self.pose.y), 2))
        angle_to_goal = math.atan2(self.goal_y - self.pose.y, self.goal_x - self.pose.x)
        
        if distance >= 0.1:
            msg.linear.x = 1.0 * distance
            msg.angular.z = 4.0 * (angle_to_goal - self.pose.theta)
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            self.get_logger().info('Goal Reached!')
            self.timer.cancel()
            
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = GoToGoal()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
