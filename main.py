import picamera as cam;
import numpy as np;
from adafruit_motorkit import MotorKit;
from motor import *
import time as time
#from camera import *

# Global Constants
r = 2       # spool radius [cm];
stepAngle = 360/200;   # angle per step;
motor1 = Motor(0); motor2 = Motor(1); motor3 = Motor(2); motor4 = Motor[3];
motors = np.array([motor1, motor2, motor3, motor4]);
print(motors.length)


# array of plants probably not needed

locs = np.genfromtxt("plantLocs.txt", skip_header=2)[:,2:4];
locs = locs.astype('int');
print(locs[0,0]);

plants = [];

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
            print("xpos: ", xpos, "ypos: ", ypos);
            lengthsNew = calcLength(xpos, ypos);
            lengthsDiff = lengthsNew-lengths;
            steps = lengthsDiff/(r*stepAngle);
            steps = steps.astype('int');
            for j in range(4):
                if lengthsDiff[j]<=0:
                    moveMotor(abs(steps[j]), j+1, direc=1);
            for h in range(4):
                if lengthsDiff[h]>0:
                    moveMotor(abs(steps[h]), h+1, direc=0);
            time.sleep(5);
            lengths = lengthsNew;
            print(i);
            #takePicture(numShelf=1,numPlant=i+1, calibrate=False);

            
        time.sleep(20);

    # input all positions into this array

    # While loop to just get this going forever (or just have it run with a BASH script idk)
    # Need a for loop to go through each motor. This will iterate through an array of values for plant number
    # Inside the for loop, first call the function to calculate the string length for each position
    # Then call the function to move the motors. This function will need to calculate the easiest way 
    # to move the motors which requires the least amount of tension
    print("main()");

    return 0;

main();
