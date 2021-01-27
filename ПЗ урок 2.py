# Задание 1

lst = ['zfk', 23, [1, 2, 3], (1, 2, 3), {9, 2, 3}, True]
a = 1
while a <= 6:
    print(type(lst[a - 1]))
    a += 1

# Задание 2

b = input('Введите список элементов через запятую: ')
b = b.split(',')
i = 0
j = 1
while i < (len(b) - 1) or j < (len(b) - 1):
    b[i], b[j] = b[j], b[i]
    i = i + 2
    j = j + 2
print(b)

# Задание 3

slovar = dict(
    winter=['12', '1', '2'],
    spring=['3', '4', '5'],
    summer=['6', '7', '8'],
    fall=['9', '10', '11']
)
month = input('Введите целое число, соответствующее номеру месяца: ')
winter = slovar.setdefault('winter')
spring = slovar.setdefault('spring')
summer = slovar.setdefault('summer')
fall = slovar.setdefault('fall')
if month == winter[0] or month == winter[1] or month == winter[2]:
    print('Месяц зимний')
elif month == spring[0] or month == spring[1] or month == spring[2]:
    print('Месяц весенний')
elif month == summer[0] or month == summer[1] or month == summer[2]:
    print('Месяц летний')
elif month == fall[0] or month == fall[1] or month == fall[2]:
    print('Месяц летний')
else:
    print('Такого месяца не существует')

# Задание 4

user_phrase = input('Напишите бога ради что-нибудь: ')
user_phrase = user_phrase.split(' ')
for ind, user_word in enumerate(user_phrase):
    if len(user_word) <= 10:
        print(ind, user_word)
    else:
        print(ind, user_word[0:10])

# Задание 5

rate = [8, 7, 6, 6, 2, 1]
user_num = int(input('Введите целое однозначное число: '))
rate.append(user_num)
rate.sort(reverse=True)
print(rate)

# Задание 6 - 1 вариант

good_name = input("Введите названия товаров через запятую: ")
good_price = input("Введите цены внесенных товаров через запятую соответственно: ")
good_color = input("Введите цвета внесенных товаров через запятую соответственно: ")
good_quality = input("Введите качество внесенных товаров через запятую соответственно, исходя из значений 'Высокое', 'Среднее' и 'Низкое': ")
good_size = input("Введите размеры внесенных товаров через запятую соответственно: ")
good_name = good_name.split(',')
good_price = good_price.split(',')
good_color = good_color.split(',')
good_quality = good_quality.split(',')
good_size = good_size.split(',')
a = 0
goods_list = []
while a < len(good_name):
    good = (a+1, dict(
        Название=good_name[a],
        Цена=float(good_price[a]),
        Цвет=good_color[a],
        Качество=good_quality[a],
        Размер=float(good_size[a])
        )
    )
    goods_list.append(good)
    a = a+1
print(goods_list)
a = 0
price = 0
while a < len(good_name)-1:
    price = int(good_price[a]) + int(good_price[a+1])
    a = a + 1
avg_price = price/len(good_name)
goods_analitics = dict(
    Товары=good_name,
    Всего_товаров=len(good_name),
    Средняя_цена=round(avg_price)
)
print(goods_analitics)

# Задание 6 - 2 вариант

good_name = ''
good_price = ''
good_color = ''
good_quality = ''
good_size = ''
a = 0
goods_list = []
while a < 3:
    good_name = input("Введите название товара " + str(a+1) + ": ")
    good_price = input("Введите цену товара " + str(a+1) + ": ")
    good_color = input("Введите цвет товара " + str(a+1) + ": ")
    good_quality = input("Введите качество товара, исходя из значений 'Высокое', 'Среднее' и 'Низкое' " + str(a+1) + ": ")
    good_size = input("Введите размер товара " + str(a+1) + ": ")
    good = (a+1, dict(
        Название=good_name,
        Цена=float(good_price),
        Цвет=good_color,
        Качество=good_quality,
        Размер=float(good_size)
        ))
    goods_list.append(good)
    a = a+1

print(goods_list)

a = 0
goods_names = []
goods_prices = []
goods_sizes = []
while a < len(goods_list):
    good = goods_list[a]
    good_info = good[1]
    good_name_a = good_info.setdefault('Название')
    goods_names.append(good_name_a)
    a = a + 1
a = 0
while a < len(goods_list):
    good = goods_list[a]
    good_info = good[1]
    goods_price_a = good_info.setdefault('Цена')
    goods_prices.append(goods_price_a)
    a = a + 1
a = 0
while a < len(goods_list):
    good = goods_list[a]
    good_info = good[1]
    good_size_a = good_info.setdefault('Цена')
    goods_sizes.append(good_size_a)
    a = a + 1
goods_analitics = dict (
    Товары=goods_names,
    Цены_товаров=goods_prices,
    Размеры_товаров=goods_sizes
)
print(goods_analitics)