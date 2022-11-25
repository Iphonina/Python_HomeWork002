# Реализуйте алгоритм перемешивания списка.
# Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод.
import random

num = int(input('Введите длину списка: '))
numbers = []
for n in range(num):
    numbers.append(random.randint(1, 50))
print(numbers)
new_list = numbers
for i in range(0, len(new_list)):
    index_rnd = random.randint(0, len(new_list)-1)
    temp = new_list[i]
    new_list[i] = new_list[index_rnd]
    new_list[index_rnd] = temp
print(new_list)



