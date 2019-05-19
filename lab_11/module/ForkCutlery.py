from module.Cutlery import Cutlery

class ForkCutlery(Cutlery):
    def __init__(self, needlesnumber, sharpness):
        super().__init__(needlesnumber)
        self.sharpness = sharpness