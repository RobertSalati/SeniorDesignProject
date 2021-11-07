from picamera import PiCamera;
import numpy as np;
import time as time;
from datetime import datetime;
import cv2 as cv;

camera = PiCamera();

def takePicture(numShelf, numPlant):
    camera.start_preview();
    time.sleep(5);

    now = datetime.now();
    directory = "/home/pi/SeniorDesignProject/images/";
    name = "shelf " + str(numShelf) + " plant " + str(numPlant) + now.strftime(" %m-%d-%Y %H:%M:%S") + ".jpg";
    title = str(directory+name)
    print(title);
    camera.capture(title);
    camera.stop_preview();
    return title;
