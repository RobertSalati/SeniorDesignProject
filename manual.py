import numpy as np;
global lengths;

lengths = np.array([0, 0, 0, 0])

kit1 = MotorKit(address=0x60);
kit2 = MotorKit(address=0x61);

class Motor:
    length = 0;

    def __init__(self,num):
        self.num = num;

    def moveMotor(steps, motorNum, dir):

    if motorNum == 1:            # Motor 1
        if dir == 0:
            for i in range(steps):
                kit1.stepper1.onestep(direction=stepper.FORWARD);
        if dir == 1:
            for i in range(steps):
                kit1.stepper1.onestep(direction=stepper.BACKWARD);
     
    if motorNum == 2:           # Motor 2
        if dir == 0:
            for i in range(steps):
                kit1.stepper2.onestep(direction=stepper.FORWARD);
        if dir == 1:
            for i in range(steps):
                kit1.stepper2.onestep(direction=stepper.BACKWARD);
    
    if motorNum == 3:            # Motor 3
        if dir == 0:
            for i in range(steps):
                kit2.stepper1.onestep(direction=stepper.FORWARD);
        if dir == 1:
            for i in range(steps):
                kit2.stepper1.onestep(direction=stepper.BACKWARD);
    
    if motorNum == 4:            # Motor 4
        if dir == 0:
            for i in range(steps):
                kit2.stepper2.onestep(direction=stepper.FORWARD);
        if dir == 1:
            for i in range(steps):
                kit2.stepper2.onestep(direction=stepper.BACKWARD);

    #def moveMotor(steps, dir):
    #    if (num == 1 or num == 2):
    #        if dir == 0:
    #            for i in range(steps):
    #                kit1.stepper1.onestep(direction=stepper.FORWARD);
    #        if dir == 1:
    #            for i in range(steps):
    #                kit1.stepper1.onestep(direction=stepper.BACKWARD);
    #    elif (num == 3 or num == 4):
    #                    if dir == 0:
    #            for i in range(steps):
    #                kit1.stepper1.onestep(direction=stepper.FORWARD);
    #        if dir == 1:
    #            for i in range(steps):
    #                kit1.stepper1.onestep(direction=stepper.BACKWARD);


