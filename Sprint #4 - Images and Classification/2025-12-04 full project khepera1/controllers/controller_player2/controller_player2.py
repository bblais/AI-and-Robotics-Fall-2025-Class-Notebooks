from controller import Robot, Supervisor,Keyboard
import struct
from Game import *
import sys
sys.path.insert(0, os.path.abspath('../../game/'))
print(sys.path)
from my_game import *
import ast

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
    robot.step(int(amount_of_time))
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)

def backward(amount_of_time):
    left_motor.setVelocity(-10)
    right_motor.setVelocity(-10)
    robot.step(int(amount_of_time))
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)

        
def stop(amount_of_time=timestep):
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)
    robot.step(int(amount_of_time))

def left(amount_of_time):
    left_motor.setVelocity(-4.7)
    right_motor.setVelocity(4.7)
    robot.step(int(amount_of_time))
    left_motor.setVelocity(0)
    right_motor.setVelocity(0)

def right(amount_of_time):
    left_motor.setVelocity(4.7)
    right_motor.setVelocity(-4.7)
    robot.step(int(amount_of_time))
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



player=2


receiver = robot.getDevice('receiver')
receiver.setChannel(player)
receiver.enable(timestep)

emitter = robot.getDevice('emitter')
emitter.setChannel(player+10)  # Robot 1 uses channel 1 and 11

print(f"robot {player} open grip")

# arm_up()
open_grip()


def make_move(move,player):
    # do the robot stuff here
    pass



def read_state(filename,show_images=False):
    from classy import CSC
    from pylab import imread,figure,subplot,imshow,title,axis,uint8,atleast_2d
    from Game import Board

    C=CSC()
    C.load('../../game/board_CSC.json')
    
    #filename='images/image_20251203_113954_903464.png'
    #show_images=True
    
    im=imread(filename)
    im=(im*255).astype(uint8)
    
    if show_images:
        figure()
        imshow(im)
    
    count=1
    if show_images:
        figure()
    
    start_r,start_c=230,230
    rows_per_square,cols_per_square=140,140



    state=Board(4,4)
    for r in range(4):
        for c in range(4):
            r1=start_r+rows_per_square*r
            r2=start_r+rows_per_square*(r+1)
            c1=start_c+cols_per_square*c
            c2=start_c+cols_per_square*(c+1)
            
            subimage=im[r1:r2,c1:c2]
            vector=subimage.ravel()
            prediction=C.predict(atleast_2d(vector))[0]
            state[r,c]=prediction
            
            if show_images:
                subplot(4,4,count)
                imshow(subimage)
                title(prediction)
                axis('off')
                
            count+=1
    
    return state


def get_move(state):
    if not state in T:
        print("state not in table")
        move=random_move(state,player)
    else:
        move=top_choice(T[state])

    return move


#  0  1  2  3
#  4  5  6  7
#  8  9 10 11
# 12 13 14 15

move=None
T=LoadTable(f'../../game/breakthrough_4x4_skittles_agent{player}_table.json')


def wait_for_turn():
    # clear out old messages    
    while receiver.getQueueLength()>0:
        receiver.nextPacket()

    state=initial_state()
    waiting_for_turn = True
    while waiting_for_turn:
        if robot.step(timestep) == -1:
            return None
        if receiver.getQueueLength() > 0:
            waiting_for_turn=False
            repr_string=receiver.getString()
            result = ast.literal_eval(repr_string)
            state.board=result
            receiver.nextPacket()

        
    return state
 

def clear_messages():
    # clear out old messages    
    while receiver.getQueueLength()>0:
        receiver.nextPacket()        

while robot.step(timestep) != -1:

    wait_for_turn()

    state=read_state('../overhead_camera_controller/images/current_board.png')
    print("Read state:")
    print(state)

    move=get_move(state)
    print("move is ",move)


    make_move(move,player)


    clear_messages()