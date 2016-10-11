
from slot import Slot

class Grid(object):
    rows = 20
    columns= 20

    def __init__(self, grid):
        self.grid = [[0 for x in range(columns)] for x in range(rows)]

    # Skriv kode der laver et slot i hvert plads i griddet.
    def createSlot(self):
        for i in range(rows):
            for j in range(columns):
                self.grid[i][j] = Slot()





    # Tager og flytter en ugle eller en mus fra et felt til et andet felt.
    def moveAnimal(oldSlot, newSlot, animal, currentSlotI, currentSlotJ):
        #Direction to move
        random_num = random.randrange(0,4)
        if random_num == 0:
            oldSlot = currentSlot
            newSlot = topSlot(currentSlotI, currentSlotJ)
        if random_num == 1:
            oldSlot = currentSlot
            newSlot = bottomSlot(currentSlotI, currentSlotJ)
        if random_num == 2:
            oldSlot = currentSlot
            newSlot = leftSlot(currentSlotI, currentSlotJ)
        if random_num == 3:
            oldSlot = currentSlot
            newSlot = rightSlot(currentSlotI, currentSlotJ)
        #When to move
        if moveMouse():
            oldSlot.rmAnimal("mouse")
            newSlot.addAnimal("mouse")
        if moveOwl():
            oldSlot.rmAnimal("owl")
            newSlot.addAnimal("owl")



    # printer alle felter ud i terminalen
    def printSlots(self):
        for i in range(20):
            for j in range(20):
                print self.grid[i][j]
