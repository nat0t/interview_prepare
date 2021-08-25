"""
Написать программу, которая запрашивает у пользователя ввод числа. На введенное число она отвечает сообщением, целое оно
или дробное. Если дробное — необходимо далее выполнить сравнение чисел до и после запятой. Если они совпадают, программа
должна возвращать значение True, иначе False.
"""


def calc_frac(number) -> bool:
    if not number % 1:
        print('Received number is integer.')
    else:
        print('Received number is fractional.')
        whole, frac = str(number).split('.')
        return True if whole == frac else False


if __name__ == '__main__':
    float_false_num = 5.86
    float_true_num = 52.52
    int_num = 5

    print(calc_frac(float_false_num))
    print(calc_frac(float_true_num))
    print(calc_frac(int_num))
