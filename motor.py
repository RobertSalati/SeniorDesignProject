import numpy as np;
from adafruit_motorkit import MotorKit;
from adafruit_motor import stepper;
import time as time;


global r, stepAngle, l, w, h;

r = 0.015;       # spool radius [m];
stepAngle = 360/200*np.pi/180;   # angle per step [rad];

numSteps = 25;


kit1 = MotorKit(address=0x60);
kit2 = MotorKit(address=0x61);
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

        if (dir == 1):  # Winds the spool up - Decreases length
            dir = stepper.FORWARD;
        elif (dir == -1):    # Unwinds the spool - Increases length
            dir = stepper.BACKWARD
        for i in range(int(steps)):
            motorAddresses[self.num].onestep(direction=dir);
            #motorAddresses[self.num].onestep(direction=dir,style = stepper.INTERLEAVE);
            time.sleep(0.05);
    def release(self):
        motorAddresses[self.num].release();

    def calcLengths(self,x, y):
        self.length = self.lengthNew;
        self.lengthNew = np.sqrt((self.xpos-x)**2+(self.ypos-y)**2)-0.02;

    def calcSteps(self):
        self.steps = int((self.lengthNew-self.length)/(r*stepAngle));

        if (self.steps < 0):
            self.direction=-1;      # Unwind
        else:
            self.direction=1;       # Wind up
    
    def printMotor(self):
        print(" ");
        print("    Motor", self.num+1, ":");
        print("        Coordinates:","(", self.xpos, ",", self.ypos, ")"); 
        print("        Length:", self.length);
        print("        New length:", self.lengthNew);
        print("        Steps:", self.steps);


def controlMotors(plant, motors):

    for motor in motors:
        motor.count = 0;
        motor.calcLengths(plant.xpos,plant.ypos);
        motor.calcSteps();
        motor.printMotor();

    print("----------------------------");

    steps = np.array([np.abs(motors[0].steps), np.abs(motors[1].steps), np.abs(motors[2].steps), np.abs(motors[3].steps)])
    maxMotor = motors[np.argmax(steps)]; maxSteps = np.abs(maxMotor.steps);
    print("    Motor num:",maxMotor.num+1, "Steps:", maxSteps);

    while (maxMotor.count/maxSteps < maxSteps):
        for motor in motors:
            motor.count += np.abs(motor.steps);
            if (motor.count % np.abs(maxSteps) < np.abs(motor.steps)):
                motor.move(steps=1,dir=motor.direction);

def controlMotorsTest1(plant,motors):
    
    loop = True;

    for motor in motors:        # calculate parameters for movement
        motor.count = 0;
        motor.calcLengths(plant.xpos,plant.ypos);
        motor.calcSteps();
    
    motorsSorted = np.empty([4],dtype='object');
    ind = 0;
    for motor in motors:
        if motor.direction == -1:
            motorsSorted[ind] = motor;
            ind += 1;

    for motor in motors:
        if motor.direction == 1:
            motorsSorted[ind] = motor;
            ind += 1;

    for motor in motorsSorted:
        motor.printMotor();


    while loop == True:
        for motor in motorsSorted:
            print("num: ", motor.num+1);
            if np.abs(motor.count) == np.abs(motor.steps):
                print("   No steps remaining")
                motor.release();

            elif numSteps < np.abs(motor.steps)-np.abs(motor.count):

                motor.move(steps=50, dir=motor.direction);
                motor.count += numSteps;
                motor.release();
                print("   Moving", numSteps, "steps");
                print("  ", np.abs(motor.steps)-np.abs(motor.count), "steps remaining");

            elif numSteps > np.abs(motor.steps)-np.abs(motor.count):
                motor.move(steps=motor.steps-numSteps, dir=motor.direction);
                print("   Moving", np.abs(motor.steps)-np.abs(motor.count), "steps");
                motor.count += np.abs(motor.steps)-np.abs(motor.count);
                motor.release();
                

            time.sleep(0.01);

        loop = False;
        for motor in motors:
            if np.abs(motor.count) < np.abs(motor.steps):
                loop = True;
                break;

        print("----------------------------------------");
        time.sleep(1);

def controlMotorsTest2(plant,motors):

    for motor in motors:        # calculate parameters for movement
        motor.count = 0;
        motor.calcLengths(plant.xpos,plant.ypos);
        motor.calcSteps();
        motor.printMotor();
    print("----------------------------");
    
    motorsSorted = np.empty([4],dtype='object');
    ind = 0;
    for motor in motors:
        if motor.direction == -1:
            motorsSorted[ind] = motor;
            ind += 1;

    for motor in motors:
        if motor.direction == 1:
            motorsSorted[ind] = motor;
            ind += 1;

    for motor in motorsSorted:
        motor.printMotor();
        motor.move(motor.steps, motor.direction);

        time.sleep(1);


