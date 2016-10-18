
from slot import Slot

class Grid(object):
    rows = 20
    columns= 20
    grid = [[]]
    def __init__(self,):
        self.grid = [[0 for x in range(columns)] for x in range(rows)]

    # Skriv kode der laver et slot i hvert plads i griddet.
    def createSlot(self):
        for i in range(rows):
            for j in range(columns):
                self.grid[i][j] = Slot()


    def getNeighbors(currentSlot, currentSlotI, currentSlotJ):
        nSlot =   grid[currentSlotI][currentSlotJ + 1]
        neSlot = grid[currentSlotI + 1][currentSlotJ + 1]
        eSlot = grid[currentSlotI + 1][currentSlotJ]
        seSlot = grid[currentSlotI + 1][currentSlotJ - 1]
        sSlot = grid[currentSlotI][currentSlotJ - 1]
        swSlot = grid[currentSlotI - 1][currentSlotJ - 1]
        wSlot = grid[currentSlotI - 1][currentSlotJ]
        nwSlot = grid[currentSlotI - 1][currentSlotJ + 1]
        moveDic = {'N' :  nSlot.dicSlot(), 'NE' :  neSlot.dicSlot(), 'E' :  eSlot.dicSlot(), 'SE' :  seSlot.dicSlot(), 'S' :  sSlot.dicSlot(), 'SW' :  swSlot.dicSlot(), 'W' :  wSlot.dicSlot(), "NW" : wSlot.dicSlot()}


    # # Tager og flytter en ugle eller en mus fra et felt til et andet felt.
    # def moveAnimal(newSlot, currentSlot, animal, currentSlotI, currentSlotJ):
    #     #Direction to move
    #     random_num = random.randrange(0,4)
    #     if random_num == 0:
    #         newSlot = topSlot(currentSlotI, currentSlotJ)
    #     if random_num == 1:
    #         newSlot = bottomSlot(currentSlotI, currentSlotJ)
    #     if random_num == 2:
    #         newSlot = leftSlot(currentSlotI, currentSlotJ)
    #     if random_num == 3:
    #         newSlot = rightSlot(currentSlotI, currentSlotJ)
    #     #When to move
    #     if moveMouse():
    #         currentSlot.rmAnimal("mouse")
    #         newSlot.addAnimal("mouse")
    #         currentSlot = newSlot
    #     if moveOwl():
    #         currentSlot.rmAnimal("owl")
    #         newSlot.addAnimal("owl")
    #         currentSlot = newSlot



    # printer alle felter ud i terminalen
    def printSlots(self):
        for i in range(20):
            for j in range(20):
                print self.grid[i][j]
