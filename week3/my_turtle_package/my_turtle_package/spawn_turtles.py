import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn
import time

class SwarmController(Node):
    def __init__(self):
        super().__init__('swarm_controller')
        self.spawn_turtle(2.0, 2.0, 0.0, 'turtle2')
        self.spawn_turtle(8.0, 8.0, 0.0, 'turtle3')
        self.spawn_turtle(2.0, 8.0, 0.0, 'turtle4')
        
        self.pub2 = self.create_publisher(Twist, 'turtle2/cmd_vel', 10)
        self.pub3 = self.create_publisher(Twist, 'turtle3/cmd_vel', 10)
        self.pub4 = self.create_publisher(Twist, 'turtle4/cmd_vel', 10)
        
        self.timer = self.create_timer(0.5, self.move_turtles)

    def spawn_turtle(self, x, y, theta, name):
        client = self.create_client(Spawn, 'spawn')
        while not client.wait_for_service(timeout_sec=1.0):
            pass
        req = Spawn.Request()
        req.x, req.y, req.theta, req.name = x, y, theta, name
        client.call_async(req)

    def move_turtles(self):
        msg2, msg3, msg4 = Twist(), Twist(), Twist()
        
        msg2.linear.x, msg2.angular.z = 1.5, 1.5 # Circle
        msg3.linear.x, msg3.angular.z = 2.0, 0.0 # Straight
        msg4.linear.x, msg4.angular.z = 0.0, 2.0 # Spin in place
        
        self.pub2.publish(msg2)
        self.pub3.publish(msg3)
        self.pub4.publish(msg4)

def main(args=None):
    rclpy.init(args=args)
    node = SwarmController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
