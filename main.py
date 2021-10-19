import picamera as cam;
import numpy as np;
from adafruit_motorkit import MotorKit;

# Global Constants:
l = 3;      # length of the shelf (x axis) [m]
w = 1;      # width of the shelf (y axis)[m]
h = 0.1;    # camera sag [m]


print("main.py");

def main():
    # While loop to just get this going forever (or just have it run with a BASH script idk)
    # Need a for loop to go through each motor. This will iterate through an array of values for plant number
    # Inside the for loop, first call the function to calculate the string length for each position
    # Then call the function to move the motors. This function will need to calculate the easiest way 
    # to move the motors which requires the least amount of tension
    print("main()");

    return 0;

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

while(True):
    x = int(input("x: "));
    y = int(input("y: "));
    L1, L2, L3, L4 = calcLength(x,y);
    print("L1: ", L1, "L2: ", L2, "L3: ", L3, "L4: ", L4);
