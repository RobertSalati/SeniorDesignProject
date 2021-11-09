import picamera as cam;
import numpy as np;
from adafruit_motorkit import MotorKit;
from adafruit_motor import stepper;

l = 3;      # length of the shelf (x axis) [m]
w = 1;      # width of the shelf (y axis)[m]
h = 0.1;    # camera sag [m]

kit1 = MotorKit(address=0x60);
#kit2 = MotorKit(address=0x61);
motorAddresses = [kit1.stepper1, kit1.stepper2];

class Motor:
    length = 0;

    def __init__(self,num, xpos, ypos):
        self.num = num;
        self.xpos = xpos;
        self.ypos = ypos;


    def moveMotor(self, steps, dir):

        if (dir == 0):
            dir = stepper.FORWARD;
        elif (dir == 1):
            dir = stepper.BACKWARD
        for i in range(steps):
            motorAddresses[self.num].onestep(direction=dir);
    
    def changeLength(self,x,y):
        self.length = np.sqrt((self.xpos-x)**2+(self.ypos-y)**2);
