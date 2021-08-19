"""
Написать функцию, реализующую вывод таблицы умножения размерностью AｘB. Первый и второй множитель должны задаваться в
виде аргументов функции. Значения каждой строки таблицы должны быть представлены списком, который формируется в цикле.
После этого осуществляется вызов внешней lambda-функции, которая формирует на основе списка строку. Полученная строка
выводится в главной функции. Элементы строки (элементы таблицы умножения) должны разделяться табуляцией.
"""


def get_row(columns: int, row_number: int) -> list:
    return [str(row_number * column_number) for column_number in range(1, columns + 1)]


def get_mul_table(columns: int, rows: int) -> str:
    table = ''
    for row_number in range(1, rows + 1):
        table += '\t'.join(get_row(columns, row_number)) + '\n'
    return table


if __name__ == '__main__':
    print(get_mul_table(12, 20))
