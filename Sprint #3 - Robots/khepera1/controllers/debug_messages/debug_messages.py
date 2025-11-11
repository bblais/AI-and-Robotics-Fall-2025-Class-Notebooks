"""debug_messages controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

robot.step(1)
raise ValueError
# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

receiver = robot.getDevice('receiver')
receiver.setChannel(1)
receiver.enable(timestep)


print(dir(receiver))
print(receiver.getChannel())


emitter = robot.getDevice('emitter')
emitter.setChannel(11)  # Robot 1 uses channel 1 and 11
print(emitter.getChannel())



# Main loop:
# - perform simulation steps until Webots is stopping the controller
i=0
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    message=f"ping {i}"
    i+=1

    print("1 sending ",message)
    emitter.send(message)
    waiting_for_confirmation=True

    while waiting_for_confirmation:
        if robot.step(timestep) == -1:
            break
            
        if receiver.getQueueLength() > 0:
            message=receiver.getString()
            
            print("1 confirm ",message)
            receiver.nextPacket()
            waiting_for_confirmation = False



    robot.step(1000)

# Enter here exit cleanup code.
