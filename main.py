import numpy as np;
from motor import *;
from plant import *;
#from camera import *;

def main():

    w = 0.229/2;
    l=0.375/2;
    h=0.005;         # Camera sag [m]
    motors = np.array([Motor(0,0.7366,0.3048,0.8636), Motor(1,0.7366,-0.3048,0.8763), Motor(2, -0.7747, -.3048, 0.8001), Motor(3,-0.7747, 0.3048,0.8128)]);
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
            controlMotorsTest(plant, motors)
            compensate(motors);
            time.sleep(5);
            
        loop = False;

        break

    return 0;

main();

