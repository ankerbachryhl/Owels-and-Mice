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
        self.numOwels = 2
        self.rocks = 5

        self.currentMouseSlots = []
        self.currentOwlSlots = []
        self.MouseNumber = 0
        self.randomSpawn()

    #Spawner alle tingene random med foreloop og putter dem ind i et grid, give dem alle sammen en currentSlot
    def randomSpawn(self):
        for i in range(170):
            if self.MouseNumber < 150:
                x = random.randrange(1, 19)
                y = random.randrange(1, 19)
                currentMouseSlot = self.grid[x][y]
                if currentMouseSlot.num_mice < 2:
                    currentMouseSlot.addAnimal("mouse")
                    self.MouseNumber += 1
        for i in range(self.numOwels):
            x = random.randrange(1,19)
            y = random.randrange(1,19)
            currentOwlSlot = self.grid[x][y]
            if currentOwlSlot.num_owels == 0:
                currentOwlSlot.addAnimal("owl")
            else:
                second_x = random.randrange(1,19)
                second_y = random.randrange(1,19)
                currentOwlSlot = self.grid[second_x][second_y]
                currentOwlSlot.addAnimal("owl")
        for i in range(self.rocks):
            x = random.randrange(1,19)
            y = random.randrange(1,19)
            currentRockSpot = self.grid[x][y]
            if currentRockSpot.has_rock == False:
                currentRockSpot.has_rock = True
            else:
                second_x = random.randrange(1,19)
                second_y = random.randrange(1,19)
                currentRockSpot = self.grid[second_x][second_y]
                currentRockSpot.has_rock = True

    def checkForMouse(self):
        self.currentMouseSlots = []
        for i in range(0, 22):
            for j in range(0, 22):
                if self.grid[i][j].num_mice == 1:
                    self.currentMouseSlots.append(self.grid[i][j])
                elif self.grid[i][j].num_mice == 2:
                    self.currentMouseSlots.append(self.grid[i][j])
                    self.currentMouseSlots.append(self.grid[i][j])
                elif self.grid[i][j].num_mice == 3:
                    self.currentMouseSlots.append(self.grid[i][j])
                    self.currentMouseSlots.append(self.grid[i][j])
                    self.currentMouseSlots.append(self.grid[i][j])

    def checkForOwl(self):
        self.currentOwlSlots = []
        for i in range(0, 22):
            for j in range(0, 22):
                if self.grid[i][j].num_owels == 1:
                    self.currentOwlSlots.append(self.grid[i][j])
                elif self.grid[i][j].num_owels == 2:
                    self.currentOwlSlots.append(self.grid[i][j])
                    self.currentOwlSlots.append(self.grid[i][j])



    #Med foreloop gaa igennem fx. hver mus og kald mouseMove og brug rmAnimal and addAnimal
    def moveMouse(self):
        self.checkForMouse()
        print(len(self.currentMouseSlots))
        for i in range(len(self.currentMouseSlots)):
            currentMouseSlot = self.currentMouseSlots[i]
            currentMouseSlotI = self.currentMouseSlots[i].cordI
            currentMouseSlotJ = self.currentMouseSlots[i].cordJ
            self.getNeighbors(currentMouseSlot, currentMouseSlotI, currentMouseSlotJ)
            self.mouseMoveRules(currentMouseSlot, currentMouseSlotI, currentMouseSlotJ)
            self.newMouse(currentMouseSlot)

    def moveOwl(self):
        self.checkForOwl()
        print(len(self.currentOwlSlots))
        for i in range(len(self.currentOwlSlots)):
            currentOwlSlot = self.currentOwlSlots[i]
            currentOwlSlotI = self.currentOwlSlots[i].cordI
            currentOwlSlotJ = self.currentOwlSlots[i].cordJ
            self.getNeighbors(currentOwlSlot, currentOwlSlotI, currentOwlSlotJ)
            self.owlMoveRules(currentOwlSlot)
            value = currentOwlSlot.dicSlot()
            self.owlEat(value, currentOwlSlot)

    #Styrere steps
    def steps(self):
        threading.Timer(5.0, self.steps).start()
        self.moveMouse()
        self.moveOwl()
        self.print_ten_Slots()
        print(self.MouseNumber)


simulation_one = Sim()

simulation_one.steps()
