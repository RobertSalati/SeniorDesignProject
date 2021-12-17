import numpy as np;
from motor import *;
from plant import *;
from camera import *;
import time as time;
import timeit

def main():

    w = 0.229/2;
    l=0.375/2;
    h=0.005;         # Camera sag [m]
    motors = np.array([Motor(0,0.7366,0.3048,0.9639), Motor(1,0.7366,-0.3048,0.8288), Motor(2, -0.7747, -.3048, 0.6563), Motor(3,-0.7747, 0.3048,0.8197)]);
  
    for motor in motors:
        motor.release();
    plants = selectPlants();


    # Loop that actually moves the camera
    maxDays = int(input("\nNumber of days to run: "));
    runsPerDay = int(input("\nRuns per day: "));

    maxRuns = maxDays*runsPerDay;
    downTime = 24/runsPerDay*3600;
    print(downTime);

    numRuns = 0;

    time.sleep(3);

    while (numRuns < maxRuns):
        
        start = timeit.default_timer();

        for plant in plants:

            plant.printPlant();         # Print out plant information
            controlMotors(plant, motors)
            time.sleep(10);

            name = takePicture(numShelf=1, numPlant=plant.num, calibrate=False);

        numRuns += 1;

        stop = timeit.default_timer();
        timeToMove = stop-start;
        time.sleep(downTime-timeToMove);

    return 0;

main();

