from module.Cutlery import Cutlery
from module.Structure_type import Structure_type

class PlateCutlery(Cutlery, object):
    def __init__(self, rating = 0, price = 0, material = "wood", prodaction = "well", diagonal = 0.0, color = "string", structure = Structure_type.SHALLOW):
        super(PlateCutlery, self).__init__(rating, price, material, prodaction)
        self.diagonal = diagonal
        self.color = color
        self.structure = structure

    def __str__(self):
        return ('FOR PLATE : Rating = {0}, price = {1}$, material is {2}, prodaction is {3}, diagonal = {4}, color is {5}, structure is {6}').format(
            self.rating, self.price, self.material, self.prodaction, self.diagonal, self.color, self.structure)

    def __repr__(self):
        return self.__str__()           
        


