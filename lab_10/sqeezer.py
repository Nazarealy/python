class Sqeezer:

    staticProdaction = 100

    def __init__(self, color = "%variant%", sqeezSpeed = 0, enginePower = 0, founder = "%variant%", price = 0, rating = 0.0, material = "%variant%"):
        self.color = color
        self.sqeezSpeed = sqeezSpeed
        self.enginePower = enginePower
        self.founder = founder
        self.price = price
        self.rating = rating
        self.material = material

    def __del__(self):
        print("%s deleted" % self.color)

    def __str__(self):
        return "color: {0}, sqeezSpeed: {1}, enginePower: {2}founder: {3},\nprice: {4}, rating: {5}, material: {6}.\n".format(self.color, self.sqeezSpeed, 
            self.enginePower, self.founder, self.price, self.rating, self.material)   

    @staticmethod
    def anotherstaticProdaction(newstaticProdaction):
            Sqeezer.staticProdaction += newstaticProdaction

defalt = Sqeezer()
juicy = Sqeezer("red", 15, 220, "German", 15, 5, "plastick")

print(defalt)
print(juicy)

print("Total number of prodaction: " + str(Sqeezer.staticProdaction))
Sqeezer.anotherstaticProdaction(50)
print("Total number of prodaction: " + str(Sqeezer.staticProdaction))
print()
    

    


   