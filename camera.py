#from picamera import PiCamera;
import numpy as np;
import time as time;
from datetime import datetime;
import cv2 as cv;
import matplotlib.pyplot as plt;
#from motor import *;

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

    else:  # Creates file name for storage
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

    title = "calibrate.jpg";
    #title = takePicture(numShelf=0,numPlant=0,calibrate=True);  # Takes calibration picture
    
    img = cv.imread(title);     # Creates numpy array of the image

    width = int(img.shape[1] * 0.5)
    
    # New height
    height = int(img.shape[0] * 0.5)
    
    # New dimensions
    dim = (width, height)
    
    # Resize image
    img = cv.resize(img, dim, interpolation = cv.INTER_AREA)

    img = cv.rotate(img,cv.ROTATE_180);

    img_gs = cv.cvtColor(img, cv.COLOR_BGR2GRAY);       # Converts image to grayscale

    img_blur = cv.GaussianBlur(img,(5,5),0);

    thresh_rgb, img_rgb_binary = cv.threshold(img_blur, 40, 255, cv.THRESH_BINARY);

    thresh_gs, img_gs_binary = cv.threshold(img_blur, 70, 255, cv.THRESH_BINARY);

    img_edges = cv.Canny(img_rgb_binary, 10, 10)

    # Probabilistic hough transform

    lines = cv.HoughLinesP(img_edges,rho=1, theta=1*np.pi/180, threshold=10, minLineLength=10, maxLineGap=10);
    corners = [];

    for i in range(len(lines)):
        x1 = lines[i][0][0]
        y1 = lines[i][0][1]    
        x2 = lines[i][0][2]
        y2 = lines[i][0][3]    
        cv.line(img_rgb_binary,(x1,y1),(x2,y2),(0,255,0),5);
        corners.append([x1,y1]); corners.append([x2,y2]);
    corners = np.array(corners);
    cornersMag = np.empty(len(corners));
    for i in range(len(corners)):
        cornersMag[i] = np.linalg.norm(corners[i]);

    topLeft = corners[np.argmin(cornersMag)];
    botRight = corners[np.argmax(cornersMag)];
    print(topLeft); print(botRight);

    center = np.abs(topLeft+botRight)/2;

    l = np.sqrt(2*((topLeft[0]-botRight[0])**2+(topLeft[1]-botRight[1])**2));

    lpp = 3/l;

    app = 9/l**2;

    # Now for actually moving the camera

    if (center[0] < width/2-100 or center[0] > width/2+100 or center[1] < height/2-100 or center[1] > height/2+100):
        print("calibrating");
        currentPos = [];



    plt.imshow(convertRGB(img_rgb_binary));
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