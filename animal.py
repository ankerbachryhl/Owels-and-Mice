import random
from mouse import Mouse
from owl import Owl

class Animal(Owl):
    def __init__(self):
        Owl.__init__(self)

    #Klassen bruges til at binde de forskellige klasser sammen saadan at de alle har adgang til self variablerne
