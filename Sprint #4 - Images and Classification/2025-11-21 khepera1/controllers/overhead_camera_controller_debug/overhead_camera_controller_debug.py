from controller import Robot, Camera, Emitter, Receiver, Keyboard,Supervisor
from datetime import datetime
import os
from numpy import pi
from Game import *

position_variation=0.03
position_variation=0.00


sys.path.insert(0, os.path.abspath('../../game/'))
print(sys.path)
from my_game import *
state=initial_state()

from numpy.random import rand

def reset_home():
    robot_node = robot.getSelf()
    robot_node.getField("translation").setSFVec3f([.6, .60, 0.0001])
    robot_node.getField("rotation").setSFRotation([0, 0, 1, 0])  # No rotation
    
def row_col_to_translation(r,c,board_shape=(4,4)):
    x=-.5+c/board_shape[1]+1/2/board_shape[1]
    y=.5-r/board_shape[0]-1/2/board_shape[0]
    return x,y



def add_piece(x,y,p):
    # Define the position where you want to create the object
    #x, y, z = -0.256793, -0.452234, 0.0300022
    
    x+=(2*rand()-1)*position_variation
    y+=(2*rand()-1)*position_variation

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
    
from PIL import Image

def create_checkered_board(width, height, board_cols, board_rows, output_file):
    """
    Create a checkered board image with alternating white and light gray squares.
    
    Args:
        width: Image width in pixels
        height: Image height in pixels
        board_cols: Number of columns in the board
        board_rows: Number of rows in the board
        output_file: Output PNG filename
    """
    # Create a new image with white background
    img = Image.new('RGB', (width, height), color='white')
    pixels = img.load()
    
    # Calculate square dimensions
    square_width = width / board_cols
    square_height = height / board_rows
    
    # Define colors
    white = (255, 255, 255)
    light_gray = (150, 150, 150)
    
    # Fill in the squares
    for row in range(board_rows):
        for col in range(board_cols):
            # Determine color based on position (checkerboard pattern)
            if (row + col) % 2 == 0:
                color = white
            else:
                color = light_gray
            
            # Calculate pixel boundaries for this square
            x_start = int(col * square_width)
            x_end = int((col + 1) * square_width)
            y_start = int(row * square_height)
            y_end = int((row + 1) * square_height)
            
            # Fill the square
            for y in range(y_start, y_end):
                for x in range(x_start, x_end):
                    pixels[x, y] = color
    
    # Save the image
    img.save(output_file)
    print(f"Image saved as {output_file}")
    


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
    create_checkered_board(2048, 2048, C, R, 
                       f'../../textures/squares{R}x{C}.png')

if not os.path.exists("../"+texture_fname):
    texture_fname=f"../textures/blank.png"

url_field.setMFString(0, texture_fname)

for r in range(state.shape[0]):
    for c in range(state.shape[1]):
        x,y=row_col_to_translation(r,c,state.shape)
        add_piece(x,y,state[r,c])


current_player=1
first_turn=True

# Enable keyboard
keyboard = Keyboard()
keyboard.enable(timestep)

count=1
while robot.step(timestep) != -1:

    key=keyboard.getKey()
    if (key==Keyboard.CONTROL+ord('B')):
        print('Ctrl+B is pressed')

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        filename = f"images/image_{timestamp}.png"
        print("saving ",filename,os.getcwd())
        # Save image
        camera.saveImage(filename, 100)  # 100 is quality            
            
