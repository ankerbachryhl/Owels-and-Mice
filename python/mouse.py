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
