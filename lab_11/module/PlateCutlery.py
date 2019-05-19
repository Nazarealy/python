from module.Cutlery import Cutlery

class PlateCutlery(Cutlery):
    def __init__(self, diagonal, color, structure):
        super().__init__(diagonal, color)
        self.structure = structure

