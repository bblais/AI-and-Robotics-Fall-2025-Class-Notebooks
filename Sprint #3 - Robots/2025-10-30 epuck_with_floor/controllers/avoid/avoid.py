"""my_first_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from numpy import sum,cos,sin,array,sqrt,degrees,arctan2,pi,abs

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

gyro = robot.getDevice("gyro")
gyro.enable(timestep)

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

# Sensor orientations (in radians)
sensor_orientations =array([1.27, 0.77, 0.00, 5.21, 4.21, 3.14159, 2.37, 1.87])

use=[0,1,2,5,6,7]
sensor_orientations=sensor_orientations[use]

print("Motors initialized.")
# Main loop:
# - perform simulation steps until Webots is stopping the controller
count=0
while robot.step(timestep) != -1:

    
    # Read the sensors:
    sensor_values = array([sensor.getValue() for sensor in sensors])
    
    if count%30==0:
        print("Sensor values:", end=" ")
        for i, val in enumerate(sensor_values):
            print(f"ps{i}:{val:.2f}", end=" ")
        print(f"gyro {gyro.getValues()}")
        print()

    sensor_values=sensor_values[use]
    # Calculate obstacle strengths (subtract baseline)
    vector_x=(sensor_values*cos(sensor_orientations)).sum()
    vector_y=(sensor_values*sin(sensor_orientations)).sum()
    magnitude=sqrt(vector_x**2+vector_y**2)
    obstacle_angle = degrees(arctan2(vector_y, vector_x))
    if count%30==0:
        print(sensor_values,sensor_orientations)
        print(f"\tvx,vy {vector_x},{vector_y},mag {magnitude} angle {obstacle_angle}")
    
    if magnitude>230:
        
        if obstacle_angle>90: # turn right
            left_speed=4
            right_speed=-4
        else: # turn left
            left_speed=-4
            right_speed=4

    else:        
        left_speed=4
        right_speed=4
            
    if count%30==0:
        print(f"\tMotors - Left: {left_speed:.2f}, Right: {right_speed:.2f}")

    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)
    
    count+=1

# Enter here exit cleanup code.

print("Controller has ended.")