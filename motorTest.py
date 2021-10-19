from adafruit_motorkit import MotorKit;
from adafruit_motor import stepper;
import board;
import time;

kit = MotorKit(i2c=board.I2C());   

for i in range(10):

    kit.stepper1.onestep();
    time.sleep(0.5);

