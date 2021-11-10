import numpy as np;
#from adafruit_motorkit import MotorKit;
from motor import *
from plant import *
import time as time
#from camera import *

def main():

    motors = np.array([Motor(0,l,w,0.9652), Motor(1,l,-w,0.9652), Motor(2,-l,-w,0.9652), Motor(3,-l,w,0.9652)]);

    locs = np.genfromtxt("plantLocs.txt", skip_header=2)[:,2:4].astype('float');

    plants = np.empty(len(locs),dtype=object);
    print(plants);
    # Initial loop to find what plants will be worked with.
    count = 0;
    while (True):

        plantNum = input("Plant number: ");

        if (plantNum == "done" or plantNum == "Done"):
            break;

        elif (plantNum == "all" or plantNum == "All"):
            for i in range(len(locs)):
                plants[i]=(Plant(i,locs[i,0],locs[i,1]));
            break;

        else: 
            plantNum = int(plantNum)
            plants[count] = (Plant(plantNum,locs[plantNum,0],locs[plantNum,1]));
        count += 1;

    del count, locs;

    #time.sleep(3);

    # Loop that actually moves the camera
    while (True):
        for plant in plants:
            print("Plant", plant.num, ":");
            print("    xpos: ", plant.xpos, "ypos: ", plant.ypos);

            for motor in motors:
                motor.calcSteps(plant.xpos,plant.ypos);
                print("    Motor", motor.num+1, ":");
                print("        Length:", motor.length);
                print("        New length:", motor.lengthNew);
                print("        Steps:", int((motor.lengthNew-motor.length)/(r*stepAngle)));

            steps = np.array([motors[0].steps, motors[1].steps, motors[2].steps, motors[3].steps])
            maxMotor = motors[np.argmax(steps)]; maxSteps = np.max(steps);
            print("    Motor num:",maxMotor.num+1, "Steps:", maxSteps);

            while (maxMotor.count/maxSteps < maxSteps):
                for motor in motors:
                    motor.count += np.abs(motor.steps);
                    if (motor.count % maxSteps <= np.abs(motor.steps)):
                        a = 1;
                        #motor.move(1,motor.direction);
            print("    Steps completed:");
            for motor in motors:
                print("        Motor", motor.num, ":", int(motor.count/maxSteps));
                motor.count = 0;


            #for motor in motors:
            #    if (motor.priority == 1):
            #        motors[motor.num].moveMotor((motor.lengthNew-motor.length)/(r*stepAngle),0);

            #for motor in motors:
            #    if (motor.priority == 0):
            #        motors[motor.num].moveMotor((motor.lengthNew-motor.length)/(r*stepAngle),1);

            #time.sleep(5);
            #takePicture(numShelf=1,numPlant=i+1, calibrate=False);

            
        #time.sleep(20);
        break;

    # input all positions into this array

    # While loop to just get this going forever (or just have it run with a BASH script idk)
    # Need a for loop to go through each motor. This will iterate through an array of values for plant number
    # Inside the for loop, first call the function to calculate the string length for each position
    # Then call the function to move the motors. This function will need to calculate the easiest way 
    # to move the motors which requires the least amount of tension

    return 0;

main();
