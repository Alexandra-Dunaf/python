#1
def div():
    try:
        args1 = int(input("напишите число"))
        args2 = int(input("напишите еще 1 число, кроме 0"))
        res = args1 / args2
    except ValueError:
        return 'Ошибка, нужно напечатать цифру'
    except ZeroDivisionError:
        return "Ни та цифра! Вы не можете использовать 0 в качестве делителя"
    return res
print(f'результат  {div()}')


# 2
def info(**kwargs):
    return ' '.join(kwargs.values())


print(info(name=input('имя: '), s_name=input('фамилия: '), city=input('дата рождения: '),
           l_town=input('город проживания: '), email=input('e-mail: '), tel=input('номер телефона: ')))


# 3
def my_func(arg1, arg2, arg3):
   return sum(sorted([arg1,arg2,arg3])[1:])
print(my_func(arg1 = int(input('1е число: ')), arg2 = int(input('2е число: ')), arg3 = int(input('3е число: '))))


# 4
def power(x, y):
    res = 1
    for i in range(abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1 / res
print(power(float(input("введите положительное число, х = ")), int(input("введите целое отрицательное число, у = "))))


# 5
def sum_num():
    res = 0
    while True:
        in_list = input('введите числа через пробел, для выхода нажмите "*" ').split()
        for num in in_list:
            if num == '*':
                return res
            else:
                try:
                    res += int(num)
                except ValueError:
                    print("если вы хотите выйти из программы, наберите ' * '")
        print(f"Сумма = {res}")
print(sum_num())


# 6
def int_func():
    word = input("введите несколько слов через пробел ")
    print(word.title())
    return
int_func()
