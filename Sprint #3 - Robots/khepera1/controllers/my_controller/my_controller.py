from controller import Robot, Supervisor

TIME_STEP = 50
OPEN_GRIP = 0.029
CLOSED_GRIP = 0.005

def reset_home():
    robot_node = robot.getSelf()
    robot_node.getField("translation").setSFVec3f([-.6, -.6, 0])
    robot_node.getField("rotation").setSFRotation([0, 0, 1, 0])  # No rotation
    
robot = Supervisor()
# Reset robot position and orientation


# Get number of devices
num_devices = robot.getNumberOfDevices()

print(f"Total devices: {num_devices}\n")

# List all devices
for i in range(num_devices):
    device = robot.getDeviceByIndex(i)
    print(f"Device {i}: {device.getName()} (Type: {device.getNodeType()})")


# robot = Robot()

motor = robot.getDevice("motor")
left_grip = robot.getDevice("left grip")
right_grip = robot.getDevice("right grip")
ds = robot.getDevice("ds")  # distance sensor in the gripper
camera=robot.getDevice("camera")
camera.enable(TIME_STEP)

# Get a handler to the motors and set target position to infinity (speed control)
left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

ds.enable(TIME_STEP)

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

        
def stop(amount_of_time=TIME_STEP):
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
        
reset_home()
arm_up()
open_grip()

while robot.step(TIME_STEP) != -1:

    forward(2000) # ms
    
    arm_down()

    stop(500) # ms


    left(400) # ms

    close_grip()
    
    backward(2000)
    
    stop()
    break
    

