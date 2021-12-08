import numpy as np;
from motor import *;
from plant import *;
#from camera import *;

def main():

    w = 0.229/2;
    l=0.375/2;
    h=0.005;         # Camera sag [m]
    motors = np.array([Motor(0,l,w,0.21), Motor(1,l,-w,0.21), Motor(2,-l,-w,0.21), Motor(3,-l,w,0.205)]);

    plants = selectPlants();

    #calibrate(motors);

    time.sleep(3);

    # Loop that actually moves the camera
    while (True):

        for plant in plants:
            plant.printPlant();         # Print out plant information
            controlMotors(plant, motors)

        time.sleep(5);
            
        #time.sleep(20);
        break;

    return 0;

main();

