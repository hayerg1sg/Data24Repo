from reptile import *
class snake(reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.venom = None
        self.surprise_attack()

    def surprise_attack(self):
        print("gotcha")
        
sally= snake()