#pygamec

import random
from gg import GG


class Mouse(GG):

    def __init__(self, x, y, stringAttribute):
        GG.__init__(self)
        self.mouse_steps = 0
        self.dead = False

        self.x = x
        self.y = y


    #Steps 20 steps = dead
    def checkIfDead(self):
        if self.mouse_steps == 20:
            return True



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
                # self.addNewMouseToList()
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


        for key in self.moveMouseDic:
            if self.moveMouseDic[key]['numOwels'] == 0 and self.moveMouseDic[key]['numMice'] < 2:
                possibleDirections.append(key)
            if self.moveMouseDic[key]['hasRock'] == True:
                stoneSpots.append(key)
            if self.moveMouseDic[key]['numOwels'] == 1 and len(stoneSpots) > 0:
                self.owlAndHide = True
            else:
                pass

        if len(possibleDirections) > 0:
            if self.owlAndHide == True:
                print 'wuhuuu owl and hide = true'
                rand_two = random.randrange(len(stoneSpots))
                self.stoneDirections = rand_two

                if self.stoneDirections  == 'N':
                    self.nSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")
                    # self.x = self.nSlot.cordI
                    # self.y = self.nSlot.cordJ
                    # return self.x
                    # return self.y
                    self.movedN = True
                if self.stoneDirections  == 'NE':
                    self.neSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")
                    # self.x = self.neSlot.cordI
                    # self.y = self.neSlot.cordJ
                    # return self.x
                    # return self.y
                    self.movedNE = True
                if self.stoneDirections  == 'E':
                    self.eSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")
                    # self.x = self.eSlot.cordI
                    # self.y = self.eSlot.cordJ
                    # return self.x
                    # return self.y
                    self.movedE = True
                if self.stoneDirections == 'SE':
                    self.seSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")
                    # self.x = self.seSlot.cordI
                    # self.y = self.seSlot.cordJ
                    # return self.x
                    # return self.y
                    self.movedSE = True
                if self.stoneDirections == 'S':
                    self.sSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")
                    # self.x = self.sSlot.cordI
                    # self.y = self.sSlot.cordJ
                    # return self.x
                    # return self.y
                    self.movedS = True
                if self.stoneDirections == 'SW':
                    self.swSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")
                    # self.x = self.swSlot.cordI
                    # self.y = self.swSlot.cordJ
                    # return self.x
                    # return self.y
                    self.movedSW = True
                if self.stoneDirections == 'W':
                    self.wSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")
                    # self.x = self.wSlot.cordI
                    # self.y = self.wSlot.cordJ
                    # return self.x
                    # return self.y
                    self.movedW = True
                if self.stoneDirections == 'NW':
                    self.nwSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")
                    # self.x = self.nwSlot.cordI
                    # self.y = self.nwSlot.cordJ
                    # return self.x
                    # return self.y
                    self.movedNW = True

            else:
                rand_three = random.randrange(len(possibleDirections))
                self.movingSlot = possibleDirections[rand_three]

                if self.movingSlot == 'N':
                    self.nSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")
                    # self.x = self.nSlot.cordI
                    # self.y = self.nSlot.cordJ
                    # return self.x
                    # return self.y
                    self.movedN = True
                if self.movingSlot == 'NE':
                    self.neSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")
                    # self.x = self.neSlot.cordI
                    # self.y = self.neSlot.cordJ
                    # return self.x
                    # return self.y
                    self.movedNE = True
                if self.movingSlot == 'E':
                    self.eSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")
                    # self.x = self.eSlot.cordI
                    # self.y = self.eSlot.cordJ
                    # return self.x
                    # return self.y
                    self.movedE = True
                if self.movingSlot == 'SE':
                    self.seSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")
                    # self.x = self.seSlot.cordI
                    # self.y = self.seSlot.cordJ
                    # return self.x
                    # return self.y
                    self.movedSE = True
                if self.movingSlot == 'S':
                    self.sSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")
                    # self.x = self.sSlot.cordI
                    # self.y = self.sSlot.cordJ
                    # return self.x
                    # return self.y
                    self.movedS = True
                if self.movingSlot == 'SW':
                    self.swSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")
                    # self.x = self.swSlot.cordI
                    # self.y = self.swSlot.cordJ
                    # return self.x
                    # return self.y
                    self.movedSW = True
                if self.movingSlot == 'W':
                    self.wSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")
                    # self.x = self.wSlot.cordI
                    # self.y = self.wSlot.cordJ
                    # return self.x
                    # return self.y
                    self.movedW = True
                if self.movingSlot == 'NW':
                    self.nwSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")
                    # self.x = self.nwSlot.cordI
                    # self.y = self.nwSlot.cordJ
                    # return self.x
                    # return self.y
                    self.movedNW = True
