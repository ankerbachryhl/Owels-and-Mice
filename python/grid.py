
from slot import Slot

class Grid(object):

    #Laver griddet
    def __init__(self):
        self.grid = [[0 for x in range(0, 22)] for x in range(0, 22)]
        self.createSlot()
        self.moveMouseDic = {}
        self.moveOwlDic = {}

    #Laver en slot i hver plads i griddet
    def createSlot(self):
        for i in range(0, 22):
            for j in range(0, 22):
                self.grid[i][j] = Slot(i, j)


    #Bruges til at forhindre at de stepper uden for murene
    def checkValuesI(self, i):
        self.gg = False
        if i < 1:
            i += 1
            return i
            self.gg = True
            return self.gg
        elif i > 20:
            i -= 1
            return i
            self.gg = True
            return self.gg
        else:
            return i
    def checkValuesJ(self, j):
        self.gg = False
        if j < 1:
            j += 1
            return j
            self.gg = True
            return self.gg
        elif j > 20:
            j -= 1
            return j
            self.gg = True
            return self.gg
        else:
            return j

    def checkOwlValuesI(self, i):
        if i < 2:
            i += 2
            return i
        elif i > 19:
            i -= 2
            return i
        else:
            return i
    def checkOwlValuesJ(self, j):
        if j < 2:
            j += 2
            return j
        elif j > 19:
            j -= 2
            return j
        else:
            return j


    #Returnere alle musenes naboere og uglernes naboere
    def getNeighbors(self, currentSlot, currentSlotI, currentSlotJ):

        #North
        if self.grid[self.checkValuesI(currentSlotI)][self.checkValuesJ(currentSlotJ - 1)].cordJ < 1:
            self.nSlot = currentSlot
        else:
            self.nSlot = self.grid[currentSlotI][currentSlotJ - 1]

        #North East
        if self.grid[self.checkValuesI(currentSlotI + 1)][self.checkValuesJ(currentSlotJ - 1)].cordI > 19:
            self.neSlot = currentSlot
        elif self.grid[self.checkValuesI(currentSlotI + 1)][self.checkValuesJ(currentSlotJ - 1)].cordJ < 1:
            self.neSlot = currentSlot
        else:
            self.neSlot = self.grid[currentSlotI + 1][currentSlotJ - 1]

        #North West
        if self.grid[self.checkValuesI(currentSlotI - 1)][self.checkValuesJ(currentSlotJ - 1)].cordI < 1:
            self.nwSlot = currentSlot
        elif self.grid[self.checkValuesI(currentSlotI - 1)][self.checkValuesJ(currentSlotJ - 1)].cordJ < 1:
            self.nwSlot = currentSlot
        else:
            self.nwSlot = self.grid[currentSlotI - 1][currentSlotJ - 1]

        #E
        if self.grid[self.checkValuesI(currentSlotI + 1)][self.checkValuesJ(currentSlotJ)].cordI > 19:
            self.eSlot = currentSlot
        else:
            self.eSlot = self.grid[currentSlotI + 1][currentSlotJ]

        #SE
        if self.grid[self.checkValuesI(currentSlotI + 1)][self.checkValuesJ(currentSlotJ + 1)].cordJ > 19:
            self.seSlot = currentSlot
        elif self.grid[self.checkValuesI(currentSlotI + 1)][self.checkValuesJ(currentSlotJ + 1)].cordI > 19:
            self.seSlot = currentSlot
        else:
            self.seSlot = self.grid[currentSlotI + 1][currentSlotJ + 1]

        #South
        if self.grid[self.checkValuesI(currentSlotI)][self.checkValuesJ(currentSlotJ + 1)].cordJ > 19:
            self.sSlot = currentSlot
        else:
            self.sSlot = self.grid[currentSlotI][currentSlotJ + 1]

        #South West
        if self.grid[self.checkValuesI(currentSlotI - 1)][self.checkValuesJ(currentSlotJ + 1)].cordJ > 19:
            self.swSlot = currentSlot
        elif self.grid[self.checkValuesI(currentSlotI - 1)][self.checkValuesJ(currentSlotJ + 1)].cordI < 1:
            self.swSlot = currentSlot
        else:
            self.swSlot = self.grid[currentSlotI - 1][currentSlotJ + 1]

        #West
        if self.grid[self.checkValuesI(currentSlotI - 1)][self.checkValuesJ(currentSlotJ)].cordI < 1:
            self.wSlot = currentSlot
        else:
            self.wSlot = self.grid[currentSlotI - 1][currentSlotJ]

        #Muse naboer dict

        self.moveMouseDic = {'N'    :   self.nSlot.dicSlot(),   'NE'    :   self.neSlot.dicSlot(),  'E' :   self.eSlot.dicSlot(),   'NW'    :   self.nwSlot.dicSlot(),  'SE'    :   self.seSlot.dicSlot(),  'S' :   self.sSlot.dicSlot(),   'SW'    :   self.swSlot.dicSlot(),  'W' :  self.wSlot.dicSlot()}

        #Ugle naboere (dobbelt saa stor synsradius)

        #North
        if self.grid[self.checkOwlValuesI(currentSlotI)][self.checkOwlValuesJ(currentSlotJ - 2)].cordJ < 2:
            self.nnSlot = currentSlot
        else:
            self.nnSlot = self.grid[currentSlotI][currentSlotJ - 2]

        #North East
        if self.grid[self.checkOwlValuesI(currentSlotI + 1)][self.checkOwlValuesJ(currentSlotJ - 2)].cordI > 18:
            self.nneSlot = currentSlot
        elif self.grid[self.checkOwlValuesI(currentSlotI + 1)][self.checkOwlValuesJ(currentSlotJ - 1)].cordJ < 2:
            self.nneSlot = currentSlot
        else:
            self.nneSlot = self.grid[currentSlotI + 1][currentSlotJ - 2]

        if self.grid[self.checkOwlValuesI(currentSlotI + 2)][self.checkOwlValuesJ(currentSlotJ - 2)].cordI > 18:
            self.nneeSlot = currentSlot
        elif self.grid[self.checkOwlValuesI(currentSlotI + 2)][self.checkOwlValuesJ(currentSlotJ - 2)].cordJ < 2:
            self.nneeSlot = currentSlot
        else:
            self.nneeSlot = self.grid[currentSlotI + 2][currentSlotJ - 2]

        if self.grid[self.checkOwlValuesI(currentSlotI + 2)][self.checkOwlValuesJ(currentSlotJ - 1)].cordI > 18:
            self.neeSlot = currentSlot
        elif self.grid[self.checkOwlValuesI(currentSlotI + 2)][self.checkOwlValuesJ(currentSlotJ - 1)].cordJ < 2:
            self.neeSlot = currentSlot
        else:
            self.neeSlot = self.grid[currentSlotI + 2][currentSlotJ - 1]

        #East
        if self.grid[self.checkOwlValuesI(currentSlotI)][self.checkOwlValuesJ(currentSlotJ + 2)].cordI > 18:
            self.eeSlot = currentSlot
        else:
            self.eeSlot = self.grid[currentSlotI][currentSlotJ + 2]

        #South East
        if self.grid[self.checkOwlValuesI(currentSlotI + 2)][self.checkOwlValuesJ(currentSlotJ + 1)].cordJ > 18:
            self.seeSlot = currentSlot
        elif self.grid[self.checkOwlValuesI(currentSlotI + 2)][self.checkOwlValuesJ(currentSlotJ + 1)].cordI > 18:
            self.seeSlot = currentSlot
        else:
            self.seeSlot = self.grid[currentSlotI + 2][currentSlotJ + 1]

        if self.grid[self.checkValuesI(currentSlotI + 2)][self.checkValuesJ(currentSlotJ + 2)].cordJ > 18:
            self.sseeSlot = currentSlot
        elif self.grid[self.checkValuesI(currentSlotI + 2)][self.checkValuesJ(currentSlotJ + 2)].cordI > 18:
            self.sseeSlot = currentSlot
        else:
            self.sseeSlot = self.grid[currentSlotI + 2][currentSlotJ + 2]

        if self.grid[self.checkValuesI(currentSlotI + 1)][self.checkValuesJ(currentSlotJ + 2)].cordJ > 18:
            self.sseSlot = currentSlot
        elif self.grid[self.checkValuesI(currentSlotI + 1)][self.checkValuesJ(currentSlotJ + 2)].cordI > 18:
            self.sseSlot = currentSlot
        else:
            self.sseSlot = self.grid[currentSlotI + 1][currentSlotJ + 2]

        #South
        if self.grid[self.checkOwlValuesI(currentSlotI)][self.checkOwlValuesJ(currentSlotJ + 2)].cordJ > 18:
            self.ssSlot = currentSlot
        else:
            self.ssSlot = self.grid[currentSlotI][currentSlotJ + 2]

        #South West
        if self.grid[self.checkOwlValuesI(currentSlotI - 1)][self.checkOwlValuesJ(currentSlotJ + 2)].cordJ > 18:
            self.sswSlot = currentSlot
        elif self.grid[self.checkOwlValuesI(currentSlotI - 1)][self.checkOwlValuesJ(currentSlotJ + 2)].cordI < 2:
            self.sswSlot = currentSlot
        else:
            self.sswSlot = self.grid[currentSlotI - 1][currentSlotJ + 2]

        if self.grid[self.checkOwlValuesI(currentSlotI - 2)][self.checkOwlValuesJ(currentSlotJ + 2)].cordJ > 18:
            self.sswwSlot = currentSlot
        elif self.grid[self.checkOwlValuesI(currentSlotI - 2)][self.checkOwlValuesJ(currentSlotJ + 2)].cordI < 2:
            self.sswwSlot = currentSlot
        else:
            self.sswwSlot = self.grid[currentSlotI - 2][currentSlotJ + 2]

        if self.grid[self.checkOwlValuesI(currentSlotI - 2)][self.checkOwlValuesJ(currentSlotJ + 1)].cordJ > 18:
            self.swwSlot = currentSlot
        elif self.grid[self.checkOwlValuesI(currentSlotI - 2)][self.checkOwlValuesJ(currentSlotJ + 1)].cordI < 2:
            self.swwSlot = currentSlot
        else:
            self.swwSlot = self.grid[currentSlotI - 2][currentSlotJ + 1]

        #West
        if self.grid[self.checkOwlValuesI(currentSlotI - 2)][self.checkOwlValuesJ(currentSlotJ)].cordI < 2:
            self.wwSlot = currentSlot
        else:
            self.wwSlot = self.grid[currentSlotI - 2][currentSlotJ]

        #North West
        if self.grid[self.checkOwlValuesI(currentSlotI - 2)][self.checkOwlValuesJ(currentSlotJ - 1)].cordI < 2:
            self.nwwSlot = currentSlot
        elif self.grid[self.checkOwlValuesI(currentSlotI - 2)][self.checkOwlValuesJ(currentSlotJ - 1)].cordJ < 2:
            self.nwwSlot = currentSlot
        else:
            self.nwwSlot = self.grid[currentSlotI - 2][currentSlotJ - 1]

        if self.grid[self.checkOwlValuesI(currentSlotI - 2)][self.checkOwlValuesJ(currentSlotJ - 2)].cordI < 2:
            self.nnwwSlot = currentSlot
        elif self.grid[self.checkOwlValuesI(currentSlotI - 2)][self.checkOwlValuesJ(currentSlotJ - 2)].cordJ < 2:
            self.nnwwSlot = currentSlot
        else:
            self.nnwwSlot = self.grid[currentSlotI - 2][currentSlotJ - 2]

        if self.grid[self.checkOwlValuesI(currentSlotI - 1)][self.checkOwlValuesJ(currentSlotJ - 2)].cordI < 2:
            self.nnwSlot = currentSlot
        elif self.grid[self.checkOwlValuesI(currentSlotI - 1)][self.checkOwlValuesJ(currentSlotJ - 2)].cordJ < 2:
            self.nnwSlot = currentSlot
        else:
            self.nnwSlot = self.grid[currentSlotI - 1][currentSlotJ - 2]

        #Ugle synsradius dic

        self.moveOwlDic = {'NN' : self.nnSlot.dicSlot(), 'NNE' : self.nneSlot.dicSlot(), 'NNEE' : self.nneeSlot.dicSlot(), 'SSEE' : self.sseeSlot.dicSlot(), 'EE' : self.eeSlot.dicSlot(), 'SEE' : self.seeSlot.dicSlot(), 'SSEE' : self.sseeSlot.dicSlot(), 'SSE' : self.sseSlot.dicSlot(), 'SS' : self.ssSlot.dicSlot(), 'SSW' : self.sswSlot.dicSlot(), 'SSWW' : self.sswwSlot.dicSlot(), 'SWW' : self.swwSlot.dicSlot(), 'WW' : self.wwSlot.dicSlot(), 'NWW' : self.nwwSlot.dicSlot(), 'NNWW' : self.nnwwSlot.dicSlot(), 'NNW' : self.nnwSlot.dicSlot()}

        #Retunere alle muse retninger
        return self.moveMouseDic
        return self.nSlot
        return self.neSlot
        return self.eSlot
        return self.seSlot
        return self.sSlot
        return self.swSlot
        return self.wSlot
        return self.nwSlot

        #Retunere alle ugle retninger
        return self.moveOwlDic
        return self.nnSlot
        return self.nneSlot
        return self.nneeSlot
        return self.neeSlot
        return self.eeSlot
        return self.ssSlot
        return self.seeSlot
        return self.sseeSlot
        return self.sseSlot
        return self.sswSlot
        return self.sswwSlot
        return self.swwSlot
        return self.wwSlot
        return self.nwwSlot
        return self.nnwwSlot
        return self.nnwSlot



    # printer alle felter ud i terminalen
    def printSlots(self):
        for i in range(0, 20):
            print(self.grid[i][0].state),
        print("\n")
        for i in range(0, 20):
            print(self.grid[i][1].state),
        print("\n")
        for i in range(0, 20):
            print(self.grid[i][2].state),
        print("\n")
        for i in range(0, 20):
            print(self.grid[i][3].state),
        print("\n")
        for i in range(0, 20):
            print(self.grid[i][4].state),
        print("\n")
        for i in range(0, 20):
            print(self.grid[i][5].state),
        print("\n")
        for i in range(0, 20):
            print(self.grid[i][6].state),
        print("\n")
        for i in range(0, 20):
            print(self.grid[i][7].state),
        print("\n")
        for i in range(0, 20):
            print(self.grid[i][8].state),
        print("\n")
        for i in range(0, 20):
            print(self.grid[i][9].state),
        print("\n")
        for i in range(0, 20):
            print(self.grid[i][10].state),
        print("\n")
        for i in range(0, 20):
            print(self.grid[i][11].state),
        print("\n")
        for i in range(0, 20):
            print(self.grid[i][12].state),
        print("\n")
        for i in range(0, 20):
            print(self.grid[i][13].state),
        print("\n")
        for i in range(0, 20):
            print(self.grid[i][14].state),
        print("\n")
        for i in range(0, 20):
            print(self.grid[i][15].state),
        print("\n")
        for i in range(0, 20):
            print(self.grid[i][16].state),
        print("\n")
        for i in range(0, 20):
            print(self.grid[i][17].state),
        print("\n")
        for i in range(0, 20):
            print(self.grid[i][18].state),
        print("\n")
        for i in range(0, 20):
            print(self.grid[i][19].state),
        print("\n")
        print("\n")
