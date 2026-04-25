Lab 2 Report: ROS 2 CLI Tools, Topics, Services, and RQT
Student: Azmeer Ali
Course: MCT-454L Mobile Robotics

Steps Followed:
_Simulation Launch: Initiated the ROS 2 environment by sourcing Humble and launched the core simulation using ros2 run turtlesim turtlesim_node.
_Teleoperation & Monitoring: Activated the turtle_teleop_key node in a separate terminal to control the turtle via keyboard inputs. Simultaneously, I monitored the active data streams by using ros2 topic list and echoing the /turtle1/pose topic to observe real-time coordinate updates.
_Direct CLI Commands: Experimented with direct topic publishing by sending geometry_msgs/msg/Twist velocity commands using ros2 topic pub. I also executed a command-line service call to /reset to return the turtle to its origin.
_RQT Graphical Interface: Transitioned from the CLI to the rqt GUI to visually explore the ROS 2 ecosystem, specifically utilizing the Plugins menu to view the node graph and active services.
_Multi-Turtle Interaction: Using the Services tab in rqt, I called the /spawn service, specifying distinct $x$, $y$, and $\theta$ values to instantiate a second turtle. I then identified its unique velocity topic (e.g., /turtle2/cmd_vel) and successfully controlled its movements.

Observations:
_Real-time Responsiveness: The Turtlesim environment updates instantaneously in response to both CLI terminal commands and graphical rqt inputs.
_Node Independence: The ROS 2 architecture ensures that nodes and topics remain segregated; by publishing exclusively to the second turtle's topic, it was observed that it moves completely independently of the first turtle.
_GUI vs. CLI Efficiency: While the terminal is effective for rapid testing, the rqt interface provides a significantly more structured and intuitive method for calling services (like /spawn), eliminating the need to manually format complex parameter strings.
