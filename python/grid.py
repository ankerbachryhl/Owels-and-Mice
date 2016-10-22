
from slot import Slot

class Grid(object):

    def __init__(self):
        self.grid = [[0 for x in range(0,20)] for x in range(0,20)]
        self.createSlot()
        self.moveMouseDic = {}

        #Walls

        # self.nSlot = ""
        # self.nSlot = ""
        # self.neSlot = ""
        # self.eSlot = ""
        # self.seSlot = ""
        # self.sSlot = ""
        # self.swSlot = ""
        # self.wSlot = ""
        # self.nwSlot = ""

    # Skriv kode der laver et slot i hvert plads i griddet.
    def createSlot(self):
        for i in range(0,20):
            for j in range(0,20):
                self.grid[i][j] = Slot(i, j)



    def checkValuesNJ(self, j):
        if j < 0:
            j += 1
            return j
        else:
            return j


    def checkValuesNEI(self, i):
        if i > 19:
            i -= 1
            return i

        else:
            return i

    def checkValuesSEJ(self, j):
        if j > 19:
            j -= 1
            return j
        else:
            return j

    def checkValuesNWI(self, i):
        if i < 0:
            i += 1
            return i

        else:
            return i

    def checkValuesSWJ(self, j):
        if j > 19:
            j -= 1
            return j
        else:
            return j

    #East
    def checkValuesEI(self, i):
        if i > 19:
            i -= 1
            return i
        else:
            return i

    def checkValuesSEI(self, i, j):
        if j == 19:
            i -= 1
            return i
        else:
            return i

    def checkValuesNEJ(self, i, j):
        if i == 19:
            j += 1
            return j
        else:
            return j

    #South
    def checkValuesSJ(self, j):
        if j > 19:
            j -= 1
            return j
        else:
            return j

    def checkValuesSWI(self, i, j):
        if j == 19:
            i += 1
            return i
        else:
            return i

    def checkValuesNWJ(self, j):
        if j < 0:
            j += 1
            return j
        else:
            return j

    #West
    def checkValuesWI(self, i):
        if i < 0:
            i += 1
            return i
        else:
            return i


    # def checkAllValuesNW(i, j):
    #     if i < 0:
    #         i += 1
    #         j -= 1
    #         return i, j
    #     elif j > 19:
    #         i += 1
    #         j -= 1
    #         return j, i
    #     else:
    #         return j, i


    def checkValuesI(self, i):
        if i < 0:
            i += 1
            return i
        elif i > 19:
            i -= 1
            return i
        else:
            return i
    def checkValuesJ(self, j):
        if j < 0:
            j += 1
            return j
        elif j > 19:
            j -= 1
            return j
        else:
            return j


    def getNeighbors(self, currentSlot, currentSlotI, currentSlotJ):


        self.nSlot = self.grid[currentSlotI][self.checkValuesNJ(currentSlotJ - 1)]
        self.neSlot = self.grid[self.checkValuesNEI(currentSlotI + 1)][self.checkValuesNEJ(currentSlotI, currentSlotJ - 1)]
        self.nwSlot = self.grid[self.checkValuesNWI(currentSlotI - 1)][self.checkValuesNWJ(currentSlotJ - 1)]
        self.eSlot = self.grid[self.checkValuesEI(currentSlotI + 1)][currentSlotJ]
        #South East
        self.seSlot = self.grid[self.checkValuesSEI(currentSlotI + 1, currentSlotJ)][self.checkValuesSEJ(urrentSlotJ + 1)]
        #South
        self.sSlot = self.grid[currentSlotI][self.checkValuesSJ(currentSlotJ + 1)]
        #South West
        self.swSlot = self.grid[self.checkValuesSWI(currentSlotI - 1, currentSlotJ)][self.checkValuesSWJ(currentSlotJ + 1)]
        #West
        self.wSlot = self.grid[self.checkValuesWI(currentSlotI - 1)][currentSlotJ]

        #Mouse Radius Dic

        self.moveMouseDic = {'N'    :   self.nSlot.dicSlot(),   'NE'    :   self.neSlot.dicSlot(),  'E' :   self.eSlot.dicSlot(),   'NW'    :   self.nwSlot.dicSlot(),  'SE'    :   self.seSlot.dicSlot(),  'S' :   self.sSlot.dicSlot(),   'SW'    :   self.swSlot.dicSlot(),  'W' :  self.wSlot.dicSlot()}


        #Owl neighbors
        #North
        # self.nnSlot = self.grid[currentSlotI][currentSlotJ + 2]
        # #North east
        # self.nneSlot = self.grid[currentSlotI + 1][currentSlotJ + 2]
        # self.nneeSlot = self.grid[currentSlotI + 2][currentSlotJ + 2]
        # self.neeSlot = self.grid[currentSlotI + 2][currentSlotJ + 1]
        # #East
        # self.eeSlot = self.grid[currentSlotI + 2][currentSlotJ]
        # #South east
        # self.seeSlot = self.grid[currentSlotI + 2][currentSlotJ - 1]
        # self.sseeSlot = self.grid[currentSlotI - 2][currentSlotJ + 2]
        # self.sseSlot = self.grid[currentSlotI + 1][currentSlotJ - 2]
        # #South
        # self.ssSlot = self.grid[currentSlotI][currentSlotJ - 2]
        # #South West
        # self.sswSlot = self.grid[currentSlotI - 1][currentSlotJ - 2]
        # self.sswwSlot = self.grid[currentSlotI - 2][currentSlotJ - 2]
        # self.swwSlot = self.grid[currentSlotI - 2][currentSlotJ - 1]
        # #West
        # self.wwSlot = self.grid[currentSlotI - 2][currentSlotJ]
        # #North West
        # self.nwwSlot = self.grid[currentSlotI - 2][currentSlotJ + 1]
        # self.nnwwSlot = self.grid[currentSlotI - 2][currentSlotJ + 2]
        # self.nnwSlot = self.grid[currentSlotI - 1][currentSlotJ + 2]
        # #Owl Radius Dic
        #
        # self.moveOwlDic = {'N' :  self.nSlot.dicSlot(), 'NE' :  self.neSlot.dicSlot(), 'E' :  self.eSlot.dicSlot(), 'SE' :  self.seSlot.dicSlot(), 'S' :  self.sSlot.dicSlot(), 'SW' :  self.swSlot.dicSlot(), 'W' :  self.wSlot.dicSlot(), 'NW' : self.wSlot.dicSlot(), 'NN' : self.nnSlot.dicSlot(), 'NNE' : self.nneSlot.dicSlot(), 'NNEE' : self.nneeSlot.dicSlot(), 'SSEE' : self.sseeSlot.dicSlot(), 'EE' : self.eeSlot.dicSlot(), 'SEE' : self.seeSlot.dicSlot(), 'SSEE' : self.sseeSlot.dicSlot(), 'SSE' : self.sseSlot.dicSlot(), 'SS' : self.ssSlot.dicSlot(), 'SSW' : self.sswSlot.dicSlot(), 'SSWW' : self.sswwSlot.dicSlot(), 'SWW' : self.swwSlot.dicSlot(), 'WW' : self.wwSlot.dicSlot(), 'NWW' : self.nwwSlot.dicSlot(), 'NNWW' : self.nnwwSlot.dicSlot(), 'NNW' : self.nnwSlot.dicSlot()}
        # self.seeSlot = self.grid[currentSlotI + 2][currentSlotJ - 1]
        # self.sseeSlot = self.grid[currentSlotI - 2][currentSlotJ + 2]
        # self.sseSlot = self.grid[currentSlotI + 1][currentSlotJ - 2]

        #Return all mouse directions
        return self.moveMouseDic
        return self.nSlot
        return self.neSlot
        return self.eSlot
        return self.seSlot
        return self.sSlot
        return self.swSlot
        return self.wSlot
        return self.nwSlot
        # Return all Owl directions
        # return self.moveOwlDic
        # return self.nnSlot
        # return self.nneSlot
        # return self.nneeSlot
        # return self.neeSlot
        # return self.eeSlot
        # return self.ssSlot
        # return self.seeSlot
        # return self.sseeSlot
        # return self.sseSlot
        # return self.sswSlot
        # return self.sswwSlot
        # return self.swwSlot
        # return self.wwSlot
        # return self.nwwSlot
        # return self.nnwwSlot
        # return self.nnwSlot




    # printer alle felter ud i terminalen
    def print_ten_Slots(self):
        for i in range(20):
            print(self.grid[i][0].num_mice),
        print("\n")
        for i in range(20):
            print(self.grid[i][1].num_mice),
        print("\n")
        for i in range(20):
            print(self.grid[i][2].num_mice),
        print("\n")
        for i in range(20):
            print(self.grid[i][3].num_mice),
        print("\n")
        for i in range(20):
            print(self.grid[i][4].num_mice),
        print("\n")
        for i in range(20):
            print(self.grid[i][5].num_mice),
        print("\n")
        for i in range(20):
            print(self.grid[i][6].num_mice),
        print("\n")
        for i in range(20):
            print(self.grid[i][7].num_mice),
        print("\n")
        for i in range(20):
            print(self.grid[i][8].num_mice),
        print("\n")
        for i in range(20):
            print(self.grid[i][9].num_mice),
        print("\n")
        for i in range(20):
            print(self.grid[i][10].num_mice),
        print("\n")
        for i in range(20):
            print(self.grid[i][11].num_mice),
        print("\n")
        for i in range(20):
            print(self.grid[i][12].num_mice),
        print("\n")
        for i in range(20):
            print(self.grid[i][13].num_mice),
        print("\n")
        for i in range(20):
            print(self.grid[i][13].num_mice),
        print("\n")
        for i in range(20):
            print(self.grid[i][14].num_mice),
        print("\n")
        for i in range(20):
            print(self.grid[i][15].num_mice),
        print("\n")
        for i in range(20):
            print(self.grid[i][16].num_mice),
        print("\n")
        for i in range(20):
            print(self.grid[i][17].num_mice),
        print("\n")
        for i in range(20):
            print(self.grid[i][18].num_mice),
        print("\n")
        for i in range(20):
            print(self.grid[i][19].num_mice),

        print("\n")
        print("\n")
        print("\n")
        print("\n")
