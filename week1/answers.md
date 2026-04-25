Define: node, topic, package, workspace.
Node: A process that performs computation.
Topic: A named communication channel for streaming messages between nodes.
Package: A folder containing ROS 2 code, dependencies, and build information.
Workspace: A main folder that contains one or more ROS 2 packages as well as their build outputs.

Explain why sourcing is required. What happens if you do not source a workspace?
Sourcing updates your terminal's environment variables so it knows where to find ROS 2 commands and your newly built packages. If you do not source, commands like ros2 won't be recognized, and ROS will not be able to locate your custom packages or executables, leading to "command not found" or "package not found" errors.3. What is the purpose of colcon build? What folders does it generate?
The colcon build command is used to compile and build the packages within a ROS 2 workspace. It generates the build/, install/, and log/ folders.4. Explain what the entry_points console script does in setup.py.
The entry_points section maps a command-line name to a specific Python function. This registers the node as an executable, allowing ROS 2 to know exactly what script to run when using the ros2 run command.

Draw a diagram showing one publisher and one subscriber connected by a topic.
+-------------------+                    +--------------------+
|      Node A       |                    |       Node B       |
|    (Publisher)    |                    |    (Subscriber)    |
|                   |                    |                    |
| publishes msgs    |   /my_topic        | receives msgs      |
| at 10 Hz          +------------------->| and acts on them   |                  
+-------------------+                    +--------------------+
