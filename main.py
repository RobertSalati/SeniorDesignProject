import numpy as np;
from motor import *;
from plant import *;
#from camera import *;

def main():

    w = 0.13;       # Half width of the shelf (y direction) [m]
    l=0.205;        # Half length of the shelf (x direction) [m]
    h=0.015;         # Camera sag [m]
    motors = np.array([Motor(0,l,w,0.215), Motor(1,l,-w,0.24), Motor(2,-l,-w,0.24), Motor(3,-l,w,0.235)]);      # Set up motor array

    plants = selectPlants();

    #calibrate(motors);

    #time.sleep(3);

    # Loop that actually moves the camera
    while (True):

        for plant in plants:
            plant.printPlant();         # Print out plant information
            controlMotors(plant, motors)

        #time.sleep(5);
            
    #time.sleep(20);
        break;

    return 0;

main();

