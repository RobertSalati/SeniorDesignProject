import picamera as cam;
import numpy as np;
from adafruit_motorkit import motorkit;
from adafruit_motor import stepper;

l = 3;      # length of the shelf (x axis) [m]
w = 1;      # width of the shelf (y axis)[m]
h = 0.1;    # camera sag [m]

global lengths;

lengths = np.array([NULL, NULL, NULL, NULL]);

class Motor:
    length = NULL;

kit1 = MotorKit(address=0x60);
kit2 = MotorKit(address=0x61);

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


def calcLength(x, y):

    print("calcLength()");

    L1 = np.sqrt((l-x)**2+(w-y)**2+h**2);

    L2 = np.sqrt((l-x)**2+(w+y)**2+h**2);

    L3 = np.sqrt((l+x)**2+(w+y)**2+h**2);

    L4 = np.sqrt((l+x)**2+(w-y)**2+h**2);

    lengths = np.array([L1, L2, L3, L4]);
    return lengths;
