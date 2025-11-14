from controller import Robot, Camera, Emitter, Receiver, Keyboard,Supervisor
from datetime import datetime
import os
from numpy import pi
from Game import *

sys.path.insert(0, os.path.abspath('../../game/'))
print(sys.path)
from my_game import *
state=initial_state()

def reset_home():
    robot_node = robot.getSelf()
    robot_node.getField("translation").setSFVec3f([.6, .60, 0.0001])
    robot_node.getField("rotation").setSFRotation([0, 0, 1, 0])  # No rotation
    
def row_col_to_translation(r,c):
    x=-.375+.25*c
    y=-.375+.25*(3-r)
    return x,y
        



def add_piece(x,y,p):
    # Define the position where you want to create the object
    #x, y, z = -0.256793, -0.452234, 0.0300022
    
    if p==0:
        return
    elif p==1:
        color_name='RED'
        r,g,b=1, 0.155604, 0.246125
    elif p==2:
        color_name='BLUE'
        r,g,b=0.246125, 0.155604, 1
    else:
        raise ValueError("Not implemented")
        
    # VRML string for the red stick
    red_stick_string = f'''DEF {color_name}_STICK Solid {{
      translation {x} {y} 0
      rotation -1.1787095735033249e-11 1 4.892081418304912e-11 4.693215650486149e-06
      children [
        Pose {{
          rotation 1 0 0 3.14159
          children [
            DEF STICK_SHAPE Shape {{
              appearance PBRAppearance {{
                baseColor {r} {g} {b}
                roughness 0.783569247
                metalness 0
              }}
              geometry Cylinder {{
                height 0.06
                radius 0.016
              }}
            }}
          ]
        }}
      ]
      name "{color_name.lower()} stick"
      contactMaterial "stick"
      boundingObject Cylinder {{
                height 0.06
                radius 0.016
      }}
      physics Physics {{
        density 2
      }}
    }}'''
    
    # Get the root node and import the object
    root_node = supervisor.getRoot()
    children_field = root_node.getField('children')
    children_field.importMFNodeFromString(-1, red_stick_string)
    
    


supervisor=robot = Supervisor()
timestep = int(robot.getBasicTimeStep())

root = supervisor.getRoot()
children_field = root.getField('children')

robots = {}
for i in range(children_field.getCount()):
    node = children_field.getMFNode(i)
    print(node.getTypeName() )
    if node.getTypeName() == 'Khepera1':
        name_field = node.getField('name')
        robot_name = name_field.getSFString()
        print("name:",robot_name)
        robots[robot_name]=node
print(len(robots),"found")
print(robots)

for name in robots:

    robot1_translation = robots[name].getField('translation')
    robot1_rotation = robots[name].getField('rotation')

    if name=='player 1':
        r,c=4,-1
        rot=[0, 1, 0, 0]
    elif name=='player 2':
        r,c=-1,4
        rot=[0, 0, 1, pi]
    else:
        raise ValueError("You can't get there from here.")
    
    x,y=row_col_to_translation(r,c)
    robot1_translation.setSFVec3f([x,y, 0.0001])
    robot1_rotation.setSFRotation(rot)

# Get devices
camera = robot.getDevice('overhead_camera')
camera.enable(timestep)

receiver1 = robot.getDevice('receiver1')
receiver1.setChannel(11)
receiver1.enable(timestep)

emitter1 = robot.getDevice('emitter1')
emitter1.setChannel(1)

receiver2 = robot.getDevice('receiver2')
receiver2.setChannel(12)
receiver2.enable(timestep)

emitter2 = robot.getDevice('emitter2')
emitter2.setChannel(2)


# Get the root node and search for RectangleArena
root = supervisor.getRoot()
children_field = root.getField("children")
arena = None
for i in range(children_field.getCount()):
    node = children_field.getMFNode(i)
    if node.getTypeName() == "RectangleArena":
        arena = node
        break

if arena is None:
    raise ValueError("Error: RectangleArena not found!")        

floor_size_field = arena.getField("floorSize")
        
num_rows,num_columns = state.shape
floor_size_field.setSFVec2f([(num_columns+2)*0.25, 
                               (num_rows+2)*0.25])

num_rows,num_columns = state.shape
floor_size_field.setSFVec2f([(4+2)*0.25, 
                               (4+2)*0.25])


floor=None
for i in range(children_field.getCount()):
    node = children_field.getMFNode(i)
    if node.getTypeName() == "Floor":
        floor = node
        break


# Navigate to the ImageTexture url field
appearance = floor.getField('appearance').getSFNode()
base_color_map = appearance.getField('baseColorMap').getSFNode()
url_field = base_color_map.getField('url')

# Change the texture URL
R,C=state.shape
texture_fname=f"../textures/squares{R}x{C}.png"
if not os.path.exists("../"+texture_fname):
    texture_fname=f"../textures/blank.png"
url_field.setMFString(0, texture_fname)

for r in range(state.shape[0]):
    for c in range(state.shape[1]):
        x,y=row_col_to_translation(r,c)
        add_piece(x,y,state[r,c])




while robot.step(timestep) != -1:

        
    # Check for incoming requests
    if receiver1.getQueueLength() > 0:
        print("here1")
        message = receiver1.getString()
        receiver1.nextPacket()
        
        if "TAKE_PICTURE" in message:
            print("in overhead1:",message)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            filename = f"image_{timestamp}.png"
            
            print("from robot1")
            
            print("saving ",filename,os.getcwd())

            # Save image
            camera.saveImage(filename, 100)  # 100 is quality            
            
            # Send image data back
            # First send metadata
            emitter1.send(filename)

    if receiver2.getQueueLength() > 0:
        message = receiver2.getString()
        receiver2.nextPacket()
        
        print("here2")
        if "TAKE_PICTURE" in message:
            print("in overhead2:",message)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            filename = f"image_{timestamp}.png"
            
            
            print("from robot2")
            print("saving ",filename,os.getcwd())

            # Save image
            camera.saveImage(filename, 100)  # 100 is quality            
            
            # Send image data back
            # First send metadata
            emitter2.send(filename)
