ListPass = {'Gena': 'qwerty'}
login = input("Введите логин: ")
n = 1
if login in ListPass:
    while n < 4:
        password = input("Введите пароль: ")
        if password == ListPass[login]:
            print("Успешно")
        else:
            print(f"Неправильный пароль, попыток {n} из 3х")
            n += 1
        print("Заходите через 5 минут")
    else:
        print("Not user")



class Transport:
    def __init__(self, speed, capacity):
        self._speed = speed
        self._capacity = capacity

    def start(self):
        print("Транспорт начал движение")
    def stop(self):
        print("Транспорт остановил движение")
    def info(self):
        print(f"Скорость {self._speed} км/ч, вместимость {self._capacity}чел")

class Car(Transport):
    def __init__(self, speed, capacity, brand):
        super().__init__(speed, capacity)
        self.brand = brand

    def info(self):
        base_info = super().info()
        print(f"Автомобиль {self.brand}: {base_info}")

class Bus(Transport):
    def __init__(self, speed, capacity, route_number):
        super().__init__(speed, capacity)
        self.brand = route_number

    def info(self):
        base_info = super().info()
        print(f"Автобус {self.brand}: {base_info}")
# Класс Electric:
# Имеет атрибут: _battery_level - уровень заряда батареи (%)
# Методы: charge() - заряжает батарею до 100%.
# battery_status() - показывает уровень заряда.
# Класс ElectricCar - пример множественного наследования:
# Наследуется от Car и Electric.
# Переопределяет метод info(), добавляя данные о заряде батереи.

class Electric:
    def __init__(self, battery_level):
        self._battery_level = battery_level

    def charge(self):
        self._battery_level = 100
        print("Батарея заряжена")

    def battery_status(self):
        print(f"Уровень заряда: {self._battery_level}%")


class ElectricCar(Car, Electric):
    def __init__(self, speed, capacity, brand, battery_level):
        Car.__init__(self, speed, capacity, brand)
        Electric.__init__(self, battery_level)

    def info(self):
        car_info = super().info()
        print(f"Электромобиль {self.brand}:{car_info}, заряд {self._battery_level}%")


tesla = ElectricCar(120, 5, 'Tesla', 85)
tesla.start()
tesla.charge()
tesla.info()

bus = Bus(50, 40, 13)
bus.start()
bus.info()

