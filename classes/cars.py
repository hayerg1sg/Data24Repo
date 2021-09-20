class Cars:
    def __init__(self, car_make, max_speed):
        print("vroom")
        self. car_make = car_make          #class variables
        self.max_speed = max_speed          #class variables
        self.current_speed =0

    def increase_speed(self, speed_increase):
        if self.current_speed + speed_increase > self.max_speed:
            print(f"your car cannot go any quicker than {self.max_speed}mph")
            self.current_speed = self.max_speed
        else:
            self.current_speed+=speed_increase

my_car = Cars("bentley", 200)
print(my_car.car_make)
print(my_car.current_speed)
my_car.increase_speed(150)
print(my_car.current_speed)
