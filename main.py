import picamera as cam;
import numpy as np;
from adafruit_motorkit import MotorKit;
from motor import *
import time as time
#from camera import *

# Global Constants
r = 0.02;       # spool radius [m];
stepAngle = 360/200;   # angle per step;
l=0.28;
w=0.43;
h=0.03;

motors = np.array([Motor(0,w,0,23), Motor(1,w,l,24), Motor(2,0,0,23), Motor(3,0,l,23.5)])

# array of plants probably not needed

locs = np.genfromtxt("plantLocs.txt", skip_header=2)[:,2:4];
locs = locs.astype('int');
print(locs[0,0]);

plants = [];

def main():
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

            lengths = np.array([motors[0].length, motors[0].length, motors[0].length, motors[0].length]);
            for motor in motors:
                motor.changeLength(xpos,ypos);

            lengths = np.array([motors[0].length, motors[0].length, motors[0].length, motors[0].length]);
            lengthsNew = np.array([motors[0].lengthNew, motors[0].lengthNew, motors[0].lengthNew, motors[0].lengthNew]);
            lengthsDiff = lengthsNew-lengths;
            for i in range(len(motors)):
                if (lengthsNew[i]<lengths[i]):
                    motors[i].moveMotor(lengthsDiff[i]/(r*stepAngle),0);

            for i in range(len(motors)):
                if (lengthsNew[i]>lengths[i]):
                    motors[i].moveMotor(lengthsDiff[i]/(r*stepAngle),1);

            time.sleep(5);
            #takePicture(numShelf=1,numPlant=i+1, calibrate=False);

            
        time.sleep(20);

    # input all positions into this array

    # While loop to just get this going forever (or just have it run with a BASH script idk)
    # Need a for loop to go through each motor. This will iterate through an array of values for plant number
    # Inside the for loop, first call the function to calculate the string length for each position
    # Then call the function to move the motors. This function will need to calculate the easiest way 
    # to move the motors which requires the least amount of tension

    return 0;

main();
