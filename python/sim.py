from grid import Grid
from thing import Thing
import random
import threading

class Sim(object):

    #init
    def __init__(self):
        self.numMice = 150
        self.numOwels = 2
        self.rocks = 5


    #Spawner alle tingene random med foreloop og putter dem ind i et grid, give dem alle sammen en currentSlot
    def randomSpawn(self):
        for i in numMice:
            y = random.randrange(0,20)
            x = random.randrange(0,20)
            currentSlot = grid[y][x]
            currentSlot.addAnimal("mouse")

    def checkForMouse(self):
        allMices = []
        allMicesI = []
        allMicesJ = []
        for i in range(20):
            for j in range(20):
                if grid[i][j].num_mice == 1:
                    currentSlot = grid[i][j]
                    currentSlotI = i
                    currentSlotJ = j
                    allMices.append(currentSlot)
                    allMicesI.append(currentSlotI)
                    allmicesJ.append(currentSlotJ)
                if grid[i][j].num_mice == 2:
                    currentSlot = grid[i][j]
                    currentSlotI = i
                    currentSlotJ = j
                    allMices.append(currentSlot)
                    allMicesI.append(currentSlotI)
                    allmicesJ.append(currentSlotJ)
                    #Second time
                    allMices.append(currentSlot)
                    allMicesI.append(currentSlotI)
                    allmicesJ.append(currentSlotJ)

    #Med foreloop gaa igennem fx. hver mus og kald mouseMove og brug rmAnimal and addAnimal
    def moveMouse(self):
        self.checkForMouse()
        for i in len(allMices):
            currentSlot = allMices[i]
            currentSlotI = allMicesI[i]
            currentSlotJ = allMicesJ[i]
            getNeigbors(currentSlot, currentSlotI, currentSlotJ)
            mouseMoveRules(currentSlot)

    #Styrere steps
    def steps(self):
        self.randomSpawn()
        self.moveMouse()
        threading.Timer(60, steps).start()


    #Searger for at dyrene bevaeger sig efter hvert step
    def movement(animal):
        pass

firstSim = Sim()

firstSim.steps()
