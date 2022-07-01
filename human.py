from controller import Robot

robot = Robot()
timestep = 64
emitter=robot.getDevice("emitter")

def add_delay(num_timestep):
    time_counter = 0
    while robot.step(timestep)  !=  -1:
        if time_counter >= num_timestep:
            break
        time_counter += 1

i=0
commands=["sit","stand","walk","stand"]

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    
    while(i<20):
        info = bytes(commands[i%4], 'utf-8')
        emitter.send(info)
        add_delay(50)
        i=i+1