import re
import json
import random

# Задание 1

content = ()
while True:
    content = input('Введите данные: ') + "\n"
    new_file = open("textfile.txt", "a", encoding="UTF-8")
    new_file.writelines(content)
    new_file.close()
    if content == "\n":
        break

# Задание 2

with open("new_text_file.txt", "r", encoding="UTF-8") as read_file:
    lines_list = read_file.readlines()
    lines_count = len(lines_list)
    print("Количество строк в файле = " + str(lines_count))
    i = 1
    for line in lines_list:
        words_count = len(line.split())
        print("Количество слов в " + str(i) + " строке = " + str(words_count))
        i += 1

# Задание 3

with open("employees_salarys.txt", "r", encoding="UTF-8") as salaries_file:
    employees_list = salaries_file.readlines()
    sal = 0
    for line in employees_list:
        value_list = line.split()
        sal += int(value_list[1])
        if int(value_list[1]) < 20000:
            print("Бедолага с зп меньше 20к - " + str(value_list[0]))
    print("Средняя зп сотрудника = " + str(sal/len(employees_list)))

# Задание 4

with open("numbers_file.txt", "r", encoding="UTF-8") as numbers_file:
    numbers_list = numbers_file.readlines()
    numb_list = []
    for line in numbers_list:
        value_list = line.split()
        if value_list[2] == "1":
            value_list.insert(0, "Один")
            value_list.pop(1)
        elif value_list[2] == "2":
            value_list.insert(0, "Два")
            value_list.pop(1)
        elif value_list[2] == "3":
            value_list.insert(0, "Три")
            value_list.pop(1)
        elif value_list[2] == "4":
            value_list.insert(0, "Четыре")
            value_list.pop(1)
        value = (" ".join(value_list))
        numb_list.append(str(value))
    print(numb_list)
with open("textfile.txt", "w", encoding="UTF-8") as f_obj:
    file_text = f_obj.writelines(numb_list)
    print(file_text)

# Задание 5

new_numb_list = []
while len(new_numb_list) < 10:
    numb = random.randint(1, 10)
    new_numb_list.append(str(numb))
value = (" ".join(new_numb_list))
with open("random_numbers.txt", "w", encoding="UTF-8") as rand_numb_file:
    rand_numb_file.writelines(value)
with open("random_numbers.txt", "r", encoding="UTF-8") as rand_numb_read_file:
    rand_numb_list = rand_numb_read_file.read()
    rand_numb_list = rand_numb_list.split()
    arg_sum = 0
    for arg in rand_numb_list:
        arg_sum += int(arg)
    print(arg_sum)

# Задание 6

sub_list = []
hours_list = []
with open("subject_list.txt", "r", encoding="UTF-8") as subject_list:
    subject_list = subject_list.readlines()
    for line in subject_list:
        one_sub = line.split(":")
        sub_name = one_sub[0]
        sub_list.append(sub_name)
    for line in subject_list:
        numb_from_line = (re.findall(r'\d+', line))
        numb_sum = 0
        for arg in numb_from_line:
            numb_sum += int(arg)
        hours_list.append(numb_sum)
    a = 0
    final_dict = dict()
    while a < len(sub_list):
        key = sub_list[a]
        value = hours_list[a]
        final_dict.update({key: value})
        a += 1
    print(final_dict)

# Задание 7

with open("firms_data.txt", "r", encoding="UTF-8") as firms_data_list:
    firms_data_list = firms_data_list.readlines()
    print(firms_data_list)
    avg_profit = 0
    i = 0
    final_list = []
    firms_dict = dict()
    avg_dict = dict()
    for line in firms_data_list:
        firm_data = line.split()
        firm_name = firm_data[0]
        revenue = int(firm_data[2])
        costs = int(firm_data[3])
        profit = revenue-costs
        firms_dict.update({firm_name: profit})
        if profit > 0:
            avg_profit += profit
            i += 1
        print("Прибыль органиизации " + firm_name + " = " + str(profit))
    avg_profit = avg_profit/i
    avg_dict.update({"average_profit": avg_profit})
    final_list.append(firms_dict)
    final_list.append(avg_dict)
    print("Средняя прибыль организаций - " + str(avg_profit))
with open("firms_data.json", "w", encoding="UTF-8") as firms_array:
    json.dump(final_list, firms_array)
