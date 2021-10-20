from picamera import PiCamera;
import numpy as np;
import time as time;
#import opencv as cv;

camera = PiCamera();

def takePicture(num):
    camera.start_preview();
    sleep(3);
    title = "plant " + str(num) ", "
    camera.capture(title);
