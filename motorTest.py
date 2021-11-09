from adafruit_motorkit import MotorKit;
from adafruit_motor import stepper;
import board;
import time;
from motor import *;
import numpy as np

#2048 steps for 1 rotation with small motor
#200 steps for 1 rotation with big motor

# 360 = 2048


motors = np.array([Motor(0,1,1), Motor(1,-1,1), Motor(2,-1,-1), Motor(3,1,-1)]) 

while True:
    angle = int(input("Move angle: "));
    num = int(input("Motor number: "));
    steps = abs(int(angle/360 * 200));
    if angle <= 0:
        direction = 1;
    else:
        direction = 0;

    motors[num-1].moveMotor(steps, direction);
    

