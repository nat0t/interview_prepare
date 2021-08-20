"""
Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации (нуль необходимо
исключить). Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону:
“elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.
"""
import random


def randomizer(start: float, end: float, numbers: int) -> None:
    rand_list = []
    rand_dict = {}

    while numbers > 0:
        number = random.uniform(start, end)
        if number:
            rand_list.append(number)
            rand_dict[f'elem_{numbers}'] = number
            numbers -= 1
    print(rand_list)
    print(rand_dict)


if __name__ == '__main__':
    randomizer(-5, 2, 10)
