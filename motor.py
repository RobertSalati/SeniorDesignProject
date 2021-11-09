import picamera as cam;
import numpy as np;
from adafruit_motorkit import MotorKit;
from adafruit_motor import stepper;
import time as time;

l = 0.28;      # length of the shelf (x axis) [m]
w = 0.43;      # width of the shelf (y axis)[m]
h = 0.03;    # camera sag [m]

kit1 = MotorKit(address=0x60);
#kit2 = MotorKit(address=0x61);
motorAddresses = [kit1.stepper1, kit1.stepper2];

class Motor:
    def __init__(self,num, xpos, ypos,length):
        self.num = num;
        self.xpos = xpos;
        self.ypos = ypos;
        self.length=length
        self.lengthNew=length;
        self.priority=1;


    def moveMotor(self, steps, dir):

        if (dir == 0):
            dir = stepper.FORWARD;
        elif (dir == 1):
            dir = stepper.BACKWARD
        for i in range(int(steps)):
            motorAddresses[self.num].onestep(direction=dir);
            time.sleep(0.005);
    
    def changeLength(self,x,y):
        self.length = self.lengthNew;
        self.lengthNew = np.sqrt((self.xpos-x)**2+(self.ypos-y)**2);
        if (self.lengthNew-self.length < 0):
            self.priority=0;
        else:
            self.priority=1;
