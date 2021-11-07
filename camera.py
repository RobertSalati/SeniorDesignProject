#from picamera import PiCamera;
import numpy as np;
import time as time;
from datetime import datetime;
import cv2 as cv;
import matplotlib.pyplot as plt;

#camera = PiCamera();

def takePicture(numShelf, numPlant):
    """Description
    Args:
        
    Returns:
        None.
    """
    camera.resolution = (2592, 1944)
    camera.start_preview();
    time.sleep(5);
    dg
    fgsdfgdfg

    img = np.empty((1944,2592,3), dtype=np.uint8);
    
    camera.capture(img, 'rgb');
    camera.stop_preview();

    now = datetime.now();
    directory = "/home/pi/SeniorDesignProject/images/";
    name = "shelf " + str(numShelf) + " plant " + str(numPlant) + now.strftime(" %m-%d-%Y %H:%M:%S") + ".jpg";
    title = str(directory+name)
    cv.imwrite(img, title);

    return img;

def coverageArea(title):

    img = cv.imread(title);
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB);

    plt.figure();
    plt.imshow(img_rgb);
    plt.show();



def calibrate():
    print("Hi");



coverageArea("cam_test.jpg");
#calibrate("cam_test.jpg");