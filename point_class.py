# Importing the math module for mathematical operations
import math

# Defining a class named 'point'
class point():
    # Constructor method to initialize the object with default or provided coordinates
    def __init__(self, abcisse = 0, ordonne = 0):
        self.__abcisse = abcisse
        self.__ordonne = ordonne

    # Getter method for retrieving the x-coordinate
    def getabcisse(self):
        return self.__abcisse

    # Setter method for setting the x-coordinate with type checking
    def setabcisse(self, abcisse):
        if isinstance(abcisse, (int, float)) and not abcisse == None:
            self.__abcisse = abcisse
        else:
            print("La coordonnée abcisse doit être un nombre")

    # Getter method for retrieving the y-coordinate
    def getordonne(self):
        return self.__ordonne

    # Setter method for setting the y-coordinate with type checking
    def setordonne(self, ordonnee):
        if isinstance(ordonnee, (int, float)) and not ordonnee == None:
            self.__ordonne = ordonnee
        else:
            print("La coordonnée ordonnée doit être un nombre")

    # Method to calculate the Euclidean norm of the point
    def Norme(self):
        return math.sqrt(self.getabcisse() ** 2 + self.getordonne() ** 2)

    # Method to calculate the Euclidean distance between two points
    def distance(self, p):
        x1, y1 = self.getabcisse(), self.getordonne()
        x2, y2 = p.getabcisse(), p.getordonne()
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
