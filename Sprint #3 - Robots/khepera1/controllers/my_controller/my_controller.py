from controller import Robot, Supervisor

TIME_STEP = 50
OPEN_GRIP = 0.029
CLOSED_GRIP = 0.005

def reset_home():
    robot_node = robot.getSelf()
    robot_node.getField("translation").setSFVec3f([-.5, -.67, 0])
    robot_node.getField("rotation").setSFRotation([0, 0, 1, 0])  # No rotation
    
    
def add_piece(x,y,z):
    # Define the position where you want to create the object
    #x, y, z = -0.256793, -0.452234, 0.0300022
    
    # VRML string for the red stick
    red_stick_string = f'''DEF RED_STICK Solid {{
      translation {x} {y} {z}
      rotation -1.1787095735033249e-11 1 4.892081418304912e-11 4.693215650486149e-06
      children [
        Pose {{
          rotation 1 0 0 3.14159
          children [
            DEF STICK_SHAPE Shape {{
              appearance PBRAppearance {{
                baseColor 1 0.155604 0.246125
                roughness 0.783569247
                metalness 0
              }}
              geometry Cylinder {{
                height 0.06
                radius 0.008
              }}
            }}
          ]
        }}
      ]
      name "red stick"
      contactMaterial "stick"
      boundingObject Box {{
        size 0.013 0.013 0.06
      }}
      physics Physics {{
        density 100
      }}
    }}'''
    
    # Get the root node and import the object
    root_node = supervisor.getRoot()
    children_field = root_node.getField('children')
    children_field.importMFNodeFromString(-1, red_stick_string)
    
    
    
supervisor=robot = Supervisor()
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

add_piece(0.256793, -0.452234, 0)

arm_up()
open_grip()

while robot.step(TIME_STEP) != -1:

    forward(2000) # ms
    
    arm_down()

    stop(500) # ms


    left(600) # ms
    forward(2000) # ms

    close_grip()
    
    backward(2000)
    
    stop()
    break
    

