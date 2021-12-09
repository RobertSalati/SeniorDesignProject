from motor import *;
from adafruit_motorkit import MotorKit;
from adafruit_motor import stepper;

motors = np.array([Motor(0,0,0,0), Motor(1,0,0,0), Motor(2,0,0,0), Motor(3,0,0,0)]);

for motor in motors:
    motor.release();
