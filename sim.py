from mouse import Mouse
from animal import Animal
import random

class Sim(Animal):

    #Laver start variabler
    def __init__(self):
        Animal.__init__(self)
        self.numOwels = 0
        self.rocks = 0
        self.MouseNumber = 0

        self.currentOwlSlots = []
        self.currentStoneSlots = []
        self.allMices = []

        self.totalSteps = 0

        self.randomSpawn()

    #Spawner alle tingene random med foreloop og putter dem ind i et grid, giver dem alle sammen en currentSlot
    def randomSpawn(self):
        #Spawner musene
        for i in range(170):
            if self.MouseNumber < 150:
                x = random.randrange(1, 19)
                y = random.randrange(1, 19)
                currentMouseSlot = self.grid[x][y]
                if currentMouseSlot.num_mice < 2:
                    currentMouseSlot.addAnimal("mouse")
                    self.MouseNumber += 1
                    self.allMices.append(Mouse(x, y, 'x'))
        #Spawner uglerne
        for i in range(50):
            if self.numOwels < 2:
                x = random.randrange(1,19)
                y = random.randrange(1,19)
                currentOwlSlot = self.grid[x][y]
                if currentOwlSlot.num_owels == 0:
                    currentOwlSlot.addAnimal("owl")
                    self.numOwels += 1
        #Placere stenene
        for i in range(50):
            if self.rocks < 10:
                x = random.randrange(1,19)
                y = random.randrange(1,19)
                currentRockSpot = self.grid[x][y]
                if currentRockSpot.has_rock == False:
                    currentRockSpot.has_rock = True
                    self.rocks += 1
                    self.currentStoneSlots.append(currentRockSpot)

    #Checker for ugler inden hvert step og giver dem et currentSlot
    def checkForOwl(self):
        self.currentOwlSlots = []
        for i in range(0, 22):
            for j in range(0, 22):
                if self.grid[i][j].num_owels == 1:
                    self.currentOwlSlots.append(self.grid[i][j])


    #Gaar med foreloop igennem alle musene og soerger for de bevaeger sig.
    def moveMouse(self):
        for i in range(len(self.allMices)):

            #Tjekker om musene eksistere
            if hasattr(self.allMices[i], 'x'):

                #Giver et currentSlot, currentSlotI og currentSlotJ til alle musene.
                currentMouseSlot = self.grid[self.allMices[i].x][self.allMices[i].y]
                currentMouseSlotI = self.allMices[i].x
                currentMouseSlotJ = self.allMices[i].y

                #Checker om nogle af musene doer ved at uglene aeder dem.
                #Hvis nogle af dem er doede saa bliver de fjernet fra allMices arrayen.
                currentDicSlot = currentMouseSlot.dicSlot()
                self.owlEat(currentDicSlot, currentMouseSlot)

                if self.mouseEaten == True:
                    self.allMices[i] = self.allMices[:i] + self.allMices[i+1 :]
                else:

                #Hvis de ikke allerede er blevet spist saa checker den hvor mange steps hver af musene har gaaet.
                    if(self.allMices[i].mouse_steps == 20):
                        currentMouseSlot.rmAnimal("mouse")
                        self.allMices[i] = self.allMices[:i] + self.allMices[i+1 :]
                        self.MouseNumber -= 1
                    else:

                #Og hvis musen ikke doer pga. for mange steps og ikke doer pga. en ugle spiser den saa bevaeger musen sig.
                #Og opdatere derefter dens kordinater

                        #Tjekker om der er nogle mus der parrer sig.
                        self.newMouse(currentMouseSlot)
                        #Tjekker naboerne
                        self.getNeighbors(currentMouseSlot, currentMouseSlotI, currentMouseSlotJ)
                        #Bevaeger sig ud fra dataerne om naboerne
                        self.mouseMoveRules(currentMouseSlot, currentMouseSlotI, currentMouseSlotJ)
                        #Giver den et steps mere
                        self.allMices[i].mouse_steps += 1

                        #Opdater kordinaterne
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

    #Seorger for uglen
    def moveOwl(self):
        self.checkForOwl()
        for i in range(len(self.currentOwlSlots)):

            #Giver et currentSlot, currentSlotI og currentSlotJ til alle uglerne.
            currentOwlSlot = self.currentOwlSlots[i]
            currentOwlSlotI = self.currentOwlSlots[i].cordI
            currentOwlSlotJ = self.currentOwlSlots[i].cordJ

            #Tjekker naboer og soerger for at uglen bevaeger sig
            self.getNeighbors(currentOwlSlot, currentOwlSlotI, currentOwlSlotJ)
            self.owlMoveRules(currentOwlSlot)

    #Seorger for stenen
    def checkStone(self):
        for i in range(len(self.currentStoneSlots)):
            if self.currentStoneSlots[i].hideUnderRock == True and self.currentStoneSlots[i].num_mice == 0:
                self.currentStoneSlots[i].hideUnderRock == False


    #Styrere stepsene
    def steps(self):
        numSteps = 1

        while numSteps > 0:
            print "How many steps do you wanna run? Press 0 to stop! "
            numSteps = input()
            for i in range(numSteps):
                self.moveMouse()
                self.moveOwl()
                self.checkStone()
                self.totalSteps += 1

            for i in range(0, 22):
                for j in range(0, 22):
                    self.grid[i][j].checkState()

            self.printSlots()
            print 'Mice left:', self.MouseNumber
            print 'Owels left:', len(self.currentOwlSlots)
            print 'Stones left:', self.rocks
            print 'Total steps:', self.totalSteps
            print("\n")

            if self.MouseNumber == 0:
                print("\n")
                print 'All the mouses died so the simulation has ended, goodbye!'
                print("\n")
                print 'Number of owels left: ', len(self.currentOwlSlots)
                print 'Number of mice left: ', self.MouseNumber
                print 'Number of rocks left: ', self.rocks
                print 'Total steps: ', self.totalSteps
                numSteps = 0


#Starter steps funktionen
simulation_one = Sim()
simulation_one.steps()
