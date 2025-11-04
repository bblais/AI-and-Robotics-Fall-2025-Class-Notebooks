"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot


def wait(sec):
    start_time = robot.getTime()
    while start_time + sec > robot.getTime():
        val=robot.step(timestep)
        if val==-1:
            return -1

def open_gripper():
    motors['gripper::right'].setPosition(0.5)

def close_gripper():
    motors['gripper::right'].setTorque(-0.2)

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

num_devices = robot.getNumberOfDevices()
print(f"Total devices: {num_devices}\n")
print("="*70)

for i in range(num_devices):
    device = robot.getDeviceByIndex(i)
    name = device.getName()
    node_type = device.getNodeType()
    
    print(f"\nDevice {i}: {name}")
    print(f"  Type: {node_type}")

motors={}
for name in [f'motor {i}' for i in range(1,7)]+['gripper::right','gripper::left']:
    motors[name]=robot.getDevice(name)

print(motors.keys())

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    wait(.5)
    close_gripper()
    wait(.5)
    open_gripper()
    wait(.5)
    close_gripper()

    motors['motor 1'].setPosition(1.55)
    motors['motor 2'].setPosition(1.12)
    open_gripper()
    wait(1.5)


    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
