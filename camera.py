#from picamera import PiCamera;
import numpy as np;
import time as time;
from datetime import datetime;
import cv2 as cv;
import matplotlib.pyplot as plt;

# Global variables
#camera = PiCamera();

# Written and tested
def takePicture(numShelf, numPlant, calibrate):
    """ Takes a picture and saves it to the images folder
    Args:
        numShelf (int): shelf number of the plant
        numPlant (int): number of the plant
        calibrate (bool): decides whether to take a picture for calibration or storage
    Returns:
        title (string): images name to be accessed by other functions
    """

    camera.start_preview();    # Opens the camera
    time.sleep(5);        # Sleeps for 5 seconds to allow the camera to adjust
   
    if (calibrate == True):     # Creates file name for calibration
        directory = "/home/pi/SeniorDesignProject/";
        name = "calibrate.jpg";

    elif (calibrate == False):  # Creates file name for storage
        now = datetime.now();
        directory = "/home/pi/SeniorDesignProject/images/";
        name = "shelf " + str(numShelf) + " plant " + str(numPlant) + now.strftime(" %m-%d-%Y %H:%M:%S") + ".jpg";

    title = str(directory+name)     # Combines image name and directory.
    camera.capture(title);      # Takes the picture
    camera.stop_preview();      # Closes the camera

    return title;

def calibrate():
    """Calibrates the camera with a vision based feedback loop
    Args:
        None.
    Returns:
        None.
    """

    title = "calibration.jpg";
    #title = takePicture(0,0,True);  # Takes calibration picture
    
    img = cv.imread(title);     # Creates numpy array of the image

    img = img[10:len(img)-10,10:len(img[0])-10]

    img_gs = cv.cvtColor(img, cv.COLOR_BGR2GRAY);       # Converts image to grayscale

    

    thresh_rgb, img_rgb_binary = cv.threshold(img, 100, 255, cv.THRESH_BINARY);

    thresh_gs, img_gs_binary = cv.threshold(img_gs, 100, 255, cv.THRESH_BINARY);

    img_edges = cv.Canny(img_gs, 10, 10)

    # Probabilistic hough transform. Probably not using this

    #lines = cv.HoughLinesP(img_edges,rho=1, theta=1*np.pi/180, threshold=10, minLineLength=1, maxLineGap=10);\

    #for i in range(len(lines)):
    #    x1 = lines[i][0][0]
    #    y1 = lines[i][0][1]    
    #    x2 = lines[i][0][2]
    #    y2 = lines[i][0][3]    
    #    cv.line(img_gs,(x1,y1),(x2,y2),(0,0,0),2);

    lines = cv.HoughLines(img_edges, rho=.1, theta=1*np.pi/180, threshold=100);

    for line in lines:
        print(line);
        rho = line[0][0]
        theta = line[0][1]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        
        x1 = int(x0 + 1000*(-b))
        x2 = int(x0 - 1000*(-b))
        y1 = int(y0 + 1000*(a))
        y2 = int(y0 - 1000*(a))
        cv.line(img_gs,(x1,y1),(x2,y2),(0,0,0),5)


    plt.imshow(convertRGB(img_gs));
    #cv.waitKey(0);
    plt.show()



def coverageArea(title):
    """Calculates plant coverage area
    Args:
        title (string): name of the image to be studied
    Returns:
        area (float): coverage area
    """

    if (True):
        print("good");
    img = cv.imread(title);
    img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB);

    plt.figure();
    plt.imshow(img_rgb);
    plt.show();


def convertRGB(img):
    return cv.cvtColor(img, cv.COLOR_BGR2RGB);
    




#coverageArea("cam_test.jpg");
calibrate();