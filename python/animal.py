import random
from mouse import Mouse
from owl import Owl

class Animal(object):

    def __init__(self, neighbors, mice_nearby, owl_nearby):
        self.neighbors = []
        self.mice_nearby = False
        self.owl_nearby = False

    # Naboer og raekkevidde
    # def neighbors(animal, currentSlotI, currentSlotJ):
    #     if (animal == "mouse"):
    #         surrondingSlots = allSlots(currentSlotI, currentSlotJ)
    #         return surrondingSlots
    #     #Lav senere dobbelt saa stor raekkevidde til uglerne
    #     if (animal == "owl"):
    #         surrondingSlots = allSlots(currentSlotI, currentSlotJ)
    #         return surrondingSlots

    def nearby(animal, currentSlotI, currentSlotJ, self):
        allSlots(currentSlotI, currentSlotJ)
        owl_nearby = False
        mouse_nearby = False
        for i in range(len(self.neighbors)):
            if self.neighbors[i].num_owl == 1:
                self.owl_nearby = True
                return self.neighbors[i]
            if self.neighbors[i].num_mice == 1:
                self.mice_nearby = True
                return self.neighbors[i]
         #Lige nu tjekker den kun mangler at flygte


    # Er move true eller false
    def moveMouse():
        num = random.randrange(0,2)
        return (num == 1)

    def moveOwl():
        return True

    #Move regler

    def topSlot(currentSlotI, currentSlotJ):
        topSlot = grid[currentSlotI][currentSlotJ - 1]
        return topSlot

    def bottomSlot(currentSlotI, currentSlotJ):
        bottomSlot = grid[currentSlotI][currentSlotJ + 1]
        return bottomSlot

    def leftSlot(currentSlotI, currentSlotJ):
        leftSlot = grid[currentSlotI - 1][currentSlotJ]
        return leftSlot

    def rightSlot(currentSlotI, currentSlotJ):
        rightSlot = grid[currentSlotI + 1][currentSlotJ]
        return rightSlot

    def allSlots(currentSlotI, currentSlotJ, self):
        del self.neighbors[:]

        topSlot = topSlot(currentSlotI, currentSlotJ)
        self.neighbors.append(topSlot)
        bottomSlot = bottomSlot(currentSlotI, currentSlotJ)
        self.neighbors.append(bottomSlot)
        leftSlot = leftSlot(currentSlotI, currentSlotJ)
        self.neighbors.append(lefttSlot)
        rightSlot = rightSlot(currentSlotI, currentSlotJ)
        self.neighbors.append(rightSlot)

        return self.neighbors
