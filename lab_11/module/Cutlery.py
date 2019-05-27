class Cutlery:
    def __init__(self, rating = 0, price = 0, material = "wood", prodaction = "well"):
        self.rating = rating
        self.price = price
        self.material = material
        self.prodaction = prodaction

    def __str__(self):
        return('Rating = {0}, price = {1}$, material is {2}, prodaction is {3}.').format(
            self.rating, self.price, self.material, self.prodaction)

    def __repr__(self):
        return self.__str__()

