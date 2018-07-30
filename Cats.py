# May pena
# This program reads a csv file with cat information and
# sorts cats in 4 different ways by using a class
# called Cats. 


def orgFile( fileName ):
    # open a csv file
    file = open( fileName, "r" )
    lines = file.readlines()
    file.close()
    catlist = []
    
    # process each line of the file
    for line in lines:

        # split the line at the commas
        words = line.strip().split( ", " )
        
        # skip lines that do not have 5 fields
        if len( words ) != 5:
            continue
        
        #organizes the words into name, age, vac....

        name  = words[0]
        age   = words[1]
        vacc  = words[2]
        tat   = words[3]
        breed = words[4]
        
        #turns vacc and tat into a boolean 
        vacc = vacc == 'vaccinated'
        tat  =  tat == 'not tattooed'
        
        #the output we want
        cat  = Cat( name,breed, vacc, tat, int(age) )
        catlist.append(cat)
   
    return catlist


class Cat:
    """a class that implements a cat and its
    information.  Name, breed, vaccinated,
    tattooed, and age."""

    def __init__( self, na, brd, vacc, tat, ag ):
        """constructor.  Builds a cat with all its information"""
        self.name       = na
        self.breed      = brd
        self.vaccinated = vacc
        self.age        = ag
        self.tattooed   = tat

    def isVaccinated( self ):
        """returns True if cat is vaccinated, False otherwise"""
        return self.vaccinated

    def getAge( self ):
        """returns cat's age"""
        return self.age

    def getName( self ):
        """returns name of cat"""
        return self.name

    def getBreed(self):
        """returns the breed of the cat"""
        return self.breed
    
    def isTattooed(self):
        return self.tattooed

    def __str__( self ):
        """default string representation of cat"""
        vacc = "vaccinated"
        if not self.vaccinated:
            vacc = "not vaccinated"
            
        tat= "not tattooed"
        if not self.tattooed:
            tat= "tattooed"
        
        return "{0:20}:==> {1:1}, {2:1}, {3:1}, {4:1} yrs old".format(
            self.name, self.breed, vacc, tat, self.age )
    
def main():
    print( "Enter below the name of the csv file. For example: test.csv" )
    cats = orgFile( input( "File name: " ) )

    # print the list of all the cats and the ones that share the same properties
    print( "\nComplete List:" )
    for cat in cats:
        print( cat )
    print("\nNon-vaccinated cats:")
    for cat in cats:
        if cat.vaccinated == False:
            print(cat)
    print("\nStray cats:")
    for cat in cats:
        if cat.breed == "stray":
            print(cat)
    print("\nNon-vaccinated cats 2 or older:")
    for cat in cats:
        if cat.vaccinated == False and cat.age >= 2:
            print (cat)
    print("\nNon-tattooed cats:")
    for cat in cats:
        if cat.tattooed == True:
            print(cat)
    print("\nNot vaccinated and tattooed cats:")
    for cat in cats:
        if cat.vaccinated == False and cat.tattooed == True:
            print(cat)          

main()
