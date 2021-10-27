import picamera as cam;
import numpy as np;
from adafruit_motorkit import MotorKit;
from motor import *
import time as time
#from camera import *

# Global Constants
r = 2       # spool radius [cm];
stepAngle = 360/2048;   # angle per step;

# array of plants probably not needed

locs = np.genfromtxt("plantLocs.txt", skip_header=2)[:,2:4];
locs = locs.astype('int');
print(locs[0,0]);


plants = [];

print("main.py");


def main():
    lengths = np.array([0, 1, 1, 2]);
    # Initial loop to find what plants will be worked with.
    while (True):
        plantNum = input("Plant number: ");
        if (plantNum == "done" or plantNum == "Done"):
            break;
        else: 
            plants.append(int(plantNum)-1);
    # Loop that actually moves the camera
    while (True):
        for i in plants:
            xpos, ypos = locs[i][0], locs[i][1];
            print(xpos, ypos);
            lengthsNew = calcLength(xpos, ypos);
            lengthsDiff = lengthsNew-lengths;
            steps = lengthsDiff/(r*stepAngle);
            steps = steps.astype('int');
            print(steps)
            for i in range(2):
                if lengthsDiff[i]<=0:
                    moveMotor(abs(steps[i]), i+1, direc=1);
            for i in range(2):
                if lengthsDiff[i]>0:
                    moveMotor(abs(steps[i]), i+1, direc=0);
            time.sleep(5);
            lengths = lengthsNew;
            
        break;

    # input all positions into this array

    # While loop to just get this going forever (or just have it run with a BASH script idk)
    # Need a for loop to go through each motor. This will iterate through an array of values for plant number
    # Inside the for loop, first call the function to calculate the string length for each position
    # Then call the function to move the motors. This function will need to calculate the easiest way 
    # to move the motors which requires the least amount of tension
    print("main()");

    return 0;

main();
