class Cutlery:
    def __init__(self, rating, price, material, prodaction):
        self.rating = rating
        self.price = price
        self.material = material
        self.prodaction = prodaction

    def __del__(self):
        print("destructor")

