"""
Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл. Если файл с
таким именем уже существует, выводим соответствующее сообщение. Необходимо открыть файл и подготовить два списка: с
текстовой и числовой информацией. Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом, чтобы каждая строка файла
содержала текстовое и числовое значение. Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл. Во
второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого. Вся программа должна
запускаться по вызову первой функции.
"""
import os
import random
import string


def create_file(path, rows):
    if os.path.exists(path):
        print(f'File {path} exists.')
    else:
        chars = [random.choice(string.ascii_letters) for _ in range(rows)]
        numbers = [random.choice(string.digits) for _ in range(rows)]
        with open(path, 'w') as file:
            for row in zip(chars, numbers):
                file.write('{}\t{}\n'.format(*row))


def read_file(path):
    with open(path) as file:
        for row in file.readlines():
            print(row.replace('\n', ''))


if __name__ == '__main__':
    path_file = 'test.txt'
    rows_number = 10

    create_file(path_file, rows_number)
    read_file(path_file)
