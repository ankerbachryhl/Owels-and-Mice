#pygame

import random


class Mouse(object):

    mouse_steps = 0
    mouse_dead = False
    mouse_hide = False

    #Steps 20 steps = dead
    def steps():
        if mouse_steps == 20:
            mouse_dead = True

    #Styrer hvad der sker naar musen dear
    def dead(currentSlot):
        if mouse_dead == True:
            currentSlot.rmAnimal("mouse")

    #Move regler for mouse, bruger neighbors like moveDic['numMice']

    def mouseMoveRules(currentSlot):
        rand_one = randrange.random(0,2)
        possibleDirections = []
        if rand_one == 1:
            if moveDic['N'].numOwl == 0 and moveDic['N'].numMice == 2:
                possibleDirections.append(moveDic['N'])

            if moveDic['NE'].numOwl == 0 and moveDic['NE'].numMice == 2:
                possibleDirections.append(moveDic['NE'])

            if moveDic['E'].numOwl == 0 and moveDic['E'].numMice == 2:
                possibleDirections.append(moveDic['E'])

            if moveDic['SE'].numOwl == 0 and moveDic['SE'].numMice == 2:
                possibleDirections.append(moveDic['SE'])

            if moveDic['S'].numOwl == 0 and moveDic['S'].numMice == 2:
                possibleDirections.append(moveDic['S'])

            if moveDic['SW'].numOwl == 0 and moveDic['SW'].numMice == 2:
                possibleDirections.append(moveDic['SW'])

            if moveDic['W'].numOwl == 0 and moveDic['W'].numMice == 2:
                possibleDirections.append(moveDic['W'])

            if moveDic['NW'].numOwl == 0 and moveDic['NW'].numMice == 2:
                possibleDirections.append(moveDic['NW'])

            rand_two = random.randrange(len(possibleDirections))
            currentSlot.rmAnimal("mouse")
            possibleDirections[rand_two].addAnimal("mouse")




    def getDir(currentSlot):
        if moveDic['N'].numMice == 1:
            pass

    #Spawner ny mus
    def pairing(currentSlot, neighbors):
        random = random.randrange(0,10)
        if currentSlot.num_mice == 2 and random == 9:
            x = random.randrange(0,4)
            neighbors[x].addAnimal("mouse")

    #Musen gemmer sig
    def hide(currentSlot):
        if owl_nearby == True and currentSlot.has_rock == True:
            mouse_hide = True
