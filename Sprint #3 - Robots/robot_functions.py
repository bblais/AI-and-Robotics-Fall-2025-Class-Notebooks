def Wait(T):
    while robot.step(timestep) != -1:
        elapsed_time += timestep / 1000.0  # timestep is in milliseconds
        
        if elapsed_time >= T:
            break


def forward(speed):
    left_motor.setVelocity(speed)
    right_motor.setVelocity(speed)

def stop():
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)


forward(3.0)
Wait(2.0)
stop()


