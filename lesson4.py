# 1
def calc():
    x = float(input('Введите количество отработанных часов : '))
    y = float(input('Введите суммы оплаты труда за 1 час : '))
    c = float(input('Укажите размер премии - '))
    pay = x * y
    return pay + c


print(f'Размер заработной платы составил: {calc()}')

# 2
in_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
res_list = [number for i, number in enumerate(in_list) if i > 0 and in_list[i] > in_list[i - 1]]
print(res_list)

# 3
my_list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
print(my_list)

# 4
from random import randint

my_list = [randint(0, 20) for _ in range(20)]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(f"{my_list} {new_list}")

# 5
from functools import reduce


def my_list(el_1, el_2):
    return el_1 * el_2


new_list = [el for el in range(100, 1001, 2)]
print(f"{new_list} {reduce(my_list, new_list)}")

# 6
from itertools import count, cycle

for i in count(int(
        input("Введите число. Для следующего числа нажмите Enter. Для выхода из программы нажмите 'q'. Ваше число: "))):
    print(i, end='')
    ex = input()
    if ex == "q":
        break

new_list = input('введите числа разделеные пробелом. Для выхода нажмите "q"').split()
iter = cycle(new_list)
ex = None

while ex != "q":
    print(next(iter), end="")
    ex = input("введите число")


# 7
def fact_gen(number):
    temp = 1
    if number == 0:
        yield f'{number}! = 1'
    for i in range(1, number + 1):
        temp *= i
        yield f'{i}! = {temp}'


for el in fact_gen(int(input("Укажите факториал какого числа Вы хотели бы узнать?"))):
    print(el)
