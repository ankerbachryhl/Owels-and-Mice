#pygamec

import random
from grid import Grid

class Mouse(Grid):

    def __init__(self):
        Grid.__init__(self)
        self.mouse_steps = 0
        self.dead = False



    #Steps 20 steps = dead
    def dead(self):
        if self.mouse_steps == 20:
            self.dead = True

    #Move regler for mouse, bruger neighbors like self.moveMouseDic['numMice']

    def newMouse(self, currentSlot):
        possiblePairingSpot = []
        if currentSlot.num_mice == 2:
            for key in self.moveMouseDic:
                if self.moveMouseDic[key]['numMice'] == 0 and self.moveMouseDic[key]['numOwels'] == 0:
                    possiblePairingSpot.append(key)

            rand_five = random.randrange(0,10)
            # 10% chance for at en ny mus spawner paa et ledigt felt
            if len(possiblePairingSpot) > 0 and rand_five == 9:
                rand_four = random.randrange(len(possiblePairingSpot))
                if possiblePairingSpot[rand_four] == 'N':
                    self.nSlot.addAnimal("mouse")
                    self.MouseNumber += 1
                if possiblePairingSpot[rand_four] == 'NE':
                    self.neSlot.addAnimal("mouse")
                    self.MouseNumber += 1
                if possiblePairingSpot[rand_four] == 'E':
                    self.eSlot.addAnimal("mouse")
                    self.MouseNumber += 1
                if possiblePairingSpot[rand_four] == 'SE':
                    self.seSlot.addAnimal("mouse")
                    self.MouseNumber += 1
                if possiblePairingSpot[rand_four] == 'S':
                    self.sSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")
                    self.MouseNumber += 1
                if possiblePairingSpot[rand_four] == 'SW':
                    self.swSlot.addAnimal("mouse")
                    self.MouseNumber += 1
                if possiblePairingSpot[rand_four] == 'W':
                    self.wSlot.addAnimal("mouse")
                    self.MouseNumber += 1
                if possiblePairingSpot[rand_four] == 'NW':
                    self.nwSlot.addAnimal("mouse")
                    self.MouseNumber += 1

    def mouseMoveRules(self, currentSlot, currentSlotI, currentSlotJ):
        rand_one = random.randrange(0,2)
        possibleDirections = []
        stoneSpots = []
        owlAndHide = False

        if rand_one == 1:

            for key in self.moveMouseDic:
                if self.moveMouseDic[key]['numOwels'] == 0 and self.moveMouseDic[key]['numMice'] < 2:
                    possibleDirections.append(key)
                if self.moveMouseDic[key]['hasRock'] == True:
                    stoneSpots.append(key)
                if self.moveMouseDic[key]['numOwels'] == 1 and len(stoneSpots) > 0:
                    owlAndHide = True
                    return owlAndHide
                else:
                    pass

            if len(possibleDirections) > 0:
                if owlAndHide == True:
                    rand_two = random.randrange(len(stoneSpots))
                    if stoneSpots[rand_two] == 'N':
                        self.nSlot.addAnimal("mouse")
                        currentSlot.rmAnimal("mouse")
                    if stoneSpots[rand_two] == 'NE':
                        self.neSlot.addAnimal("mouse")
                        currentSlot.rmAnimal("mouse")
                    if stoneSpots[rand_two] == 'E':
                        self.eSlot.addAnimal("mouse")
                        currentSlot.rmAnimal("mouse")
                    if stoneSpots[rand_two] == 'SE':
                        self.seSlot.addAnimal("mouse")
                        currentSlot.rmAnimal("mouse")
                    if stoneSpots[rand_two] == 'S':
                        self.sSlot.addAnimal("mouse")
                        currentSlot.rmAnimal("mouse")
                    if stoneSpots[rand_two] == 'SW':
                        self.swSlot.addAnimal("mouse")
                        currentSlot.rmAnimal("mouse")
                    if stoneSpots[rand_two] == 'W':
                        self.wSlot.addAnimal("mouse")
                        currentSlot.rmAnimal("mouse")
                    if stoneSpots[rand_two] == 'NW':
                        self.nwSlot.addAnimal("mouse")
                        currentSlot.rmAnimal("mouse")

                else:
                    rand_three = random.randrange(len(possibleDirections))
                    self.movingSlot = possibleDirections[rand_three]

                    if self.movingSlot == 'N':
                        self.nSlot.addAnimal("mouse")
                        currentSlot.rmAnimal("mouse")
                    if self.movingSlot == 'NE':
                        self.neSlot.addAnimal("mouse")
                        currentSlot.rmAnimal("mouse")
                    if self.movingSlot == 'E':
                        self.eSlot.addAnimal("mouse")
                        currentSlot.rmAnimal("mouse")
                    if self.movingSlot == 'SE':
                        self.seSlot.addAnimal("mouse")
                        currentSlot.rmAnimal("mouse")
                    if self.movingSlot == 'S':
                        self.sSlot.addAnimal("mouse")
                        currentSlot.rmAnimal("mouse")

                    if self.movingSlot == 'SW':
                        self.swSlot.addAnimal("mouse")
                        currentSlot.rmAnimal("mouse")

                    if self.movingSlot == 'W':
                        self.wSlot.addAnimal("mouse")
                        currentSlot.rmAnimal("mouse")

                    if self.movingSlot == 'NW':
                        self.nwSlot.addAnimal("mouse")
                        currentSlot.rmAnimal("mouse")
