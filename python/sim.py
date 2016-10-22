from grid import Grid
from thing import Thing
from animal import Animal
import threading
import random





class Sim(Animal):

    #init
    def __init__(self):
        # Grid.__init__(self)
        Animal.__init__(self)
        self.numMice = 3
        self.numOwels = 2
        self.rocks = 5

        self.currentMouseSlots = []
        self.currentOwlSlots = []

        self.randomSpawn()



    #Spawner alle tingene random med foreloop og putter dem ind i et grid, give dem alle sammen en currentSlot
    def randomSpawn(self):
        for i in range(self.numMice):
            mx = random.randrange(0,20)
            my = random.randrange(0,20)
            currentMouseSlot = self.grid[mx][my]
            currentMouseSlot.addAnimal("mouse")
            # self.currentMouseSlots.append(currentMouseSlot)
        for i in range(self.numOwels):
            pass
            # ox = random.randrange(20)
            # oy = random.randrange(20)
            # currentOwlSlot = self.grid[mx][my]
            # currentOwlSlot.addAnimal("mouse")
            # self.currentOwlSlots.append(currentOwlSlot)

    def checkForMouse(self):
        self.currentMouseSlots = []
        for i in range(0, 20):
            for j in range(0, 20):
                if self.grid[i][j].num_mice == 1:
                    self.currentMouseSlots.append(self.grid[i][j])
                elif self.grid[i][j].num_mice == 2:
                    self.currentMouseSlots.append(self.grid[i][j])
                    self.currentMouseSlots.append(self.grid[i][j])


    #Med foreloop gaa igennem fx. hver mus og kald mouseMove og brug rmAnimal and addAnimal
    def moveMouse(self):
        self.checkForMouse()
        print(len(self.currentMouseSlots))
        for i in range(len(self.currentMouseSlots)):
            currentMouseSlot = self.currentMouseSlots[i]
            currentMouseSlotI = self.currentMouseSlots[i].cordI
            currentMouseSlotJ = self.currentMouseSlots[i].cordJ
            currentMouseSlot.checkWall()
            self.getNeighbors(currentMouseSlot, currentMouseSlotI, currentMouseSlotJ)
            self.mouseMoveRules(currentMouseSlot, currentMouseSlotI, currentMouseSlotJ)



    def moveOwl(self):
        for i in range(len(self.currentOwlSlots)):
            currentOwlSlot = self.currentOwlSlots[i]
            currentOwlSlotI = self.currentOwlSlots[i].cordI
            currentOwlSlotJ = self.currentOwlSlots[i].cordJ
            self.getNeighbors(currentOwlSlot, currentOwlSlotI, currentOwlSlotJ)
            self.owlMoveRules(currentOwlSlot)
            print(currentMouseSlot.num_mice)
            self.checkForMouse()




    #Styrere steps
    def steps(self):
        threading.Timer(5.0, self.steps).start()
        self.moveMouse()
        self.print_ten_Slots()

    #Searger for at dyrene bevaeger sig efter hvert step

simulation_one = Sim()

simulation_one.steps()
