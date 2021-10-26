from adafruit_motorkit import MotorKit;
from adafruit_motor import stepper;
import board;
import time;
from motor import *;

kit = MotorKit(address=0x6f);
#kit1 = MotorKit(address=0x70);

#2048 steps for 1 rotation with small motor
#200 steps for 1 rotation with big motor

# 360 = 2048


while True:
    angle = int(input("Move angle: "));
    num = int(input("Motor number: "));
    steps = abs(int(angle/360 * 2048));
    if angle <= 0:
        direction = 1;
    else:
        direction = 0;
    moveMotor(steps,num,direction);

