from controller import Robot, Supervisor,Keyboard
import struct

OPEN_GRIP = 0.029
CLOSED_GRIP = 0.005


    
robot = Robot()
# Reset robot position and orientation
# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())


# Get number of devices
num_devices = robot.getNumberOfDevices()

# print(f"Total devices: {num_devices}\n")

# # List all devices
# for i in range(num_devices):
#     device = robot.getDeviceByIndex(i)
#     print(f"Device {i}: {device.getName()} (Type: {device.getNodeType()})")


# robot = Robot()

motor = robot.getDevice("motor")
left_grip = robot.getDevice("left grip")
right_grip = robot.getDevice("right grip")
ds = robot.getDevice("ds")  # distance sensor in the gripper
camera=robot.getDevice("camera")
camera.enable(timestep)

# Get a handler to the motors and set target position to infinity (speed control)
left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

ds.enable(timestep)

i = 0

def forward(amount_of_time):
    left_motor.setVelocity(10)
    right_motor.setVelocity(10)
    robot.step(amount_of_time)
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)

def backward(amount_of_time):
    left_motor.setVelocity(-10)
    right_motor.setVelocity(-10)
    robot.step(amount_of_time)
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)

        
def stop(amount_of_time=timestep):
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)
    robot.step(amount_of_time)

def left(amount_of_time):
    left_motor.setVelocity(-4.7)
    right_motor.setVelocity(4.7)
    robot.step(amount_of_time)
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)

def right(amount_of_time):
    left_motor.setVelocity(4.7)
    right_motor.setVelocity(-4.7)
    robot.step(amount_of_time)
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)
   
def arm_down():
    motor.setPosition(0.0) 
def arm_up():
    motor.setPosition(-1.4)
        
def close_grip():
    left_grip.setPosition(CLOSED_GRIP)
    right_grip.setPosition(CLOSED_GRIP)

def open_grip():
    left_grip.setPosition(OPEN_GRIP)
    right_grip.setPosition(OPEN_GRIP)

def take_picture():
    from PIL import Image
    import numpy as np
    import os
    
    # Send request
    emitter.send("TAKE_PICTURE2")
    waiting_for_image = True
    
    # Wait for response
    while waiting_for_image:
        if robot.step(timestep) == -1:
            return None
            
        if receiver.getQueueLength() > 0:
            filename=receiver.getString()
            
            print("loading ",filename,os.getcwd())
            receiver.nextPacket()
            img = Image.open("../overhead_camera_controller/"+filename)
            im = np.array(img)            
            waiting_for_image = False

    return im    
    

player=2


receiver = robot.getDevice('receiver')
receiver.setChannel(player)
receiver.enable(timestep)



emitter = robot.getDevice('emitter')
emitter.setChannel(player+10)  # Robot 1 uses channel 1 and 11


im=take_picture()
print(im.shape)

print("robot 2 open grip")

# arm_up()
open_grip()

while robot.step(timestep) != -1:

    forward(2000) # ms
    
    arm_down()

    stop(500) # ms


    left(800) # ms
    forward(2500) # ms

    close_grip()
    stop(200) # ms
    arm_up()
    backward(2000)
    
    stop()
    im=take_picture()
    print(im.shape)

    break
    

