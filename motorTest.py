from adafruit_motorkit import MotorKit;
from adafruit_motor import stepper;
import board;
import time;

kit = MotorKit(address=0x6f);   

for i in range(1000):

    kit.stepper2.onestep();
    time.sleep(0.01);

