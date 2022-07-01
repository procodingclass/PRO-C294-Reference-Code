from controller import Robot

robot=Robot()

timestep=64

flag= 0

leg1=robot.getDevice("front_left")
leg2=robot.getDevice("front_right")
leg3=robot.getDevice("back_left")
leg4=robot.getDevice("back_right")

receiver= robot.getDevice("receiver")
receiver.enable(timestep)
received_data=0

def add_delay(num_timestep):
    time_counter = 0
    while robot.step(timestep)  !=  -1:
        if time_counter >= num_timestep:
            break
        time_counter += 1
        
def walk(flag):
    if(flag%10==0):
        leg1.setPosition(-0.3)
    elif(flag%10==2):
        leg2.setPosition(-0.3)
    elif(flag%10==4):
        leg4.setPosition(-0.3)
    elif(flag%10==6):
        leg3.setPosition(-0.3)
    elif(flag%10==7):
        leg1.setPosition(0.2)
        leg2.setPosition(0.2)
        leg4.setPosition(0.2)
        leg3.setPosition(0.2)

def sit():
    leg1.setPosition(0)
    leg2.setPosition(0)
    leg4.setPosition(-0.37)
    leg3.setPosition(-0.37)
    add_delay(3)

def stand():
    leg1.setPosition(0)
    leg2.setPosition(0)
    leg4.setPosition(0)
    leg3.setPosition(0)
    add_delay(3)
    
while (robot.step(timestep) !=-1):    
    if receiver.getQueueLength() > 0: 
        received_data = receiver.getData().decode()   
        print(received_data, type(received_data))
        receiver.nextPacket()

    if received_data == "sit":
        sit()
        received_data=" "
        
    elif received_data == "stand":
        stand()
        received_data=" "
        
    elif received_data == "walk":
        flag = flag + 1
        while(flag%30 != 0):
            walk(flag)
            flag=flag+1
            add_delay(3)
        received_data=" "