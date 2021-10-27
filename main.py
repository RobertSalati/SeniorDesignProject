import picamera as cam;
import numpy as np;
from adafruit_motorkit import MotorKit;
from motor import *
from camera import *

# Global Constants:

pos1 = [1,1]; pos2 = [1,2]; pos3 = [1,3]; pos4 = [1,4];
pos5 = [2,1]; pos6 = [2,2]; pos7 = [2,3]; pos8 = [2,4];
pos9 = [3,1]; pos10 = [3,2]; pos11 = [3,3]; pos12 = [3,4];
pos13 = [4,1]; pos14 = [4,2]; pos15 = [4,3]; pos16 = [4,4];

plants = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]);

print("main.py");

def main():
    # input all positions into this array
    # While loop to just get this going forever (or just have it run with a BASH script idk)
    # Need a for loop to go through each motor. This will iterate through an array of values for plant number
    # Inside the for loop, first call the function to calculate the string length for each position
    # Then call the function to move the motors. This function will need to calculate the easiest way 
    # to move the motors which requires the least amount of tension
    print("main()");

    return 0;

main();
