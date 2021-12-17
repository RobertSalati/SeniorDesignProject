import numpy as np;
from adafruit_motorkit import MotorKit;
from adafruit_motor import stepper;
import time as time;


global r, stepAngle, l, w, h;

r = 0.015;       # spool radius [m];
stepAngle = 360/200*np.pi/180;   # angle per step [rad];


kit1 = MotorKit(address=0x60);
kit2 = MotorKit(address=0x61);
motorAddresses = [kit1.stepper1, kit1.stepper2, kit2.stepper1, kit2.stepper2];


class Motor:
    def __init__(self,num, xpos, ypos, length):
        """Motor Constructor.
        Args:
            num (int): motor number, used for indexing
            xpos (float): motor x location
            ypos (float): motor y location
            length (float): initial string length
        Returns: 
            None
        """
        self.num = num;
        self.xpos = xpos;
        self.ypos = ypos;
        self.length=length
        self.lengthNew=length;
        self.steps=0;
        self.count=0;
        self.direction=1;

    def move(self, steps, dir):
        """Moves the motor a desired number of steps
        Args:
            steps (int): number of steps the motor needs to take
            dir (int): direction of motor. 1 to decrease length, -1 to increase length
            length (float): length 
        """
        if (dir == 1):  # Unwinds the spool - Increases length
            dir = stepper.FORWARD;
        elif (dir == -1):    # Winds the spool - Decreases length
            dir = stepper.BACKWARD
        for i in range(int(steps)):
            motorAddresses[self.num].onestep(direction=dir);
            time.sleep(0.05);

    def release(self):
        """Turns off holding torque
        Args: 
            None.
        Returns:
            None.
        """
        motorAddresses[self.num].release();

    def calcLengths(self,x, y):
        """Calculates new string length.
        Args:
            x (float): Desired x coordinate of the camera
            y (float): Desired y coordinate of the camera.
        Returns:
            None.
        """
        self.length = self.lengthNew;
        self.lengthNew = np.sqrt((self.xpos-x)**2+(self.ypos-y)**2)-0.02;

    def calcSteps(self):
        """Calculates the number of steps the motor needs to take
        Args:
            None.
        Returns:
            None.
        """
        self.steps = int((self.lengthNew-self.length)/(r*stepAngle));

        if (self.steps < 0):
            self.direction=-1;      # Unwind
        else:
            self.direction=1;       # Wind up
    
    def printMotor(self):
        """Prints out motor information.
        Args:
            None.
        Returns: 
            None.
        """
        print(" ");
        print("    Motor", self.num+1, ":");
        print("        Coordinates:","(", self.xpos, ",", self.ypos, ")"); 
        print("        Length:", self.length);
        print("        New length:", self.lengthNew);
        print("        Steps:", self.steps);

def compensate(motors):
    """Function to compensate any errors the motors may have occured. Simply moves the motors back an equal amount of steps.
    Args: 
        motors (Array dtype:object): Array of 4 motor objects.
    Returns:
        None.
    """
    for motor in motors:
        motor.move(25, -1);

def controlMotors(plant,motors):
    """Main function to move the motors. Calculates the lengths and number of steps, and moves motors a prescribed number of steps at a time.
    Args:
        plant (object): Plant which the camera needs to move to.
        motors (Array dtype:object): Array of 4 motor objects.
    Returns:
        None.
    """    

    numSteps = 50;
    loop = True;

    for motor in motors:        # calculate parameters for movement
        motor.count = 0;
        motor.calcLengths(plant.xpos,plant.ypos);
        motor.calcSteps();
    
    motorsSorted = np.empty([4],dtype='object');
    ind = 0;

    # Sorting motors by direction. Want motors to give slack before they pull or bad things happen
    for motor in motors:
        if motor.direction == 1:
            motorsSorted[ind] = motor;
            ind += 1;

    for motor in motors:
        if motor.direction == -1:
            motorsSorted[ind] = motor;
            ind += 1;

    for motor in motorsSorted:
        motor.printMotor();


    while loop == True:
        for motor in motorsSorted:
            print("num: ", motor.num+1);
            if np.abs(motor.count) == np.abs(motor.steps):      # If no more steps remaining, don't move
                print("   No steps remaining")
                motor.release();
                # end if
            elif numSteps < np.abs(motor.steps)-np.abs(motor.count):        # If more than numSteps remaining, step numSteps times.

                motor.move(steps=numSteps, dir=motor.direction);
                motor.release();
                motor.count += numSteps;

                print("   Moving", numSteps, "steps");
                print("  ", np.abs(motor.steps)-np.abs(motor.count), "steps remaining");
                # end elif

            elif numSteps >= np.abs(motor.steps)-np.abs(motor.count):       # If less than numSteps remaining, do the remaining steps
                motor.move(steps=np.abs(motor.steps)-np.abs(motor.count), dir=motor.direction);
                print("   Moving", np.abs(motor.steps)-np.abs(motor.count), "steps");
                motor.release();
                motor.count += np.abs(motor.steps)-np.abs(motor.count);
                # end elif

            time.sleep(0.01);

        loop = False;
        for motor in motors:
            if np.abs(motor.count) < np.abs(motor.steps):
                loop = True;
                break;
                # end if
            #end for


        print("----------------------------------------");
        time.sleep(1);
        # end while
    compensate(motors);

def controlMotorsOld(plant, motors):
    """Main function to move the motors. Calculates the lengths and number of steps, and moves all motors simultaneously
    
    Args:
        plant (object): Plant which the camera needs to move to.
        motors (Array dtype:object): Array of 4 motor objects.
    Returns:
        None.
    =======================================================================================
                                        NO LONGER IN USE
    =======================================================================================
    """
    for motor in motors:
        motor.count = 0;
        motor.calcLengths(plant.xpos,plant.ypos);
        motor.calcSteps();
        motor.printMotor();

    print("----------------------------");

    steps = np.array([np.abs(motors[0].steps), np.abs(motors[1].steps), np.abs(motors[2].steps), np.abs(motors[3].steps)])
    maxMotor = motors[np.argmax(steps)]; maxSteps = np.abs(maxMotor.steps);
    print("    Motor num:",maxMotor.num+1, "Steps:", maxSteps);

    while (maxMotor.count/maxSteps < maxSteps):
        for motor in motors:
            motor.count += np.abs(motor.steps);
            if (motor.count % np.abs(maxSteps) < np.abs(motor.steps)):
                motor.move(steps=1,dir=motor.direction);
