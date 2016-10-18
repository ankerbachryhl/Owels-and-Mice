import random
from mouse import Mouse
from owl import Owl

class Animal(object):

    def __init__(self, neighbors, mice_nearby, owl_nearby):
        self.neighbors = []
        self.mice_nearby = False
        self.owl_nearby = False



    # def nearby(animal, currentSlotI, currentSlotJ, self):
    #     allSlots(currentSlotI, currentSlotJ)
    #     owl_nearby = False
    #     mouse_nearby = False
    #     for i in range(len(self.neighbors)):
    #         if self.neighbors[i].num_owl == 1:
    #             self.owl_nearby = True
    #             return self.neighbors[i]
    #         if self.neighbors[i].num_mice == 1:
    #             self.mice_nearby = True
    #             return self.neighbors[i]
         #Lige nu tjekker den kun mangler at flygte


    # Er move true eller false
    def moveMouse():
        num = random.randrange(0,2)
        return (num == 1)

    def moveOwl():
        return True
