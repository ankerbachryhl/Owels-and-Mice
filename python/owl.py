from mouse import Mouse
import random

class Owl(Mouse):

    def __init__(self):
        Mouse.__init__(self, 0, 0, 0)
        self.mouseEaten = False

    #Draeber en mus
    def owlEat(self, currentSlot, currentOwlSlot):
        self.mouseEaten = False
        if currentSlot['numOwels'] == 1 and currentSlot['numMice'] == 1:
            currentOwlSlot.rmAnimal("mouse")
            self.MouseNumber -= 1
            self.mouseEaten = True
        elif currentSlot['numOwels'] == 1 and currentSlot['numMice'] == 2:
            currentOwlSlot.rmAnimal("mouse")
            self.MouseNumber -= 1
            self.mouseEaten = True

    def owlMoveRules(self, currentSlot):
        rand_one = random.randrange(0,2)
        possibleDirections = []
        stoneSpots = []

        for key in self.moveOwlDic:
            if self.moveOwlDic[key]['numOwels'] == 0 and self.moveOwlDic[key]['numMice'] == 1 and self.moveOwlDic[key]['hasRock'] == False:
                possibleDirections.append(key)
            if self.moveOwlDic[key]['numOwels'] == 0 and self.moveOwlDic[key]['numMice'] == 2:
                possibleDirections.append(key)
            if len(possibleDirections) == 0:
                if self.moveOwlDic[key]['numOwels'] == 0:
                    possibleDirections.append(key)

        if len(possibleDirections) > 0:

            rand_two = random.randrange(len(possibleDirections))
            self.movingSlot = possibleDirections[rand_two]

            if self.movingSlot == 'N':
                self.nSlot.addAnimal("owl")
                currentSlot.rmAnimal("owl")
            if self.movingSlot == 'NE':
                self.neSlot.addAnimal("owl")
                currentSlot.rmAnimal("owl")
            if self.movingSlot == 'E':
                self.eSlot.addAnimal("owl")
                currentSlot.rmAnimal("owl")
            if self.movingSlot == 'SE':
                self.seSlot.addAnimal("owl")
                currentSlot.rmAnimal("owl")
            if self.movingSlot == 'S':
                self.sSlot.addAnimal("owl")
                currentSlot.rmAnimal("owl")
            if self.movingSlot == 'SW':
                self.swSlot.addAnimal("owl")
                currentSlot.rmAnimal("owl")
            if self.movingSlot == 'W':
                self.wSlot.addAnimal("owl")
                currentSlot.rmAnimal("owl")
            if self.movingSlot == 'NW':
                self.nwSlot.addAnimal("owl")
                currentSlot.rmAnimal("owl")

            if self.movingSlot == 'NN':
                self.nSlot.addAnimal("owl")
                currentSlot.rmAnimal("owl")
            if self.movingSlot == 'EE':
                self.eSlot.addAnimal("owl")
                currentSlot.rmAnimal("owl")
            if self.movingSlot == 'SS':
                self.sSlot.addAnimal("owl")
                currentSlot.rmAnimal("owl")
            if self.movingSlot == 'WW':
                self.wSlot.addAnimal("owl")
                currentSlot.rmAnimal("owl")

            if self.movingSlot in ('NNE', 'NNEE', 'NEE'):
                self.neSlot.addAnimal("owl")
                currentSlot.rmAnimal("owl")
            if self.movingSlot in ('NNW', 'NNWW', 'NWW'):
                self.nwSlot.addAnimal("owl")
                currentSlot.rmAnimal("owl")

            if self.movingSlot in ('SEE', 'SSEE', 'SSE'):
                self.seSlot.addAnimal("owl")
                currentSlot.rmAnimal("owl")
            if self.movingSlot in ('SWW', 'SSWW', 'SSW'):
                self.swSlot.addAnimal("owl")
                currentSlot.rmAnimal("owl")




    #Skal geare saadan at den ikke aeder en mus hvis den gemmer sig
