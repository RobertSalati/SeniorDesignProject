import picamera as cam;
import numpy as np;
from adafruit_motorkit import MotorKit;

l = 3;      # length of the shelf (x axis) [m]
w = 1;      # width of the shelf (y axis)[m]
h = 0.1;    # camera sag [m]

def moveMotor():
    # simply moves the motor. Nothing more nothing less
    print("moveMotor()");
    
    return 0;

def calcLength(x, y):

    print("calcLength()");

    L1 = np.sqrt((l-x)**2+(w-y)**2+h**2);

    L2 = np.sqrt((l-x)**2+(w+y)**2+h**2);

    L3 = np.sqrt((l+x)**2+(w+y)**2+h**2);

    L4 = np.sqrt((l+x)**2+(w-y)**2+h**2);

    return L1, L2, L3, L4;
