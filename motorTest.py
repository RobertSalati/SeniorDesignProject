from adafruit_motorkit import MotorKit;
from adafruit_motor import stepper;
import board;
import time;
from motor import *;
import numpy as np

#2048 steps for 1 rotation with small motor
#200 steps for 1 rotation with big motor

# 360 = 2048

motors = np.array([Motor(0,0,0,0), Motor(1,0,0,0), Motor(2,0,0,0), Motor(3,0,0,0)]);

for motor in motors:
    motor.release();

while True:
    angle = int(input("Move angle: "))*np.pi/180;
    num1 = int(input("Motor number: "));
    stepAngle = 2*np.pi/400;
    steps = abs(angle/stepAngle);
    print(steps);
    if angle <= 0:
        direction = 1;
    else:
        direction = -1;
    time.sleep(2);
    for i in range(int(steps)):
        motors[num1].move(1, direction);
    motors[num1].release();
    

