from mouse import Mouse

class Owl(Mouse):

    def __init__(self):
        Mouse.__init__(self)

    #Draeber en mus
    def eat(currentSlot):
        if currentSlot.num_mice == 1 and currentSlot.has_rock == False:
            currentSlot.rmAnimal("mouse")
        elif currentSlot.num_mice == 2:
            currentSlot.rmAnimal("mouse")

    #Skal geare saadan at den ikke aeder en mus hvis den gemmer sig
