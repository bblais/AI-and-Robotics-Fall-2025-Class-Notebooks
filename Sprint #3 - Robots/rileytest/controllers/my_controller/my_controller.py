"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

timestep = int(robot.getBasicTimeStep())

num_devices = robot.getNumberOfDevices()
print(f"Total devices: {num_devices}\n")
print("="*70)

for i in range(num_devices):
    device = robot.getDeviceByIndex(i)
    name = device.getName()
    node_type = device.getNodeType()
    
    print(f"\nDevice {i}: {name}")
    print(f"  Type: {node_type}")
