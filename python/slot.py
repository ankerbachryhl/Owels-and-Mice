class Slot(object):


    def __init__(self, cordI, cordJ):
        self.cordI = cordI
        self.cordJ = cordJ
        self.num_mice = 0;
        self.num_owls = 0;
        self.has_rock = False;
        self.all_animals = self.num_mice + self.num_owls

        self.wall = False

    def checkWall(self):
        if self.cordI - 1 == -1:
            self.wall = True
        if self.cordI + 1 == 20:
            self.wall = True
        if self.cordJ - 1 == -1:
            self.wall = True
        if self.cordJ + 1 == 20:
            self.wall = True



# Sandt falsk vaardi for om jeg kan tilfaeje flere mouses
    def canAddMouse(self):
        return self.num_mice < 2

# Sandt eller falsk om der kan tilfaejes flere ugler
    def canAddOwel(self):
        return self.num_owl < 1

# Tilfaejer en mus eller en ugle til feltet, hvis man f.eks tilfaejer tre mus skal den
#stoppe programmet
    def addAnimal(self, animal):
        if(animal == "mouse"):
            if(self.canAddMouse()):
                self.num_mice += 1
            else:
                # raise Execption("Tried to add to many mice")
                pass

        if(animal == "owl"):
            if(self.canAddOwel()):
                self.num_owl +=1
            else:
                raise Exception("Tried to add to many owls")


# Fjerner en mus fra feltet, hvis man praever at fjerne en mus der ikke er der skal
# den stoppe programmet
    def rmAnimal(self, animal):
        pass
        if(animal == "mouse"):
            if (self.num_mice == 0):
                self.num_mice = 0
            else:
                self.num_mice -= 1
        if(animal == "owl"):
            if (self.num_owls < 1):
                raise Exception("Tried to remove an owl that didn't exixst")
            else:
                self.num_owel -= 1

# Retunerer en liste over hvad der er  i slottet
# {numMice: 2, numOwes : 0, hasRock : False}
    def dicSlot(self):
        slotDic = {'numMice' :  self.num_mice, 'numOwels':  self.num_owls, 'hasRock' : self.has_rock, 'allAnimals' : self.all_animals, 'hasWall' : self.wall}
        return slotDic
