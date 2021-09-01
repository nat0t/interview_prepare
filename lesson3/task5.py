"""
Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке часть строковых значений заменить
на значения типа example345 (строка+число). Далее — усовершенствовать вторую функцию из предыдущего примера (функцию
извлечения данных). Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям: вывод первого
вхождения, вывод всех вхождений. Реализовать замену всех найденных подстрок на новое значение и вывод всех подстрок,
состоящих из букв и цифр и имеющих пробелы только в начале и конце — например, example345.
"""
import os
import random
import string


def create_file(path: str, rows: int) -> None:
    if os.path.exists(path):
        print(f'File {path} exists.')
    else:
        chars = [random.choice(string.ascii_letters) for _ in range(rows)]
        numbers = [f'{random.choice(string.ascii_letters)}{random.choice(string.digits)}' for _ in range(rows)]
        with open(path, 'w') as file:
            for row in zip(chars, numbers):
                file.write('{}\t{}\n'.format(*row))


def read_file(path: str, template: str = None) -> None:
    found = []

    with open(path) as file:
        for row in file.readlines():
            print(row.strip())

            if template:
                try:
                    found_index = row.index(template)
                    found.append(row[found_index:found_index + len(template)])
                except ValueError:
                    pass
    print(f'List of found: {found}')


if __name__ == '__main__':
    path_file = 'test.txt'
    rows_number = 10

    create_file(path_file, rows_number)
    read_file(path_file, 'Y1')
