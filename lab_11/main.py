from module.Cutlery import Cutlery
from module.ForkCutlery import ForkCutlery
from module.PlateCutlery import PlateCutlery
from module.Sharpness_type import Sharpness_type
from module.SpoonCutlery import SpoonCutlery
from module.Structure_type import Structure_type

class CutleryManager:
    def __init__(self, cutlery_list):
        self.cutlery_list = cutlery_list

    def sort_cutlery_list_by_price(self, reverse):
        return sorted(self.cutlery_list, key=lambda cutlery: cutlery.price, reverse=reverse)

    def sort_cutlery_list_by_rating(self, reverse):
        return sorted(self.cutlery_list, key=lambda cutlery: cutlery.rating, reverse=reverse)

    def find_cutlery_by_material(self, material):
        return list(filter(lambda cutlery: cutlery.material == material, self.cutlery_list))

#cutlery = Cutlery(3, 400, "metal", "very") - for general class
testFork = ForkCutlery(4, 100, "wood", "much", 3, Sharpness_type.STRONG_STATE)
testSpoon = SpoonCutlery(5, 400, "plastic", "many", 20, "red")
testPlate = PlateCutlery(3, 300, "metal", "very", 5.5, "yellow", Structure_type.DEEP)

cutleries = [testPlate, testFork, testSpoon]
manager = CutleryManager(cutleries)

print(manager.sort_cutlery_list_by_price(False))
print(manager.sort_cutlery_list_by_rating(True))
print(manager.find_cutlery_by_material("wood"))


