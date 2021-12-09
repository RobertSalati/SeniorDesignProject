import numpy as np;
w = 0.229/2;
l=0.375/2;
h=0.005;
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
        print("\nPlant", self.num+1, "\n    Plant Position: (", self.xpos, ",", self.ypos, ")");

def selectPlants():
    """Function which takes user input to decide which plants will have pictures taken of them
    Args:
        None.
    Returns:
        Plants (Array, type Object) Array of plant objects.
    """
    data = np.genfromtxt("plantLocs.txt", skip_header=2);        # Read plant locations from text file
    locs = data[:,2:4].astype('float');
    #locs = np.array([[l/2,w/2],[l/2,0],[l/2,-w/2],[0,-w/2],[0,0],[0,w/2],[-l/2, w/2],[-l/2,0],[-l/2,-w/2]]);
    
    plants = np.empty(len(locs),dtype=object);         # Create empty array for plant objects (maybe replace).

    # Initial loop to find what plants will be worked with.
    count = 0;

    while (True):

        plantNum = input("\nPlant number: ");

        if (plantNum == "done" or plantNum == "Done"):      # Done inputting values
            break;      

        elif (plantNum == "all" or plantNum == "All"):      # Want to take pictures of all plants
            for i in range(len(locs)):
                plants[i]=(Plant(i,locs[i][0],locs[i][1]));
                count = len(locs);
            break;

        else: 
            plantNum = int(plantNum)-1          # Adds one plant at a time
            plant = Plant(plantNum,locs[plantNum][0],locs[plantNum][1]);
            plant.printPlant();
            plants[count] = (plant);

        count += 1;

    plants = plants[0:count];
    print("Confirm plants: ")
    for plant in plants:
        plant.printPlant();

    return plants;

selectPlants();