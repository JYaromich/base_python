class Car:
    def __init__(self, speed: int, color: str, name: str, is_polise: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_polise

    def go(self):
        print(f'Car {self.name} going')

    def stop(self):
        print(f'Car {self.name} stop')

    def turn(self, direction: str):
        print(f'Car {self.name} turn {direction}')

    def show_speed(self):
        print(f'Seep {self.name} - {self.speed}')


class TownCar(Car):
    def show_speed(self):
        print(f'Seed {self.name} - {self.speed}') if self.speed <= 60 else print('Car is speeding!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'Seed {self.name} - {self.speed}') if self.speed <= 40 else print('Car is speeding!')


class PoliceCar(Car):
    pass


car = Car(10, 'red', 'niva', False)
town_car = TownCar(70, 'red', 'nissan', False)
sport_car = SportCar(150, 'silver', 'Alfa Romeo', False)
work_car = WorkCar(50, 'black', 'JBL', False)
police_car = PoliceCar(50, 'black', 'lada', True)

print(town_car.speed, town_car.color, town_car.name, town_car.is_polise)
print(sport_car.speed, sport_car.color, sport_car.name, sport_car.is_polise)
print(work_car.speed, work_car.color, work_car.name, work_car.is_polise)
print(police_car.speed, police_car.color, police_car.name, police_car.is_polise)

town_car.go()
town_car.stop()
town_car.turn('left')
town_car.show_speed()

sport_car.go()
sport_car.stop()
sport_car.turn('left')
sport_car.show_speed()

work_car.go()
work_car.stop()
work_car.turn('left')
work_car.show_speed()

police_car.go()
police_car.stop()
police_car.turn('left')
police_car.show_speed()

car.go()
car.stop()
car.turn('left')
car.show_speed()
