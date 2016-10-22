#pygame

import random

from grid import Grid

class Mouse(Grid):

    def __init__(self):
        Grid.__init__(self)
        self.mouse_steps = 20
        self.dead = True

        #Walls

        self.westWall = False
        self.northWall = False
        self.eastWall = False
        self.southWall = False

        possibleDirections = []



    #Steps 20 steps = dead
    def dead(self):
        if steps == 20:
            return self.mouse_dead == True

    #Move regler for mouse, bruger neighbors like self.moveMouseDic['numMice']

    def mouseMoveRules(self, currentSlot, currentSlotI, currentSlotJ):
        self.westWall = False
        self.northWall = False
        self.eastWall = False
        self.southWall = False


        rand_one = random.randrange(0,2)
        possiblePairingSpot = []
        possibleDirections = []
        stoneSpots = []
        owlAndHide = False
        cmon = False
        # if(self.dead()):
        #     currentSlot.rmAnimal("mouse")
        #     print "A MOUSE HAS DIED"
        # else:
        # if rand_one == 1:

        #Check if there is any wall
        # if currentSlotI == 0:
        #     self.westWall = True
        #     return self.westWall
        #
        # if currentSlotJ == 0:
        #     self.northWall = True
        #     return self.northWall
        #
        # if currentSlotI == 19:
        #     self.eastWall = True
        #     return self.eastWall
        #
        # if currentSlotJ == 19:
        #     self.southWall = True
        #     return self.southWall

        if self.moveMouseDic['N']['numMice'] < 2:
            possibleDirections.append('N')
        if self.moveMouseDic['NE']['numMice'] < 2:
            possibleDirections.append('NE')
        if self.moveMouseDic['E']['numMice'] < 2:
            possibleDirections.append('E')
        if self.moveMouseDic['SE']['numMice'] < 2:
            possibleDirections.append('SE')
        if self.moveMouseDic['S']['numMice'] < 2:
            possibleDirections.append('S')
        if self.moveMouseDic['SW']['numMice'] < 2:
            possibleDirections.append('SW')
        if self.moveMouseDic['W']['numMice'] < 2:
            possibleDirections.append('W')
        if self.moveMouseDic['NW']['numMice'] < 2:
            possibleDirections.append('NW')


        #If there is any wall to any side remove that side from possibleDirections

        # if self.westWall == True and self.northWall == True:
        #     if 'W' in possibleDirections:
        #         possibleDirections.remove('W')
        #     if 'NW' in possibleDirections:
        #         possibleDirections.remove('NW')
        #     if 'SW' in possibleDirections:
        #         possibleDirections.remove('SW')
        #     if 'N' in possibleDirections:
        #         possibleDirections.remove('N')
        #     if 'NE' in possibleDirections:
        #         possibleDirections.remove('NE')
        #
        # if self.westWall == True and self.southWall == True:
        #     if 'W' in possibleDirections:
        #         possibleDirections.remove('W')
        #     if 'NW' in possibleDirections:
        #         possibleDirections.remove('NW')
        #     if 'SW' in possibleDirections:
        #         possibleDirections.remove('SW')
        #     if 'N' in possibleDirections:
        #         possibleDirections.remove('N')
        #     if 'NE' in possibleDirections:
        #         possibleDirections.remove('NE')
        #
        # if self.northWall == True and self.eastWall == True:
        #     if 'N' in possibleDirections:
        #         possibleDirections.remove('N')
        #     if 'NW' in possibleDirections:
        #         possibleDirections.remove('NW')
        #     if 'E' in possibleDirections:
        #         possibleDirections.remove('E')
        #     if 'SE' in possibleDirections:
        #         possibleDirections.remove('SE')
        #     if 'NE' in possibleDirections:
        #         possibleDirections.remove('NE')
        #
        # if self.eastWall == True and self.southWall == True:
        #     if 'N' in possibleDirections:
        #         possibleDirections.remove('N')
        #     if 'NW' in possibleDirections:
        #         possibleDirections.remove('NW')
        #     if 'E' in possibleDirections:
        #         possibleDirections.remove('E')
        #     if 'SE' in possibleDirections:
        #         possibleDirections.remove('SE')
        #     if 'NE' in possibleDirections:
        #         possibleDirections.remove('NE')
        #
        # elif self.eastWall == True:
        #     if 'N' in possibleDirections:
        #         possibleDirections.remove('N')
        #     if 'NW' in possibleDirections:
        #         possibleDirections.remove('NW')
        #     if 'E' in possibleDirections:
        #         possibleDirections.remove('E')
        #
        # elif self.southWall == True:
        #     if 'E' in possibleDirections:
        #         possibleDirections.remove('E')
        #     if 'SE' in possibleDirections:
        #         possibleDirections.remove('SE')
        #     if 'SW' in possibleDirections:
        #         possibleDirections.remove('SW')
        # if self.northWall == True:
        #     if 'N' in possibleDirections:
        #         possibleDirections.remove('N')
        #     if 'NW' in possibleDirections:
        #         possibleDirections.remove('NW')
        #     if 'NE' in possibleDirections:
        #         possibleDirections.remove('NE')





        # for key in self.moveMouseDic:
        #     if self.moveMouseDic[key]['numOwels'] == 0 and self.moveMouseDic[key]['numMice'] < 2:
        #         possibleDirections.append(key)
        #         # print('succes')
        #     if self.moveMouseDic[key]['hasRock'] == True:
        #         stoneSpots.append(self.moveMouseDic[key])
        #     if self.moveMouseDic[key]['numOwels'] == 1 and len(stoneSpots) > 0:
        #         owlAndHide = True
        #         return owlAndHide
        #     if len(possibleDirections) == 0 and self.northWall == False:
        #         possibleDirections.append(self.moveMouseDic['N'])
        #     if len(possibleDirections) == 0 and self.southWall == False:
        #         possibleDirections.append(self.moveMouseDic['S'])
        #     if len(possibleDirections) == 0 and self.eastWall == False:
        #         possibleDirections.append(self.moveMouseDic['E'])
        #     if len(possibleDirections) == 0 and self.westWall == False:
        #         possibleDirections.append(self.moveMouseDic['W'])
        #     else:
        #         pass

        print (possibleDirections)

        if len(possibleDirections) > 0:


            if owlAndHide == True:
                rand_two = random.randrange(len(stoneSpots))
                currentSlot.rmAnimal("mouse")
                stoneSpots[rand_two].addAnimal("mouse")
            else:
                rand_three = random.randrange(len(possibleDirections))
                self.movingSlot = possibleDirections[rand_three]
                if self.movingSlot == 'N':
                    self.nSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")

                elif self.movingSlot == 'NE':

                    self.neSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")

                elif self.movingSlot == 'E':

                    self.eSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")

                elif self.movingSlot == 'SE':

                    self.seSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")

                elif self.movingSlot == 'S':

                    self.sSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")

                elif self.movingSlot == 'SW':

                    self.swSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")

                elif self.movingSlot == 'W':

                    self.wSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")

                elif self.movingSlot == 'NW':
                    self.nwSlot.addAnimal("mouse")
                    currentSlot.rmAnimal("mouse")
                else:
                    'IT DOESN*T WORK'

        else:
            'NONE OF them moved'


        #Possible pairing spots skal lave denne her om ligesom den ovenovre

        # if currentSlot.num_mice == 2:
        #     for key in self.moveMouseDic:
        #         if self.moveMouseDic[key]['allAnimals'] == 0:
        #             possiblePairingSpot.append(key)
        #             rand_four = random.randrange(len(possiblePairingSpot))
        #             return rand_four
        #
        #     # 10% chance for at en ny mus spawner paa et ledigt felt
        #         if rand_five == 9:
        #             if possiblePairingSpot[rand_four] == 'N':
        #                 currentSlot.rmAnimal("mouse")
        #                 self.directions['N'].addAnimal("mouse")
        #
        #             if possiblePairingSpot[rand_four] == 'NE':
        #                 currentSlot.rmAnimal("mouse")
        #                 self.directions['NE'].addAnimal("mouse")
        #
        #             if possiblePairingSpot[rand_four] == 'E':
        #                 currentSlot.rmAnimal("mouse")
        #                 self.directions['E'].addAnimal("mouse")
        #
        #             if possiblePairingSpot[rand_four] == 'SE':
        #                 currentSlot.rmAnimal("mouse")
        #                 self.directions['SE'].addAnimal("mouse")
        #
        #             if possiblePairingSpot[rand_four] == 'S':
        #                 currentSlot.rmAnimal("mouse")
        #                 self.directions['S'].addAnimal("mouse")
        #
        #             if possiblePairingSpot[rand_four] == 'SW':
        #                 currentSlot.rmAnimal("mouse")
        #                 self.directions['SW'].addAnimal("mouse")
        #
        #             if possiblePairingSpot[rand_four] == 'W':
        #                 currentSlot.rmAnimal("mouse")
        #                 self.directions['W'].addAnimal("mouse")
        #
        #         if possiblePairingSpot[rand_four] == 'NW':
        #             currentSlot.rmAnimal("mouse")
        #             self.directions['NW'].addAnimal("mouse")
