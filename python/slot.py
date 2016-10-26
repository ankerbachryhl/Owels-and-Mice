class Slot(object):


    def __init__(self, cordI, cordJ):
        self.cordI = cordI
        self.cordJ = cordJ
        self.num_mice = 0;
        self.num_owels = 0;
        self.has_rock = False;

        self.all_animals = self.num_mice + self.num_owels


# Sandt falsk vaardi for om jeg kan tilfaeje flere mouses
    def canAddMouse(self):
        return self.num_mice < 2

# Sandt eller falsk om der kan tilfaejes flere ugler
    def canAddOwel(self):
        return self.num_owels < 10

# Tilfaejer en mus eller en ugle til feltet, hvis man f.eks tilfaejer tre mus skal den
#stoppe programmet
    def addAnimal(self, animal):
        if(animal == "owl"):
            if(self.canAddOwel()):
                self.num_owels += 1
            else:
                pass
        if(animal == "mouse"):
            if(self.canAddMouse()):
                self.num_mice += 1

            else:
                pass

# Fjerner en mus fra feltet, hvis man praever at fjerne en mus der ikke er der skal
# den stoppe programmet
    def rmAnimal(self, animal):
        if(animal == "mouse"):
            if (self.num_mice == 0):
                raise Exception('tried to remove a mouse that didn*t exixst')
            else:
                self.num_mice -= 1
        if(animal == "owl"):
            if (self.num_owels < 1):
                pass
            else:
                self.num_owels -= 1

# Retunerer en liste over hvad der er  i slottet
# {numMice: 2, numOwes : 0, hasRock : False}
    def dicSlot(self):
        slotDic = {'numMice' :  self.num_mice, 'numOwels':  self.num_owels, 'hasRock' : self.has_rock, 'allAnimals' : self.all_animals}
        return slotDic
