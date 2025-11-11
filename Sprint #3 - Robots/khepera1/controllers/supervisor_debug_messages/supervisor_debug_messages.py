from controller import Robot, Camera, Emitter, Receiver, Keyboard,Supervisor

"""supervisor_debug_messages controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Supervisor()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())
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

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    # Check for incoming requests
    if receiver1.getQueueLength() > 0:
        print("here1")
        message = receiver1.getString()
        receiver1.nextPacket()
        print("\t",message)
        emitter1.send(f"got {message}")


    if receiver2.getQueueLength() > 0:
        print("here2")
        message = receiver2.getString()
        receiver2.nextPacket()
        print("\t",message)
        emitter2.send(f"got {message}")


# Enter here exit cleanup code.
