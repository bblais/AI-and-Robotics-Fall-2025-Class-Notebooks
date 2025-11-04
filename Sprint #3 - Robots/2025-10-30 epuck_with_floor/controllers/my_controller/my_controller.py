"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller

num_devices = robot.getNumberOfDevices()
print(f"Total devices: {num_devices}\n")
print("="*70)

for i in range(num_devices):
    device = robot.getDeviceByIndex(i)
    name = device.getName()
    node_type = device.getNodeType()
    
    print(f"\nDevice {i}: {name}")
    print(f"  Type: {node_type}")

left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")
left_motor.setPosition(float("inf"))
right_motor.setPosition(float("inf"))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

gs0 = robot.getDevice("gs0")
gs0.enable(timestep)

gs1 = robot.getDevice("gs1")
gs1.enable(timestep)

gs2 = robot.getDevice("gs2")
gs2.enable(timestep)

sensors=[]
for i in range(8):  # from 0 to 7
    sensor_name = "ps" + str(i)
    sensor = robot.getDevice(sensor_name)
    sensor.enable(timestep)
    sensors.append(sensor)



# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.
    left_motor.setVelocity(3.28)
    right_motor.setVelocity(3.28)

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    
    value0=gs0.getValue()
    value1=gs1.getValue()
    value2=gs2.getValue()
    
    print(f"{value0:.1f},{value1:.1f},{value2:.1f}")

# Enter here exit cleanup code.

