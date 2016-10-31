from grid import Grid
from thing import Thing
from animal import Animal
import threading
import random
from mouse import Mouse




class Sim(Animal):

    #init
    def __init__(self):
        # Grid.__init__(self)
        Animal.__init__(self)
        self.numOwels = 2
        self.rocks = 10

        self.currentMouseSlots = []
        self.currentOwlSlots = []
        self.MouseNumber = 0

        self.allMices1 = []

        self.allMices = []

        self.random = []
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
                    self.allMices.append(Mouse(x, y, 'x'))

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


    # def checkForAllMices(self):
    #     for i in range(len(self.currentMouseSlots)):
    #         self.allMices[i].mouse_steps += 1


    # def ggcomeon(self):
    #     for i in range(len(self.currentMouseSlots)):
    #         steps = self.allMices[i].mouse_steps
    #         self.random.append(Mouse())
    #         self.random[i].mouse_steps + steps
    #         self.random[i].checkIfDead()
    #         if self.random[i].dead == True:
    #             self.grid[self.currentMouseSlots[i].cordI][self.currentMouseSlots[i].cordJ].rmAnimal("mouse")
    #         self.allMices = []
    #
    #
    #


    #Med foreloop gaa igennem fx. hver mus og kald mouseMove og brug rmAnimal and addAnimal
    def moveMouse(self):
        self.checkForMouse()
        print(len(self.currentMouseSlots))
        for i in range(len(self.allMices)):
            if hasattr(self.allMices[i], 'x'):
                currentMouseSlot = self.grid[self.allMices[i].x][self.allMices[i].y]
                currentMouseSlotI = self.allMices[i].x
                currentMouseSlotJ = self.allMices[i].y

                value = currentMouseSlot.dicSlot()
                self.owlEat(value, currentMouseSlot)

                if self.mouseEaten == True:
                    self.allMices[i] = self.allMices[:i] + self.allMices[i+1 :]
                else:

                    if(self.allMices[i].mouse_steps == 20):
                        currentMouseSlot.rmAnimal("mouse")
                        self.allMices[i] = self.allMices[:i] + self.allMices[i+1 :]
                        self.MouseNumber -= 1
                    else:
                        self.newMouse(currentMouseSlot)
                        self.getNeighbors(currentMouseSlot, currentMouseSlotI, currentMouseSlotJ)
                        self.mouseMoveRules(currentMouseSlot, currentMouseSlotI, currentMouseSlotJ)
                        self.allMices[i].mouse_steps += 1


                        if self.movedN == True:
                            self.allMices[i].x = self.nSlot.cordI
                            self.allMices[i].y = self.nSlot.cordJ
                        if self.movedNE == True:
                            self.allMices[i].x = self.neSlot.cordI
                            self.allMices[i].y = self.neSlot.cordJ
                        if self.movedE == True:
                            self.allMices[i].x = self.eSlot.cordI
                            self.allMices[i].y = self.eSlot.cordJ
                        if self.movedSE == True:
                            self.allMices[i].x = self.seSlot.cordI
                            self.allMices[i].y = self.seSlot.cordJ
                        if self.movedS == True:
                            self.allMices[i].x = self.sSlot.cordI
                            self.allMices[i].y = self.sSlot.cordJ
                        if self.movedSW == True:
                            self.allMices[i].x = self.swSlot.cordI
                            self.allMices[i].y = self.swSlot.cordJ
                        if self.movedW == True:
                            self.allMices[i].x = self.wSlot.cordI
                            self.allMices[i].y = self.wSlot.cordJ
                        if self.movedNW == True:
                            self.allMices[i].x = self.nwSlot.cordI
                            self.allMices[i].y = self.nwSlot.cordJ



                # self.newMouse(currentMouseSlot)


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
        numSteps = 1

        while numSteps > 0:
            print "How many steps do you wanna run? Press 0 to stop! "
            numSteps = input()
            for i in range(numSteps):
                self.moveMouse()
                self.moveOwl()
            self.print_ten_Slots()
            print(self.MouseNumber)
            if self.MouseNumber == 0:
                print 'All the mouses died so the simulation has ended, goodbye!'
                print 'number of owls left: ', len(self.currentOwlSlots)
                numSteps = 0



simulation_one = Sim()

simulation_one.steps()
