"""
Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь. Если ключу не хватает значения, в словаре
для него должно сохраняться значение None. Значения, которым не хватило ключей, необходимо отбросить.
"""
from itertools import zip_longest


def construct_dict(keys: list, values: list) -> dict:
    return dict(zip_longest(keys, values)) if len(keys) > len(values) else dict(zip(keys, values))


if __name__ == '__main__':
    lst1 = ['a', 'b', 'c', 'd', 'e']
    lst2 = [1, 2, 3]
    lst3 = [1, 2, 3, 4, 5, 6, 7]

    print(construct_dict(lst1, lst2))
    print(construct_dict(lst1, lst3))
