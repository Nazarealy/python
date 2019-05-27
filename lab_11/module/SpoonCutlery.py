from module.Cutlery import Cutlery

class SpoonCutlery(Cutlery, object):
    def __init__(self, rating = 0, price = 0, material = "wood", prodaction = "well", lenght = 0.0, color = "string"):
        super(SpoonCutlery, self).__init__(rating, price, material, prodaction)
        self.lenght = lenght
        self.color = color

    def __str__(self):
        return ('FOR SPOON : Rating = {0}, price = {1}$, material is {2}, prodaction is {3}, lenght = {4}, color is {5}').format(
            self.rating, self.price, self.material, self.prodaction, self.lenght, self.color)

    def __repr__(self):
        return self.__str__()