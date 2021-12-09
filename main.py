import numpy as np;
from motor import *;
from plant import *;
#from camera import *;
import time as time;

def main():

    w = 0.229/2;
    l=0.375/2;
    h=0.005;         # Camera sag [m]
    motors = np.array([Motor(0,l,w,0.21), Motor(1,l,-w,0.21), Motor(2,-l,-w,0.21), Motor(3,-l,w,0.21)]);
    for motor in motors:
        motor.release();
    plants = selectPlants();

    #calibrate(motors);

    time.sleep(3);

    # Loop that actually moves the camera
    loop = True;
    while (loop == True):

        for plant in plants:
            plant.printPlant();         # Print out plant information
            controlMotorsTest1(plant, motors)
            #time.sleep(5);

            #name = takePicture(numShelf=1, numPlant=plant.num, calibrate=False):
            input("press enter to continue: ");

        loop = False;

        break

    return 0;

main();

