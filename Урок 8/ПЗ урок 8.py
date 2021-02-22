# Задание 1

class Date:
    def __init__(self, date):
        self.date = date
        print(self.date)


    @classmethod
    def change(cls, date):
        date_list = date.split("-")
        date_int = [int(item) for item in date_list]
        return date_int

    @staticmethod
    def valid(date):
        date_list = date.split("-")
        date_int = [int(item) for item in date_list]
        date = date_int[0]
        month = date_int[1]
        year = date_int[2]
        if date > 31:
            print("Число месяца не прошло валидацию")
        if month > 12:
            print("Такого месяца не существует")
        if year < 0:
            print("Год не прошел валидацию")
        return date_int

print(Date.change("22-02-2021"))
print(Date.valid("36-02-2021"))

# Задание 2


class ZeroDivError(Exception):
    def __init__(self, error_text):
        self.error_text = error_text


divisible = input("Введите делимое: ")
divisor = input("Введите делитель: ")
try:
    if divisor == 0:
        raise ZeroDivError("На ноль делить нельзя")
except ValueError:
    print("На ноль делить нельзя")
except ZeroDivError as err:
    print(err)
else:
    div_result = int(divisible) / int(divisor)
    print(f"Результат деления - {div_result}")


# Задание 3


class List_Control(Exception):
    def __init__(self, error_text):
        self.error_text = error_text


user_list = []
new_el = ""
while new_el != "stop":
    new_el = input("Введите новый элемент списка: ")
    try:
        new_el = int(new_el)
        if isinstance(new_el, str):
            raise List_Control("Вы ввели не число")
    except ValueError:
        print("Вы ввели не число")
    except List_Control as err:
        print(err)
    else:
        user_list.append(new_el)
        print(user_list)
print(user_list)

# Задание 4-6


class Equipment_Warehouse:
    def __init__(self, name):
        self.name = name
        self.eqs_count = 0

    def take_equipment(self, eq_type, eq_brand, eq_count):
        self.eq_type = eq_type
        self.eq_brand = eq_brand
        self.eq_count = eq_count
        if isinstance(self.eq_count, str):
            print("Введенное значение колчества единиц оргтехники не является числом. Введите число")
        elif isinstance(self.eq_type, int) or isinstance(self.eq_brand, int):
            print("Введенное значение брэнда или типа оргтехники не является текстом. Введите текст")
        else:
            self.eqs_count = self.eqs_count + self.eq_count
        return f'Товар {self.eq_type} брэнда {self.eq_brand} в количестве {self.eq_count} шт прибыл на склад. Всего товаров на складе - {self.eqs_count}'

    def ship_equipment(self, eq_type, eq_brand, eq_count):
        self.eq_type = eq_type
        self.eq_brand = eq_brand
        self.eq_count = eq_count
        if isinstance(self.eq_count, str):
            print("Введенное значение колчества единиц оргтехники не является числом. Введите число")
        elif isinstance(self.eq_type, int) or isinstance(self.eq_brand, int):
            print("Введенное значение брэнда или типа оргтехники не является текстом. Введите текст")
        else:
            self.eqs_count = self.eqs_count - self.eq_count
        return f'Товар {self.eq_type} брэнда {self.eq_brand} в количестве {self.eq_count} шт отгружен со склада. Всего товаров на складе - {self.eqs_count}'

    def __str__(self):
        return f"Количество единиц оргтехники на складе {self.eqs_count}"


class Equipment:
    def __init__(self, brand):
        self.brand = brand


class Printer(Equipment):
    def __init__(self, brand, Printer_type):
        super().__init__(brand)
        self.Printer_type = Printer_type


class Scaner(Equipment):
    def __init__(self, brand, Scaner_type):
        super().__init__(brand)
        self.Scaner_type = Scaner_type


class Xerox(Equipment):
    def __init__(self, brand, Xerox_type):
        super().__init__(brand)
        self.Xerox_type = Xerox_type


WH = Equipment_Warehouse("Склад 1")
product1 = WH.take_equipment(eq_type="printer", eq_brand="hp", eq_count=5)
product2 = WH.take_equipment(eq_type="scaner", eq_brand="hp", eq_count=5)
product3 = WH.ship_equipment(eq_type="scaner", eq_brand="hp", eq_count=2)
print(product1)
print(product2)
print(product3)
print(WH)

# Задание 7

class ComplexNums:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.num = complex(self.a, self.b)
        print(self.num)

    def __add__(self, other):
        return ComplexNums(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return ComplexNums(self.a * other.a, self.b * other.b)


num1 = ComplexNums(3, 4)
num2 = ComplexNums(6, 7)
num3 = num1 + num2
num4 = num1 * num2
print(num3)
print(num4)