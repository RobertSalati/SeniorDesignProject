from camera import *;
import cv2 as cv;

numShelf = int(input("Shelf number: "));
numPlant = int(input("Plant number: "));
name = takePicture(numShelf,numPlant);

image = cv.imread(name);

print(image);

cv.imshow("test", image);

