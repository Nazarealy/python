class Sqeezer:

    staticProdaction = 100

    def __init__(self, color = "defolt", sqeezSpeed = 0, enginePower = 0, founder = "defolt", price = 0, rating = 0.0, material = "defolt"):
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
        return "color: {0},\nsqeezSpeed: {1},\nenginePower: {2}\nfounder: {3},\nprice: {4},\nrating: {5},\nmaterial: {6}.\n".format(self.color, self.sqeezSpeed, 
            self.enginePower, self.founder, self.price, self.rating, self.material)   

    @staticmethod
    def printHello():
        print('hello') 

    @staticmethod
    def anotherstaticProdaction(newstaticProdaction):
            Sqeezer.staticProdaction += newstaticProdaction




defalt = Sqeezer()
juicy = Sqeezer("red", 15, 220, "German", 15, 5)

print(defalt)
print(juicy)

print("Total number of prodaction: " + str(Sqeezer.staticProdaction))
Sqeezer.anotherstaticProdaction(50)
print("New number of prodaction: " + str(Sqeezer.staticProdaction))

    

    

    


   