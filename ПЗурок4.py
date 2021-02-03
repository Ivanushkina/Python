from sys import argv
from functools import reduce
from itertools import count
from itertools import cycle
from math import factorial

# Задание 1

def zp(hours, wagerate, bonus):
     salary = hours * wagerate + bonus
     return salary

script_name, hours, wagerate, bonus = argv
sal = zp(int(hours), int(wagerate), int(bonus))
print(sal)

# Задание 2

# lst = [4, 6, 3, 7, 5]
# new_lst = [el for el in lst if el > el[lst.index(el)-1]]
# print(new_lst)

# Задание 3

result = [a for a in range(20, 240) if a % 20 == 0 or a % 21 == 0]
print(result)

# Задание 4

list0 = [2,2,5,7,9,4,6,5,4,4,0]
unique = []
list1 = [unique.append(b) for b in list0 if b not in unique]
list1 = unique
print(list1)

# Задание 5

def red_func(arg1, arg2):
    sum_args = arg1+arg2
    return sum_args


range1 = [r1 for r1 in range(100, 1001) if r1 % 2 == 0]
print(reduce(red_func, range1))

# Задание 6 a

script_name, user_num, border_num = argv
for el in count(int(user_num)):
    if el > int(border_num):
        break
    else:
        print(el)

# Задание 6 b

script_name, user_list, border_num = argv
i = 0
for el in cycle(user_list):
    if i > int(border_num):
        break
    print(el)
    i += 1

# Задание 7

def fact(n):
    for el in range(1,(n+1)):
        yield el

n = int(input('Введите число: '))
for el in fact(n):
    print(el)
print(factorial(n))