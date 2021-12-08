import numpy as np;
from adafruit_motorkit import MotorKit;
from adafruit_motor import stepper;
import time as time;


global r, stepAngle, l, w, h;

r = 0.015;       # spool radius [m];
stepAngle = 360/200*np.pi/180;   # angle per step [rad];

kit1 = MotorKit(address=0x60);
kit2 = MotorKit(address=0x61);
#motorAddresses = [kit1.stepper1, kit1.stepper2];
motorAddresses = [kit1.stepper1, kit1.stepper2, kit2.stepper1, kit2.stepper2];


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
            motorAddresses[self.num].onestep(direction=dir);
            #motorAddresses[self.num].onestep(direction=dir,style = stepper.INTERLEAVE);
            time.sleep(0.05);
    
    def calcLengths(self,x, y):
        self.length = self.lengthNew;
        print("Motor", self.num, "xpos:", self.xpos, ", ypos:", self.ypos);
        self.lengthNew = np.sqrt((self.xpos-x)**2+(self.ypos-y)**2)-0.01;

    def calcSteps(self):
        self.steps = int((self.lengthNew-self.length)/(r*stepAngle));

        if (self.lengthNew-self.length < 0):
            self.direction=-1;
        else:
            self.direction=1;
    
    def printMotor(self):
        print("Motor", self.num+1, ":");
        print("    Length:", self.length);
        print("    New length:", self.lengthNew);
        print("    Steps:", self.steps);

def controlMotors(plant, motors):

    for motor in motors:
        motor.count = 0;
        motor.calcLengths(plant.xpos,plant.ypos);
        motor.calcSteps();
        motor.printMotor();

    steps = np.array([np.abs(motors[0].steps), np.abs(motors[1].steps), np.abs(motors[2].steps), np.abs(motors[3].steps)])
    maxMotor = motors[np.argmax(steps)]; maxSteps = np.abs(maxMotor.steps);
    print("    Motor num:",maxMotor.num+1, "Steps:", maxSteps);

    while (maxMotor.count/maxSteps < maxSteps):
        for motor in motors:
            motor.count += np.abs(motor.steps);
            if (motor.count % np.abs(maxSteps) < np.abs(motor.steps)):
                motor.move(steps=1,dir=motor.direction);
