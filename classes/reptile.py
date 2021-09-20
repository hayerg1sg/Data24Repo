from animal import *
class reptile(animal):

    def __init__(self):
        self.cold_blooded = True
        self.tetrapped = None
        self.heart_chambers = [3, 4]
        super().__init__()

    def seek_heat(self):
        print("its chilli outside where is the sun")

gekko = reptile()
