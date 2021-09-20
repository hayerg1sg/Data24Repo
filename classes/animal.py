class animal:

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("one breath in and out")

    def eat(self):
        print("nom nom nom")

    def procreate(self):
        print("lets get it on")

cat= animal()
