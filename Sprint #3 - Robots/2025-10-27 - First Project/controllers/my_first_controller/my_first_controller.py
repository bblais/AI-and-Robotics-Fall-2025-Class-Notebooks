"""my_first_controller controller."""

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

# Get number of devices
num_devices = robot.getNumberOfDevices()

print(f"Total devices: {num_devices}\n")

# List all devices
for i in range(num_devices):
    device = robot.getDeviceByIndex(i)
    print(f"Device {i}: {device.getName()} (Type: {device.getNodeType()})")


left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")

camera=robot.getDevice("overhead_camera")
camera.enable(timestep)


left_motor.setPosition(float("inf"))
right_motor.setPosition(float("inf"))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

sensors=[]
for i in range(8):  # from 0 to 7
    sensor_name = "ps" + str(i)
    sensor = robot.getDevice(sensor_name)
    sensor.enable(timestep)
    sensors.append(sensor)



print("Motors initialized.")
# Main loop:
# - perform simulation steps until Webots is stopping the controller
count=0
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()


    if count%30==0:
        print("Sensor values:", end=" ")
        for i,sensor in enumerate(sensors):
            sensor_value=sensor.getValue()
            print(f"ps{i}:{sensor_value:.2f}", end=" ")
        print()


    if sensors[0].getValue()>150:
        left_motor.setVelocity(-6.28)
        right_motor.setVelocity(6.28)
    else:
        left_motor.setVelocity(6.28)
        right_motor.setVelocity(6.28)



    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    count+=1

# Enter here exit cleanup code.

print("Controller has ended.")