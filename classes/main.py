from abc import ABC, abstractmethod
class Car(ABC):         #abstract class
    def speed(self):    #abstract method
        pass

class Tesla(Car):       #subclass
    def speed(self):
        print("The speed of this car is 80mph")

class Ford(Car):        #subclass
    def speed(self):
        print("The speed of this car is 60mph")

class Porsche(Car):       #subclass
    def speed(self):
        print("The speed of this car is 10mph")

t = Tesla()
t.speed()

f = Ford()
f.speed()

p = Porsche()
p.speed()