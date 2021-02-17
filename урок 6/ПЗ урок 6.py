import time


# Задание 1

class TrafficLight:
    def __init__(self):
        self.__color = "Красный"
    def running(self):
        while True:
            self.__TrafficLight__color = "Красный"
            print(self.__TrafficLight__color)
            time.sleep(7)
            self.__TrafficLight__color = "Желтый"
            print(self.__TrafficLight__color)
            time.sleep(2)
            self.__TrafficLight__color = "Зеленый"
            print(self.__TrafficLight__color)
            time.sleep(9)

light = TrafficLight()
print(light.running())

# Задание 2

class Road:
    def __init__(self):
        self._length = 6000
        self._width = 40

    def mass(self, m1, thickness):
        length = self._length
        width = self._width
        m = length * width * m1 * thickness
        return m


obj = Road()
print(obj.mass(5, 60))

# Задание 3

S_income = {"wage": 50000, "bonus": 20000}


class Worker:
    _income = S_income.get("wage") + S_income.get("bonus")

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)
        self.income = super()._income

    def get_full_name(self, name, surname):
        self.full_name = f'{name} {surname}'
        return self.full_name

    def get_total_income(self):
        self.total_income = self.income
        return self.total_income


person = Position(name="Екатерина", surname="Иванушкина", position="Бизнес-аналитик")
print(person.get_full_name(name="Екатерина", surname="Иванушкина"))
print(person.get_total_income())

# Задание 4

class Car:
    def __init__(self, speed, color, name, is_police):
         self.speed = speed
         self.color = color
         self.name = name
         self.is_police = is_police

    def go(self):
        return f'Машина {self.name} едет'

    def stop(self):
        return f'Машина {self.name} остановилась'

    def turn_left(self):
        return "Машина повернула налево"

    def turn_right(self):
        return "Машина повернула направо"

    def show_speed(self):
        self.current_speed = self.speed
        return self.current_speed


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        self.current_speed = self.speed
        if self.current_speed > 60:
            return  "Скорось превышена"

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        self.current_speed = self.speed
        if self.current_speed > 40:
            return  "Скорось превышена"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def go(self):
        return f'Полциейская машина {self.name} едет'

    def stop(self):
        return f'Полциейская машина {self.name} остановилась'

    def turn_left(self):
        return "Полциейская машина повернула налево"

    def turn_right(self):
        return "Полциейская машина повернула направо"


w_car = WorkCar(70, "red", "my_car", "False")
if w_car.speed == 0:
    print(w_car.stop())
else:
    print(w_car.go())
print(f'Скорость машины - {w_car.speed}')
print(w_car.show_speed())

p_car = PoliceCar(120, "blue", "my_p_car", "True")
if p_car.speed == 0:
    print(p_car.stop())
else:
    print(p_car.go())
print(f'Скорость машины - {p_car.speed}')
print(p_car.show_speed())

t_car = TownCar(70, "white", "my_t_car", "False")
if t_car.speed == 0:
    print(t_car.stop())
else:
    print(t_car.go())
print(f'Скорость машины - {t_car.speed}')
print(t_car.show_speed())

s_car = TownCar(200, "black", "my_s_car", "False")
if s_car.speed == 0:
    print(s_car.stop())
else:
    print(s_car.go())
print(f'Скорость машины - {s_car.speed}')
print(s_car.show_speed())


# Задание 5

class Stationery:
    def __init__(self, title):
        self.title = title
        print(self.title)

    def draw(self):
        return "Запуск отрисовки"


class Pen(Stationery):
    def draw(self):
        return "Рисуем графику штриховкой"


class Pencil (Stationery):
    def draw(self):
        return "Учимся рисовать светотень"


class Handle(Stationery):
    def draw(self):
        return "Учимся калиграфии"

pen = Pen("Ручка черная")
print(pen.draw())

pencil = Pencil("Карандаш средней жесткости")
print(pencil.draw())

handle = Handle("Маркер темно-синий")
print(handle.draw())