# 1
my_list = [1, 5.4, "world", (1, 2), True, {1, 5}]
for i in my_list:
    print(f"{i} - {type(i)}")

# 2
numbers = list(input("Введите числа"))
for i in range(1, len(numbers), 2):
    numbers[i - 1], numbers[i] = numbers[i], numbers[i - 1]
print(numbers)

# 3
month = int(input("Введите число от 1 до 12"))
my_list = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь",
           "декабрь"]
my_dict = {1: "январь", 2: "февраль", 3: "март", 4: "апрель", 5: "май", 6: "июнь", 7: "июль", 8: "август",
           9: "сентябрь", 10: "октябрь", 11: "ноябрь", 12: "декабрь"}
print(my_list[month - 1])
print(my_dict[month])

# 4
world = input('Введите несколько слов, разделенных пробелами').split()
for i, n in enumerate(world, 1):
    print(i, n) if len(world) <= 10 else print(i, world[:10])

# 5
my_list = [7, 5, 3, 3, 2]
rating = int(input("Введите число"))
i = 0
for n in my_list:
    if rating <= n:
        i += 1
my_list.insert(i, rating)
print(my_list)
