import numpy as np;
from motor import *;
from plant import *;
from camera import *;

def main():

    w = 0.13;       # Half width of the shelf (y direction) [m]
    l=0.205;        # Half length of the shelf (x direction) [m]
    h=0.015;         # Camera sag [m]
    motors = np.array([Motor(0,l,w,0.215), Motor(1,l,-w,0.24), Motor(2,-l,-w,0.24), Motor(3,-l,w,0.235)]);      # Set up motor array

    data = np.genfromtxt("plantLocs.txt", skip_header=2);        # Read plant locations from text file
    locs = data[:,2:4].astype('float');
    locs = np.array([[l/2,w/2],[l/2,0],[l/2,-w/2],[0,-w/2],[0,0],[0,w/2],[-l/2, w/2],[-l/2,0],[-l/2,-w/2]]);

    plants = np.empty(len(locs),dtype=object);         # Create empty array for plant objects (maybe replace).
    # Initial loop to find what plants will be worked with.
    count = 0;
    # Interface :)

    

    while (True):

        plantNum = input("Plant number: ");

        if (plantNum == "done" or plantNum == "Done"):      # Done inputting values
            break;      

        elif (plantNum == "all" or plantNum == "All"):      # Want to take pictures of all plants
            for i in range(len(locs)):
                plants[i]=(Plant(i,locs[i][0],locs[i][1]));
                print(plants[i].num);
            break;

        else: 
            plantNum = int(plantNum)-1          # Adds one plant at a time
            plants[count] = (Plant(plantNum,locs[plantNum][0],locs[plantNum][1]));
        count += 1;

    del count, locs;        # Delete 

    time.sleep(3);

    calibrate(motors);

    # Loop that actually moves the camera
    while (True):

        for plant in plants:
            plant.printPlant();         # Print out plant information

            for motor in motors:
                motor.count = 0;
                motor.calcLengths(plant.xpos,plant.ypos);
                motor.calcSteps();
                motor.printMotor();

            steps = np.array([np.abs(motors[0].steps), np.abs(motors[1].steps), np.abs(motors[2].steps), np.abs(motors[3].steps)])
            maxMotor = motors[np.argmax(steps)]; maxSteps = np.abs(maxMotor.steps);
            print("    Motor num:",maxMotor.num+1, "Steps:", maxSteps);

            while (maxMotor.count/maxSteps < maxSteps):
                for motor in motors:
                    motor.count += np.abs(motor.steps);
                    if (motor.count % np.abs(maxSteps) < np.abs(motor.steps)):
                        motor.move(steps=1,dir=motor.direction);
            time.sleep(5);
            
        #time.sleep(20);
        break;

    return 0;

main();

