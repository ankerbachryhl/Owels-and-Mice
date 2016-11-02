import random
from grid import Grid

class Mouse(Grid):

    def __init__(self, x, y, stringAttribute):
        Grid.__init__(self)
        self.mouse_steps = 0
        self.dead = False

        self.x = x
        self.y = y


    #Regler for parring
    def newMouse(self, currentSlot):
        possiblePairingSpot = []

        if currentSlot.num_mice == 2:
            for key in self.moveMouseDic:
                if self.moveMouseDic[key]['numMice'] == 0 and self.moveMouseDic[key]['numOwels'] == 0:
                    possiblePairingSpot.append(key)

            # 10% chance for at en ny mus spawner paa et ledigt felt
            rand_five = random.randrange(0,10)
            if len(possiblePairingSpot) > 0 and rand_five == 9:
                rand_four = random.randrange(len(possiblePairingSpot))

                if possiblePairingSpot[rand_four] == 'N':
                    self.nSlot.addAnimal("mouse")
                    self.MouseNumber += 1
                    self.allMices.append(Mouse(self.nSlot.cordI, self.nSlot.cordJ, 'x'))
                if possiblePairingSpot[rand_four] == 'NE':
                    self.neSlot.addAnimal("mouse")
                    self.MouseNumber += 1
                    self.allMices.append(Mouse(self.neSlot.cordI, self.neSlot.cordJ, 'x'))
                if possiblePairingSpot[rand_four] == 'E':
                    self.eSlot.addAnimal("mouse")
                    self.MouseNumber += 1
                    self.allMices.append(Mouse(self.eSlot.cordI, self.eSlot.cordJ, 'x'))
                if possiblePairingSpot[rand_four] == 'SE':
                    self.seSlot.addAnimal("mouse")
                    self.MouseNumber += 1
                    self.allMices.append(Mouse(self.seSlot.cordI, self.seSlot.cordJ, 'x'))
                if possiblePairingSpot[rand_four] == 'S':
                    self.sSlot.addAnimal("mouse")
                    self.MouseNumber += 1
                    self.allMices.append(Mouse(self.sSlot.cordI, self.sSlot.cordJ, 'x'))
                if possiblePairingSpot[rand_four] == 'SW':
                    self.swSlot.addAnimal("mouse")
                    self.MouseNumber += 1
                    self.allMices.append(Mouse(self.swSlot.cordI, self.swSlot.cordJ, 'x'))
                if possiblePairingSpot[rand_four] == 'W':
                    self.wSlot.addAnimal("mouse")
                    self.MouseNumber += 1
                    self.allMices.append(Mouse(self.wSlot.cordI, self.wSlot.cordJ, 'x'))
                if possiblePairingSpot[rand_four] == 'NW':
                    self.nwSlot.addAnimal("mouse")
                    self.MouseNumber += 1
                    self.allMices.append(Mouse(self.nwSlot.cordI, self.nwSlot.cordJ, 'x'))

    #Reger for hvordan musene bevaeger sig, bruger neighbors
    def mouseMoveRules(self, currentSlot, currentSlotI, currentSlotJ):
        rand_one = random.randrange(0,2)
        possibleDirections = []
        stoneSpots = []
        self.owlAndHide = False

        self.movedN = False
        self.movedNE = False
        self.movedE = False
        self.movedSE = False
        self.movedS = False
        self.movedSW = False
        self.movedW = False
        self.movedNW = False

        if currentSlot.has_rock == True and currentSlot.hideUnderRock == False:
            stoneSpots.append('Current')

        for key in self.moveMouseDic:
            if self.moveMouseDic[key]['numOwels'] == 0 and self.moveMouseDic[key]['numMice'] < 2:
                possibleDirections.append(key)
            if self.moveMouseDic[key]['hasRock'] == True and self.moveMouseDic[key]['numMice'] < 2 and self.moveMouseDic[key]['underRock'] == False:
                stoneSpots.append(key)
            if self.moveMouseDic[key]['numOwels'] == 1 and len(stoneSpots) > 0:
                self.owlAndHide = True
            else:
                pass

        if len(possibleDirections) > 0:
            if self.owlAndHide == True:
                rand_two = random.randrange(len(stoneSpots))
                self.stoneDirections = rand_two

                if self.stoneDirections  == 'N':
                    self.nSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")

                    self.nSlot.hideUnderRock == True
                    self.movedN = True
                if self.stoneDirections  == 'NE':
                    self.neSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")

                    self.nSlot.hideUnderRock == True
                    self.movedNE = True
                if self.stoneDirections  == 'E':
                    self.eSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")

                    self.eSlot.hideUnderRock == True
                    self.movedE = True
                if self.stoneDirections == 'SE':
                    self.seSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")

                    self.seSlot.hideUnderRock == True
                    self.movedSE = True
                if self.stoneDirections == 'S':
                    self.sSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")

                    self.sSlot.hideUnderRock == True
                    self.movedS = True
                if self.stoneDirections == 'SW':
                    self.swSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")

                    self.swSlot.hideUnderRock == True
                    self.movedSW = True
                if self.stoneDirections == 'W':
                    self.wSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")

                    self.wSlot.hideUnderRock == True
                    self.movedW = True
                if self.stoneDirections == 'NW':
                    self.nwSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")

                    self.nwSlot.hideUnderRock == True
                    self.movedNW = True

            else:
                rand_three = random.randrange(len(possibleDirections))
                self.movingSlot = possibleDirections[rand_three]

                if self.movingSlot == 'N':
                    self.nSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")
                    self.movedN = True
                if self.movingSlot == 'NE':
                    self.neSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")
                    self.movedNE = True
                if self.movingSlot == 'E':
                    self.eSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")
                    self.movedE = True
                if self.movingSlot == 'SE':
                    self.seSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")
                    self.movedSE = True
                if self.movingSlot == 'S':
                    self.sSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")
                    self.movedS = True
                if self.movingSlot == 'SW':
                    self.swSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")
                    self.movedSW = True
                if self.movingSlot == 'W':
                    self.wSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")
                    self.movedW = True
                if self.movingSlot == 'NW':
                    self.nwSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")
                    self.movedNW = True
