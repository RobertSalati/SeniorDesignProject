import numpy as np;
#from adafruit_motorkit import MotorKit;
#from adafruit_motor import stepper;
import time as time;

global r, stepAngle, l, w, h;

r = 0.015;       # spool radius [m];
stepAngle = 360/400*np.pi/180;   # angle per step [rad];
l=0.9144;       # Shelf length/2 [m]
w=0.3048;       # Shelf width/2 [m]
w = 0.13;
l=0.205;
h=0.035;         # Camera sag [m]

#kit1 = MotorKit(address=0x60);
#kit2 = MotorKit(address=0x61);
#motorAddresses = [kit1.stepper1, kit1.stepper2];
#motorAddresses = [kit1.stepper1, kit1.stepper2, kit2.stepper1, kit2.stepper2];


class Motor:
    def __init__(self,num, xpos, ypos, length):
        self.num = num;
        self.xpos = xpos;
        self.ypos = ypos;
        self.length=length
        self.lengthNew=length;
        self.steps=0;
        self.count=0;
        self.direction=1;


    def move(self, steps, dir):

        if (dir == -1):  # Winds the spool up - Decreases length
            dir = stepper.FORWARD;
        elif (dir == 1):    # Unwinds the spool - Increases length
            dir = stepper.BACKWARD
        for i in range(int(steps)):
            motorAddresses[self.num].onestep(direction=dir,style = stepper.INTERLEAVE);
            time.sleep(0.005);
    
    def calcSteps(self,x,y):
        self.length = self.lengthNew;
        print("Motor", self.num, "xpos:", self.xpos, ", ypos:", self.ypos);
        self.lengthNew = np.sqrt((self.xpos-x)**2+(self.ypos-y)**2);
        self.steps = int((self.lengthNew-self.length)/(r*stepAngle));

        if (self.lengthNew-self.length < 0):
            self.direction=-1;
        else:
            self.direction=1;
