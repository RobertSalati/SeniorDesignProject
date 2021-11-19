import numpy as np;

class Plant:

    def __init__(self, num, xpos, ypos):
        """Plant Constructor.
        Args:
            num (int): plant number, used for indexing
            xpos (float): plant x location
            ypos (float): plant y location
        Returns: 
            None
        """

        self.num = num;
        self.xpos = xpos; 
        self.ypos = ypos;

    def changeLocation(self, data):
        """Updates plant location in the text file.
        Args:
            None.
        Returns:
            None.
        """

        self.xpos = float(input("New X Position: "));
        self.ypos = float(input("New Y Positiin: "));
        #data = np.genfromtxt("hold.txt",skip_header=2,dtype=str, delimiter=",");
        data[self.num, 1] = self.xpos; data[self.num, 2] = self.ypos;
        np.savetxt("testLocs.txt", data.astype('str'), fmt='%s', delimiter = ', ',header = "Plant #		X	Y \n-------------------------");


    def printPlant(self):
        """Prints out plant information
        Args:
            None.
        Returns:
            None.
        """

        print("Plant", self.num, "\n    Plant Position: (", self.xpos, ",", self.ypos, ")");

plant = Plant(1,2,3);
data = np.genfromtxt("hold.txt",skip_header=2,dtype=str, delimiter=",");
plant.changeLocation(data);
