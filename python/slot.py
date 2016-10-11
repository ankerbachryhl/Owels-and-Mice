class Slot(object):


    def __init__(self, num_mice, num_owls, has_rock):
        self.num_mice = 0;
        self.num_owls = 0;
        self.has_rock = False;


# Sandt falsk vaardi for om jeg kan tilfaeje flere mouses
    def canAddMouse(self):
        return self.num_mice < 2

# Sandt eller falsk om der kan tilfaejes flere ugler
    def canAddOwel(self):
        return self.num_owl < 1


# Tilfaejer en mus eller en ugle til feltet, hvis man f.eks tilfaejer tre mus skal den
#stoppe programmet
    def addAnimal(animal, self):
        if(animal == "mouse"):
            if(canAddMouse()):
                self.num_mice +=1
            else:
                raise Execption("Tried to add to many mice")

        if(animal == "owl"):
            if(canAddOwel()):
                self.num_owl +=1
            else:
                raise Exception("Tried to add to many owls")


# Fjerner en mus fra feltet, hvis man praever at fjerne en mus der ikke er der skal
# den stoppe programmet
    def rmAnimal(animal, self):
        if(animal == "mouse"):
            if (self.num_mice < 1):
                raise Exception("Tried to remove a mouse that didn't exixst")
            else:
                self.num_mice -= 1
        if(animal == "owl"):
            if (self.num_owls < 1):
                raise Exception("Tried to remove an owl that didn't exixst")
            else:
                self.num_owel -= 1
