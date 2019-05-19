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

    def sort_cutlery_list_by_duration(self, reverse):
        return sorted(self.cutlery_list, key=lambda cutlery: cutlery.duration, reverse=reverse)

    def find_cutlery_by_children_number(self, children_number):
        return list(filter(lambda cutlery: cutlery.children_number == children_number, self.cutlery_list))

cutlery = Cutlery(5, 200, "wood", "very big")
#sharpness = sharpness(400, 2.5, 5, 15, Sharpness_type.STRONG_STATE)
#trampoline = TrampolineJumping(150, 1.2, 3, 8, 5)
cutleries = [Cutlery]
manager = CutleryManager(cutleries)

print(manager.sort_cutlery_list_by_price(False))
print(manager.sort_cutlery_list_by_duration(True))
print(manager.find_cutlery_by_children_number(5))