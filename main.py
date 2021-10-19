import picamera as cam;
import numpy as np;
from adafruit_motorkit import MotorKit;
from motor import *
from camera import *

# Global Constants:



print("main.py");

def main():
    # While loop to just get this going forever (or just have it run with a BASH script idk)
    # Need a for loop to go through each motor. This will iterate through an array of values for plant number
    # Inside the for loop, first call the function to calculate the string length for each position
    # Then call the function to move the motors. This function will need to calculate the easiest way 
    # to move the motors which requires the least amount of tension
    print("main()");

    return 0;



while(True):
    x = int(input("x: "));
    y = int(input("y: "));
    L1, L2, L3, L4 = calcLength(x,y);
    print("L1: ", L1, "L2: ", L2, "L3: ", L3, "L4: ", L4);
