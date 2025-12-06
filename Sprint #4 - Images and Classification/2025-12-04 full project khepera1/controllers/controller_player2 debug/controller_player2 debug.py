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

def take_picture():
    from PIL import Image
    import numpy as np
    import os
    
    # Send request
    emitter.send("TAKE_PICTURE1")
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

    full_filename="../overhead_camera_controller/"+filename

    return full_filename  



player=2


receiver = robot.getDevice('receiver')
receiver.setChannel(player)
receiver.enable(timestep)

emitter = robot.getDevice('emitter')
emitter.setChannel(player+10)  # Robot 1 uses channel 1 and 11

print(f"robot {player} open grip")

# arm_up()
open_grip()

def forward_square(n):
    forward(3300*n)
    stop(200)

def backward_square(n):
    backward(3300*n)
    stop(200)

def left_degrees(angle):
    left(1100*angle//90) # ms
    stop(200) # ms

def right_degrees(angle):
    right(1100*angle//90) # ms
    stop(200) # ms

def grab():
    arm_down()    
    stop(300)
    close_grip()
    stop(300)
    arm_up()    
    stop(300)

def drop():
    arm_down()    
    stop(400)
    open_grip()
    stop(300)
    arm_up()    
    stop(300)

def make_move(move,player):
    state=Board(4,4) # make an empty state just for the coordinate functions
    start,end=move

    sr,sc=state.row(start),state.col(start)
    er,ec=state.row(end),state.col(end)

    # translate this into how many squares over and how many squares up

    if player==1:
        num_forward=sc+1
        num_up=4-sr
    else:
        num_forward=4-sc
        num_up=sr+1

    forward_square(num_forward)
    left_degrees(90)
    forward_square(num_up-0.2) # a little less, to not knock the stick over
    grab()

    # now what kind of move -- N, NE, or NW?
    if ec-sc == 0:  # N, S
        forward_square(1)
        drop()        
    elif ec-sc == 1:  # NE,SW
        if player==1:
            right_degrees(43)
        else:
            left_degrees(43)

        forward_square(1.4)
        drop()        
        backward_square(1.4)
        if player==1:
            left_degrees(43)
        else:
            right_degrees(43)

    elif ec-sc == -1: # NW,SE
        if player==1:
            left_degrees(40)
        else:
            right_degrees(40)

        forward_square(1.3)
        drop()        
        backward_square(1.3)
        if player==1:
            right_degrees(40)
        else:
            left_degrees(40)
    else:
        raise ValueError("You can't get there from here.")

    backward_square(num_up+1)


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


print("Ending 2.")