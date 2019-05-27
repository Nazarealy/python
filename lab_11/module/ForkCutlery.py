from module.Cutlery import Cutlery
from module.Sharpness_type import Sharpness_type

class ForkCutlery(Cutlery, object):
    def __init__(self, rating = 0, price = 0, material = "wood", prodaction = "well", needlesnumber = 0, sharpness = Sharpness_type.EASY_STATE):
        super(ForkCutlery, self).__init__(rating, price, material, prodaction)
        self.needlesnumber = needlesnumber
        self.sharpness = sharpness

    def __str__(self):
        return ('FOR FORK : Rating = {0}, price = {1}$, material is {2}, prodaction is {3}, needlesnumber = {4}, sharpnesstype is {5}').format(
    self.rating, self.price, self.material, self.prodaction, self.needlesnumber, self.sharpness)    

    def __repr__(self):
        return self.__str__()