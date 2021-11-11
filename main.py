import numpy as np;
from motor import *;
from plant import *;
from camera import *;

def main():


    w = 0.13;
    l=0.205;
    h=0.035;         # Camera sag [m]
    motors = np.array([Motor(0,l,w,0.9652), Motor(1,l,-w,0.9652), Motor(2,-l,-w,0.9652), Motor(3,-l,w,0.9652)]);

    locs = np.genfromtxt("plantLocs.txt", skip_header=2)[:,2:4].astype('float');
    locs = np.array([[l/2,w/2],[l/2,0],[l/2,-w/2],[0,-w/2],[0,0],[0,w/2],[-l/2],[w/2],[-l/2,0],[-l/2,-w/2]]);
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
                plants[i]=(Plant(i,locs[i,0]/10,locs[i,1]/10));
            break;

        else: 
            plantNum = int(plantNum)
            plants[count] = (Plant(plantNum,locs[plantNum,0]/10,locs[plantNum,1]/10));
        count += 1;

    del count, locs;

    time.sleep(3);

    # Loop that actually moves the camera
    while (True):
        for plant in plants:
            print("Plant", plant.num, ":");
            print("    xpos: ", plant.xpos, "ypos: ", plant.ypos);

            for motor in motors:
                motor.count = 0;
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
                        motor.move(1,motor.direction);
            
        #time.sleep(20);
        break;

    return 0;

