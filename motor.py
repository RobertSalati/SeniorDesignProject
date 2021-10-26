import picamera as cam;
import numpy as np;
from adafruit_motorkit import MotorKit;
from adafruit_motor import stepper;

l = 3;      # length of the shelf (x axis) [m]
w = 1;      # width of the shelf (y axis)[m]
h = 0.1;    # camera sag [m]

kit1 = MotorKit(address=0x6f);
kit2 = MotorKit(address=0x6f);

def moveMotor(steps, num, direc):
    if num == 1:            # Motor 1
        if direc == 0:
            for i in range(steps):
                kit1.stepper1.onestep(direction=stepper.FORWARD);
        if direc == 1:
            for i in range(steps):
                kit1.stepper1.onestep(direction=stepper.BACKWARD);
     
    if num == 2:           # Motor 2
        if direc == 0:
            for i in range(steps):
                kit1.stepper2.onestep(direction=stepper.FORWARD);
        if direc == 1:
            for i in range(steps):
                kit1.stepper2.onestep(direction=stepper.BACKWARD);
    
    if num == 3:            # Motor 3
        if direc == 0:
            for i in range(steps):
                kit2.stepper1.onestep(direction=stepper.FORWARD);
        if direc == 1:
            for i in range(steps):
                kit2.stepper1.onestep(direction=stepper.BACKWARD);
    
    if num == 4:            # Motor 4
        if direc == 0:
            for i in range(steps):
                kit2.stepper2.onestep(direction=stepper.FORWARD);
        if direc == 1:
            for i in range(steps):
                kit2.stepper2.onestep(direction=stepper.BACKWARD);


def calcLength(x, y):

    print("calcLength()");

    L1 = np.sqrt((l-x)**2+(w-y)**2+h**2);

    L2 = np.sqrt((l-x)**2+(w+y)**2+h**2);

    L3 = np.sqrt((l+x)**2+(w+y)**2+h**2);

    L4 = np.sqrt((l+x)**2+(w-y)**2+h**2);

    return L1, L2, L3, L4;
