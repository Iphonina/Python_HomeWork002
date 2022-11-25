# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]
import random

size = int(input('Введите длину списка: '))
list_1 = []
for n in range(size):
    list_1.append(random.randint(1000, 10000))
print(list_1)
list_2 = []
find = input('Введите цифру: ')
for number in list_1:
    number = str(number).replace(f'{find}', "")
    list_2.append(int(number))
print(list_2)
list_3 = []
for number in list_2:
    while number > 9:
        number = sum(map(int, str(number)))
    list_3.append(number)
print(list_3)
print(list(set(list_3)))
