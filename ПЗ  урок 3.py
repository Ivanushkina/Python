# Задание 1

def divis(a, b):
    div_result = a / b
    return div_result


ask_num1 = int(input("Введите числитель: "))
ask_num2 = int(input("Введите знаменатель: "))
try:
    print(divis(ask_num1, ask_num2))
except ZeroDivisionError:
    print('На ноль делить нельзя')


# Задание 2

def info(name, second_name, birth_year, city, email, phone_number):
    info_result = (
            'Имя - ' + name + ', Фамилия - ' + second_name + ', Год рождения - ' + birth_year + ', Город проживания - ' + city + ', Электронная почта - ' + email + ', Номер телефона - ' + phone_number)
    return info_result


name = input('Введите имя: ')
second_name = input('Введите фамилию: ')
birth_year = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите электронную почту: ')
phone_number = input('Введите номер телефона: ')
print(
    info(name=name, second_name=second_name, birth_year=birth_year, city=city, email=email, phone_number=phone_number))


# Задание 3

def my_func(a, b, c):
    result_list = [a, b, c]
    ind = result_list.index(min(result_list))
    result_list.pop(ind)
    sum_result = sum(result_list)
    return sum_result


user_val = input('Введите три числа через пробел: ')
user_list = user_val.split(' ')
print(my_func(int(user_list[0]), int(user_list[1]), int(user_list[2])))


# Задание 4. Вариант 1

def my_func1(x, y):
    x = float(x)
    y = int(y)
    if y > 0:
        y = -y
    func_result = x ** y
    return func_result


user_val1 = input('Введите действительное положительное число: ')
user_val2 = input('Введите целое отрицательное число: ')
print(my_func1(user_val1, user_val2))


# Задание 4. Вариант 2

def my_func1(x, y):
    x = float(x)
    y = int(y)
    if y > 0:
        y = -y
    i = 1
    xx = x
    while i < -y:
        xx = xx * x
        i += 1
    func_result = 1 / xx
    return func_result


user_val1 = input('Введите действительное положительное число: ')
user_val2 = input('Введите целое отрицательное число: ')
print(my_func1(user_val1, user_val2))

# Задание 5

numb_sum = 0
while True:
    user_numb = input('Введите два числа через пробел. Для завершения суммирования введите "end". ')
    if user_numb == 'end':
        break
    else:
        user_numb_list = user_numb.split(' ')
        user_numb_list = [int(item) for item in user_numb_list]
        numb_sum = sum(user_numb_list) + numb_sum
        print(numb_sum)


# Задание 6

def int_func(a):
    result = a.title()
    return result


user_string = input('Напишите фразу в нижнем регистре: ')
print(int_func(user_string))
