class Car:

    def __init__(self, model, speed):
        self.model = model
        self.speed = speed

    def run(self):
        print(f'Автомобиль {self.model} поехала со скростью {self.speed}')

    def stop(self):
        print(f'Автомобиль {self.model} остановилась')


class PassengerCar(Car):
    type_ = "Легковой"

    def __init__(self, model, speed, transmission):
        super().__init__(model, speed)
        self.transmission = transmission

    def run(self):
        print(
            f'{PassengerCar.type_} автомобиль  {self.model} имеет коробку передач {self.transmission}. Едим со скростью {self.speed} ')

    def stop(self):
        print(f'{PassengerCar.type_} автомобиль  {self.model} остановилась')


class TruckCar(Car):
    type_ = "Грузовой"

    def __init__(self, model, speed, transmission):
        super().__init__(model, speed)
        self.transmission = transmission

    def run(self):
        print(
            f'{TruckCar.type_} автомобиль {self.model} имеет коробку передач {self.transmission}. Едим со скростью {self.speed} ')

    def stop(self):
        print(f'{TruckCar.type_} автомобиль {self.model} остановилась')


class Shop:

    all_count = 0

    def __init__(self, name, count):
        self.name = name
        self.count = count
        Shop.all_count += count

    def print_shop(self):
        print(f'Количество всего товара {Shop.all_count}')

    def add_count(self, count):
        self.count += count
        Shop.all_count += count


if __name__ == "__main__":
    print("1 task")
    car = Car('BMW', 200)
    car.run()
    car.stop()
    print("-"*30)
    passenger = PassengerCar("Mers", 150, 'автомат')
    passenger.run()
    passenger.stop()

    print("-" * 30)
    track = TruckCar("Газель", 150, 'ручная')
    track.run()
    track.stop()

    print("2 task")
    silpo = Shop('Silpo', 10)
    silpo.print_shop()
    silpo.add_count(20)
    silpo.print_shop()

    atb = Shop('ATB', 30)
    atb.print_shop()
    atb.add_count(40)
    atb.print_shop()
