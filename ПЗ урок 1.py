# Задание 1

name = str(input('Введите имя: '))
print("Меня зовут", name)
second_name = str(input('Введите фамилию: '))
print('Моя фамилия', second_name)
age = str(input('Введите возраст: '))
print('Мне', age, 'лет')
first_arg = int(input('Введите первое слагаемое: '))
second_arg = int(input('Введите второе слагаемое: '))
sum_result = first_arg + second_arg
print('Сумма введенных чисел =', sum_result)

# Задание 2

first_time = int(input('Введите время в секундах: '))
hours_result = int(first_time / 3600)
min_result = float(first_time / 60)
minutes_result = int(min_result) % 60
seconds_result = (first_time % 3600) % 60
print('Сконвертированное время -', hours_result, ':', minutes_result, ':', seconds_result)

# Задание 3

numb = input('Введите число для расчета: ')
arg2 = int(numb + numb)
arg3 = int(numb + numb + numb)
arg_sum = int(numb) + arg2 + arg3
print('Рассчитанная сумма =', arg_sum)

# Задание 4. Вообще не поняла, как сделать задание с помощью цикла while, поэтому сделала, как сама разобралась

numb_max = input('Введите число из не менее 2 цифр: ')
max_num = max([int(i)
               for i in str(numb_max)])
print('Самая большая цифра из введенной последовательности -', max_num)

# Задание 5

revenue = input('Введите значение выручки в рублях: ')
costs = input('Введите суммарные издержки в рублях: ')
profit = float(revenue) - float(costs)
if profit > 0:
    profitability = (profit / float(revenue)) * 100
    print('Деятельность фирмы рентабельна. Рентабельность фирмы =', profitability, '%')
    employees = input('Введите количество сотрудников в штате: ')
    employee_profit = profit / int(employees)
    print('Прибыль на одного сотрудника в рублях =', employee_profit)
else:
    print('Деятельность фирмы нерентабельна')

# Задание 6

first_day_distance = input('Сколько км спортсмен пробежал в 1 день? Введите значение: ')
x_day_distance = input('Целевый результат в км: ')
a = float(first_day_distance)
x_day = 0
while a < float(x_day_distance):
    a = a * 1.1
    x_day = x_day + 1
print('День, на который спортсмен достигнет целевого результата, -', x_day)
