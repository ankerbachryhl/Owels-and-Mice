
class Owl(object):

    #Draeber en mus
    def eat(currentSlot):
        if currentSlot.num_mice == (1,2):
            currentSlot.rmAnimal("mouse")

    #Skal geare saadan at den ikke aeder en mus hvis den gemmer sig
