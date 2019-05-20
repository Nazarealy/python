from module.Cutlery import Cutlery
from module.Sharpness_type import Sharpness_type

class ForkCutlery(Cutlery):
    def __init__(self, needlesnumber, sharpness):
        self.needlesnumber = needlesnumber
        self.sharpness = sharpness