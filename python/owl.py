from mouse import Mouse
import random

class Owl(Mouse):

    def __init__(self):
        Mouse.__init__(self, 0, 0, 0)
        self.mouseEaten = False

    #Draeber en mus hvis der er en mus og en ugle paa samme felt
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

    #Regler for hvordan uglerne bevaeger sig bruger ogsaa neighbors bare med dobbelt saa stor synsradius
    def owlMoveRules(self, currentSlot):
        rand_one = random.randrange(0,2)
        possibleDirections = []
        priorityDirections = []
        stoneSpots = []

        for key in self.moveMouseDic:
            if self.moveMouseDic[key]['numOwels'] == 0:
                possibleDirections.append(key)
            if self.moveMouseDic[key]['numOwels'] == 0 and self.moveMouseDic[key]['numMice'] == 1 and self.moveMouseDic[key]['underRock'] == False:
                priorityDirections.append(key)
            elif self.moveMouseDic[key]['numOwels'] == 0 and self.moveMouseDic[key]['numMice'] == 2:
                priorityDirections.append(key)

        for key in self.moveOwlDic:
            if self.moveOwlDic[key]['numOwels'] == 0 and self.moveOwlDic[key]['hasRock'] == False or self.moveOwlDic[key]['numMice'] < 2:
                if key == 'NN' and self.moveMouseDic['N']['numOwels'] == 0:
                    if self.moveMouseDic['N']['hasRock'] == False or self.moveMouseDic['N']['numMice'] < 2:
                        possibleDirections.append('N')
                if key == 'NNE' and self.moveMouseDic['NE']['numOwels'] == 0:
                    if self.moveMouseDic['NE']['hasRock'] == False or self.moveMouseDic['NE']['numMice'] < 2:
                        possibleDirections.append('NE')
                if key == 'NNEE' and self.moveMouseDic['NE']['numOwels'] == 0:
                    if self.moveMouseDic['NE']['hasRock'] == False or self.moveMouseDic['NE']['numMice'] < 2:
                        possibleDirections.append('NE')
                if key == 'NEE' and self.moveMouseDic['NE']['numOwels'] == 0:
                    if self.moveMouseDic['NE']['hasRock'] == False or self.moveMouseDic['NE']['numMice'] < 2:
                        possibleDirections.append('NE')
                if key == 'EE' and self.moveMouseDic['E']['numOwels'] == 0:
                    if self.moveMouseDic['E']['hasRock'] == False or self.moveMouseDic['E']['numMice'] < 2:
                        possibleDirections.append('E')
                if key == 'SEE' and self.moveMouseDic['SE']['numOwels'] == 0:
                    if self.moveMouseDic['SE']['hasRock'] == False or self.moveMouseDic['SE']['numMice'] < 2:
                        possibleDirections.append('SE')
                if key == 'SSEE' and self.moveMouseDic['SE']['numOwels'] == 0:
                    if self.moveMouseDic['SE']['hasRock'] == False or self.moveMouseDic['SE']['numMice'] < 2:
                        possibleDirections.append('SE')
                if key == 'SSE' and self.moveMouseDic['SE']['numOwels'] == 0:
                    if self.moveMouseDic['SE']['hasRock'] == False or self.moveMouseDic['SE']['numMice'] < 2:
                        possibleDirections.append('SE')
                if key == 'SS' and self.moveMouseDic['S']['numOwels'] == 0:
                    if self.moveMouseDic['S']['hasRock'] == False or self.moveMouseDic['S']['numMice'] < 2:
                        possibleDirections.append('S')
                if key == 'SSW' and self.moveMouseDic['SW']['numOwels'] == 0:
                    if self.moveMouseDic['SW']['hasRock'] == False or self.moveMouseDic['SW']['numMice'] < 2:
                        possibleDirections.append('SW')
                if key == 'SSWW' and self.moveMouseDic['SW']['numOwels'] == 0:
                    if self.moveMouseDic['SW']['hasRock'] == False or self.moveMouseDic['SW']['numMice'] < 2:
                        possibleDirections.append('SW')
                if key == 'SWW' and self.moveMouseDic['SW']['numOwels'] == 0:
                    if self.moveMouseDic['SW']['hasRock'] == False or self.moveMouseDic['S']['numMice'] < 2:
                        possibleDirections.append('SW')
                if key == 'WW' and self.moveMouseDic['W']['numOwels'] == 0:
                    if self.moveMouseDic['W']['hasRock'] == False or self.moveMouseDic['W']['numMice'] < 2:
                        possibleDirections.append('W')
                if key == 'NWW' and self.moveMouseDic['NW']['numOwels'] == 0:
                    if self.moveMouseDic['NW']['hasRock'] == False or self.moveMouseDic['NW']['numMice'] < 2:
                        possibleDirections.append('NW')
                if key == 'NNWW' and self.moveMouseDic['NW']['numOwels'] == 0:
                    if self.moveMouseDic['NW']['hasRock'] == False or self.moveMouseDic['NW']['numMice'] < 2:
                        possibleDirections.append('NW')
                if key == 'NNW' and self.moveMouseDic['NW']['numOwels'] == 0:
                    if self.moveMouseDic['NW']['hasRock'] == False or self.moveMouseDic['NW']['numMice'] < 2:
                        possibleDirections.append('NW')

            if self.moveOwlDic[key]['numOwels'] == 0 and self.moveOwlDic[key]['numMice'] == 1 and self.moveOwlDic[key]['underRock'] == False:
                if key == 'NN' and self.moveMouseDic['N']['numOwels'] == 0:
                    if self.moveMouseDic['N']['hasRock'] == False or self.moveMouseDic['N']['numMice'] < 2:
                        priorityDirections.append('N')
                if key == 'NNE' and self.moveMouseDic['NE']['numOwels'] == 0:
                    if self.moveMouseDic['NE']['hasRock'] == False or self.moveMouseDic['NE']['numMice'] < 2:
                        priorityDirections.append('NE')
                if key == 'NNEE' and self.moveMouseDic['NE']['numOwels'] == 0:
                    if self.moveMouseDic['NE']['hasRock'] == False or self.moveMouseDic['NE']['numMice'] < 2:
                        priorityDirections.append('NE')
                if key == 'NEE' and self.moveMouseDic['NE']['numOwels'] == 0:
                    if self.moveMouseDic['NE']['hasRock'] == False or self.moveMouseDic['NE']['numMice'] < 2:
                        priorityDirections.append('NE')
                if key == 'EE' and self.moveMouseDic['E']['numOwels'] == 0:
                    if self.moveMouseDic['E']['hasRock'] == False or self.moveMouseDic['E']['numMice'] < 2:
                        priorityDirections.append('E')
                if key == 'SEE' and self.moveMouseDic['SE']['numOwels'] == 0:
                    if self.moveMouseDic['SE']['hasRock'] == False or self.moveMouseDic['SE']['numMice'] < 2:
                        priorityDirections.append('SE')
                if key == 'SSEE' and self.moveMouseDic['SE']['numOwels'] == 0:
                    if self.moveMouseDic['SE']['hasRock'] == False or self.moveMouseDic['SE']['numMice'] < 2:
                        priorityDirections.append('SE')
                if key == 'SSE' and self.moveMouseDic['SE']['numOwels'] == 0:
                    if self.moveMouseDic['SE']['hasRock'] == False or self.moveMouseDic['SE']['numMice'] < 2:
                        priorityDirections.append('SE')
                if key == 'SS' and self.moveMouseDic['S']['numOwels'] == 0:
                    if self.moveMouseDic['S']['hasRock'] == False or self.moveMouseDic['S']['numMice'] < 2:
                        priorityDirections.append('S')
                if key == 'SSW' and self.moveMouseDic['SW']['numOwels'] == 0:
                    if self.moveMouseDic['SW']['hasRock'] == False or self.moveMouseDic['SW']['numMice'] < 2:
                        priorityDirections.append('SW')
                if key == 'SSWW' and self.moveMouseDic['SW']['numOwels'] == 0:
                    if self.moveMouseDic['SW']['hasRock'] == False or self.moveMouseDic['SW']['numMice'] < 2:
                        priorityDirections.append('SW')
                if key == 'SWW' and self.moveMouseDic['SW']['numOwels'] == 0:
                    if self.moveMouseDic['SW']['hasRock'] == False or self.moveMouseDic['S']['numMice'] < 2:
                        priorityDirections.append('SW')
                if key == 'WW' and self.moveMouseDic['W']['numOwels'] == 0:
                    if self.moveMouseDic['W']['hasRock'] == False or self.moveMouseDic['W']['numMice'] < 2:
                        priorityDirections.append('W')
                if key == 'NWW' and self.moveMouseDic['NW']['numOwels'] == 0:
                    if self.moveMouseDic['NW']['hasRock'] == False or self.moveMouseDic['NW']['numMice'] < 2:
                        priorityDirections.append('NW')
                if key == 'NNWW' and self.moveMouseDic['NW']['numOwels'] == 0:
                    if self.moveMouseDic['NW']['hasRock'] == False or self.moveMouseDic['NW']['numMice'] < 2:
                        priorityDirections.append('NW')
                if key == 'NNW' and self.moveMouseDic['NW']['numOwels'] == 0:
                    if self.moveMouseDic['NW']['hasRock'] == False or self.moveMouseDic['NW']['numMice'] < 2:
                        priorityDirections.append('NW')
            elif self.moveOwlDic[key]['numOwels'] == 0 and self.moveOwlDic[key]['numMice'] == 2:
                if key == 'NN' and self.moveMouseDic['N']['numOwels'] == 0:
                    if self.moveMouseDic['N']['hasRock'] == False or self.moveMouseDic['N']['numMice'] < 2:
                        priorityDirections.append('N')
                if key == 'NNE' and self.moveMouseDic['NE']['numOwels'] == 0:
                    if self.moveMouseDic['NE']['hasRock'] == False or self.moveMouseDic['NE']['numMice'] < 2:
                        priorityDirections.append('NE')
                if key == 'NNEE' and self.moveMouseDic['NE']['numOwels'] == 0:
                    if self.moveMouseDic['NE']['hasRock'] == False or self.moveMouseDic['NE']['numMice'] < 2:
                        priorityDirections.append('NE')
                if key == 'NEE' and self.moveMouseDic['NE']['numOwels'] == 0:
                    if self.moveMouseDic['NE']['hasRock'] == False or self.moveMouseDic['NE']['numMice'] < 2:
                        priorityDirections.append('NE')
                if key == 'EE' and self.moveMouseDic['E']['numOwels'] == 0:
                    if self.moveMouseDic['E']['hasRock'] == False or self.moveMouseDic['E']['numMice'] < 2:
                        priorityDirections.append('E')
                if key == 'SEE' and self.moveMouseDic['SE']['numOwels'] == 0:
                    if self.moveMouseDic['SE']['hasRock'] == False or self.moveMouseDic['SE']['numMice'] < 2:
                        priorityDirections.append('SE')
                if key == 'SSEE' and self.moveMouseDic['SE']['numOwels'] == 0:
                    if self.moveMouseDic['SE']['hasRock'] == False or self.moveMouseDic['SE']['numMice'] < 2:
                        priorityDirections.append('SE')
                if key == 'SSE' and self.moveMouseDic['SE']['numOwels'] == 0:
                    if self.moveMouseDic['SE']['hasRock'] == False or self.moveMouseDic['SE']['numMice'] < 2:
                        priorityDirections.append('SE')
                if key == 'SS' and self.moveMouseDic['S']['numOwels'] == 0:
                    if self.moveMouseDic['S']['hasRock'] == False or self.moveMouseDic['S']['numMice'] < 2:
                        priorityDirections.append('S')
                if key == 'SSW' and self.moveMouseDic['SW']['numOwels'] == 0:
                    if self.moveMouseDic['SW']['hasRock'] == False or self.moveMouseDic['SW']['numMice'] < 2:
                        priorityDirections.append('SW')
                if key == 'SSWW' and self.moveMouseDic['SW']['numOwels'] == 0:
                    if self.moveMouseDic['SW']['hasRock'] == False or self.moveMouseDic['SW']['numMice'] < 2:
                        priorityDirections.append('SW')
                if key == 'SWW' and self.moveMouseDic['SW']['numOwels'] == 0:
                    if self.moveMouseDic['SW']['hasRock'] == False or self.moveMouseDic['S']['numMice'] < 2:
                        priorityDirections.append('SW')
                if key == 'WW' and self.moveMouseDic['W']['numOwels'] == 0:
                    if self.moveMouseDic['W']['hasRock'] == False or self.moveMouseDic['W']['numMice'] < 2:
                        priorityDirections.append('W')
                if key == 'NWW' and self.moveMouseDic['NW']['numOwels'] == 0:
                    if self.moveMouseDic['NW']['hasRock'] == False or self.moveMouseDic['NW']['numMice'] < 2:
                        priorityDirections.append('NW')
                if key == 'NNWW' and self.moveMouseDic['NW']['numOwels'] == 0:
                    if self.moveMouseDic['NW']['hasRock'] == False or self.moveMouseDic['NW']['numMice'] < 2:
                        priorityDirections.append('NW')
                if key == 'NNW' and self.moveMouseDic['NW']['numOwels'] == 0:
                    if self.moveMouseDic['NW']['hasRock'] == False or self.moveMouseDic['NW']['numMice'] < 2:
                        priorityDirections.append('NW')

        if len(priorityDirections) > 0:
            rand_two = random.randrange(len(priorityDirections))
            self.movingSlot = priorityDirections[rand_two]

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
        else:
            rand_three = random.randrange(len(possibleDirections))
            self.movingSlot = possibleDirections[rand_three]

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
